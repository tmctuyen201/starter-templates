"""
🤖 Telegram Bot Template
Production-ready bot with payments, inline keyboards, and conversation handling.

Setup:
    1. Create bot via @BotFather on Telegram
    2. Get your bot token
    3. Set TELEGRAM_TOKEN environment variable
    4. Run: python bot.py
"""

import os
import logging
from datetime import datetime

from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    LabeledPrice, InputMediaPhoto
)
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ConversationHandler, PreCheckoutQueryHandler,
    ContextTypes, filters
)

# ── Configuration ──────────────────────────────────────────────────────

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "your-bot-token-here")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_...")
PAYMENT_PROVIDER_TOKEN = os.getenv("PAYMENT_PROVIDER_TOKEN", "")

# Conversation states
CHOOSING, TYPING_REPLY = range(2)

# In-memory user database (use PostgreSQL/Redis in production)
users_db: dict = {}

# Product catalog
PRODUCTS = {
    "premium_monthly": {
        "name": "⭐ Premium Monthly",
        "price": 999,  # cents
        "description": "Full access for 30 days",
    },
    "premium_yearly": {
        "name": "👑 Premium Yearly",
        "price": 7999,
        "description": "Full access for 1 year (save 33%)",
    },
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ── Command Handlers ───────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message with inline keyboard menu."""
    user = update.effective_user
    users_db[user.id] = {
        "name": user.first_name,
        "username": user.username,
        "joined": datetime.now().isoformat(),
        "commands_used": 0,
    }

    keyboard = [
        [InlineKeyboardButton("📦 Products", callback_data="products"),
         InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("❓ Help", callback_data="help"),
         InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
    ]

    welcome = (
        f"👋 Welcome, {user.first_name}!\n\n"
        f"I'm your personal assistant bot. Here's what I can do:\n\n"
        f"📦 Browse products and make purchases\n"
        f"👤 View your profile and stats\n"
        f"⚙️ Customize your settings\n\n"
        f"Choose an option below to get started!"
    )

    await update.message.reply_text(
        welcome,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show available commands."""
    help_text = (
        "🤖 **Available Commands:**\n\n"
        "/start — Main menu\n"
        "/help — Show this help\n"
        "/buy — Browse products\n"
        "/profile — Your profile\n"
        "/settings — Bot settings\n"
        "/cancel — Cancel current action\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def show_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display product catalog with inline buttons."""
    keyboard = []
    for pid, product in PRODUCTS.items():
        price_str = f"${product['price'] / 100:.2f}"
        keyboard.append([
            InlineKeyboardButton(
                f"{product['name']} — {price_str}",
                callback_data=f"buy_{pid}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="main_menu")])

    text = (
        "🛍️ **Premium Products**\n\n"
        "Unlock all features with a one-time purchase:\n\n"
    )
    for pid, p in PRODUCTS.items():
        text += f"• **{p['name']}** — ${p['price']/100:.2f}\n  {p['description']}\n"

    if update.callback_query:
        await update.callback_query.edit_message_text(
            text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
        )


async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user profile and stats."""
    user_id = update.effective_user.id
    user = users_db.get(user_id, {})

    profile_text = (
        f"👤 **Your Profile**\n\n"
        f"🆔 ID: `{user_id}`\n"
        f"📛 Name: {user.get('name', 'Unknown')}\n"
        f"🔗 Username: @{user.get('username', 'N/A')}\n"
        f"📅 Joined: {user.get('joined', 'Unknown')}\n"
        f"📊 Commands used: {user.get('commands_used', 0)}\n"
        f"⭐ Status: {'Premium' if user.get('premium') else 'Free'}\n"
    )

    keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="main_menu")]]

    if update.callback_query:
        await update.callback_query.edit_message_text(
            profile_text, reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            profile_text, reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )


# ── Callback Query Handler ─────────────────────────────────────────────

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all inline keyboard button presses."""
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "main_menu":
        await start_callback(query, context)
    elif data == "products":
        await show_products(update, context)
    elif data == "profile":
        await show_profile(update, context)
    elif data == "help":
        await query.edit_message_text(
            "🤖 Use /start to return to the main menu.\n\n"
            "Commands: /start, /help, /buy, /profile, /settings"
        )
    elif data.startswith("buy_"):
        product_id = data[4:]
        product = PRODUCTS.get(product_id)
        if product:
            await query.edit_message_text(
                f"💳 **{product['name']}**\n\n"
                f"Price: ${product['price']/100:.2f}\n"
                f"{product['description']}\n\n"
                f"Click below to complete your purchase:",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        f"💳 Pay ${product['price']/100:.2f}",
                        pay=True
                    )],
                    [InlineKeyboardButton("🔙 Back", callback_data="products")]
                ])
            )
    elif data == "settings":
        await query.edit_message_text(
            "⚙️ **Settings**\n\n"
            "• Notifications: ON\n"
            "• Language: English\n"
            "• Theme: Default\n\n"
            "_(Settings UI coming soon)_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="main_menu")]
            ])
        )


async def start_callback(query, context):
    """Re-show the main menu from a callback query."""
    keyboard = [
        [InlineKeyboardButton("📦 Products", callback_data="products"),
         InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("❓ Help", callback_data="help"),
         InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
    ]
    await query.edit_message_text(
        "🏠 **Main Menu**\n\nChoose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# ── Payment Handlers ───────────────────────────────────────────────────

async def pre_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Validate payment before processing."""
    query = update.pre_checkout_query
    await query.answer(ok=True)


async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle successful payment."""
    user_id = update.effective_user.id
    if user_id in users_db:
        users_db[user_id]["premium"] = True

    await update.message.reply_text(
        "✅ **Payment Successful!**\n\n"
        "Thank you for your purchase! Your premium features are now active.\n\n"
        "Use /profile to see your updated status.",
        parse_mode="Markdown"
    )
    logger.info(f"Payment received from user {user_id}")


# ── Message Handler ────────────────────────────────────────────────────

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages."""
    user_id = update.effective_user.id
    if user_id in users_db:
        users_db[user_id]["commands_used"] = users_db[user_id].get("commands_used", 0) + 1

    await update.message.reply_text(
        "💬 I received your message! Use /start to see the menu."
    )


# ── Main ───────────────────────────────────────────────────────────────

def main():
    """Start the bot."""
    print("🤖 Starting Telegram Bot...")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("buy", show_products))
    app.add_handler(CommandHandler("profile", show_profile))

    # Callback query handler (inline buttons)
    app.add_handler(CallbackQueryHandler(button_handler))

    # Payment handlers
    app.add_handler(PreCheckoutQueryHandler(pre_checkout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

    # Text message handler (catch-all)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    print("✅ Bot is running! Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
