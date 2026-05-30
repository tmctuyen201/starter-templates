# 🚀 Starter Templates

<p align="center">
  <img src="https://img.shields.io/badge/templates-3-blue?style=for-the-badge" alt="Templates">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/stars/tmctuyen201/starter-templates?style=for-the-badge" alt="Stars">
</p>

> 🧰 Production-ready starter templates to kickstart your next project. Copy, customize, and ship in minutes.

---

## 📦 Available Templates

| Template | Description | Stack | Complexity |
|----------|-------------|-------|------------|
| 🌶️ **[FastAPI + HTMX](./fastapi-htmx/)** | Full-stack web app with no JavaScript framework | FastAPI, HTMX, Jinja2 | ⭐ Easy |
| 🤖 **[Telegram Bot](./telegram-bot/)** | Feature-rich Telegram bot with payment integration | python-telegram-bot, Stripe | ⭐⭐ Medium |
| 🧩 **[Chrome Extension](./chrome-extension/)** | Modern Chrome extension with popup UI | Manifest V3, HTML/CSS/JS | ⭐ Easy |

---

## 🌶️ FastAPI + HTMX Template

Build modern, reactive web applications **without writing JavaScript**. HTMX lets you create dynamic UIs using only HTML attributes.

**Features:**
- ⚡ FastAPI backend with async support
- 🔄 HTMX for seamless partial page updates
- 🎨 Jinja2 templates with Tailwind CSS
- 📦 SQLite database with SQLAlchemy
- 🐳 Docker-ready deployment

```bash
cd fastapi-htmx
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🤖 Telegram Bot Template

A production-ready Telegram bot with built-in payment processing, inline keyboards, and conversation handling.

**Features:**
- 💳 Stripe payment integration
- 🔘 Inline keyboard menus
- 💬 Conversation state management
- 📊 User analytics tracking
- 🌐 Webhook & polling modes

```bash
cd telegram-bot
pip install -r requirements.txt
export TELEGRAM_TOKEN="your-token"
python bot.py
```

---

## 🧩 Chrome Extension Template

A modern Chrome extension built with Manifest V3. Includes popup UI, background service worker, and content script examples.

**Features:**
- 📋 Manifest V3 (latest standard)
- 🎨 Clean popup UI with CSS variables
- 🔔 Chrome notifications API
- 💾 Chrome storage API
- 🧪 Ready for Chrome Web Store submission

```bash
# Load in Chrome:
# 1. Open chrome://extensions
# 2. Enable Developer Mode
# 3. Click "Load unpacked" → select chrome-extension/
```

---

## 🏁 Quick Start

```bash
# Clone all templates
git clone https://github.com/tmctuyen201/starter-templates.git
cd starter-templates

# Pick a template and start building!
cd fastapi-htmx   # or telegram-bot / chrome-extension
```

---

## ⭐ Premium Templates — $49

<p align="center">
  <img src="https://img.shields.io/badge/💎_Premium_Templates-$49-gold?style=for-the-badge&logo=stripe&logoColor=white" alt="Premium">
</p>

Unlock **15+ premium templates** for serious developers:

- 🏢 **SaaS Boilerplate** — Auth, billing, dashboard, multi-tenant
- 📱 **React Native Starter** — Cross-platform mobile app template
- 🛒 **E-commerce API** — Full REST API with Stripe, inventory, orders
- 📊 **Admin Dashboard** — Analytics, charts, CRUD, role-based access
- 🔐 **Auth Microservice** — OAuth2, JWT, 2FA, social login
- 📝 **Blog Platform** — Markdown editor, SEO, comments, RSS
- 🤖 **AI Chat App** — OpenAI integration, streaming, history
- 📧 **Email Service** — Templates, queues, tracking, webhooks

> 💳 **One-time payment. Lifetime updates. Free new templates added monthly.**
>
> 👉 [Get Premium Templates](https://gumroad.com/l/starter-templates-premium) — Use code `SHIP50` for 50% off!

---

## 🤝 Contributing

Have a great starter template? Contributions are welcome!

1. Fork the repository
2. Add your template in a new directory
3. Include a clear README with setup instructions
4. Submit a Pull Request

---

## 📄 License

MIT License — use these templates freely in personal and commercial projects.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/tmctuyen201">tmctuyen201</a>
</p>
