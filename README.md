# 🚀 Starter Templates

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/tmctuyen201/starter-templates?style=for-the-badge&logo=github&color=yellow)](https://github.com/tmctuyen201/starter-templates/stargazers)
[![Templates](https://img.shields.io/badge/Templates-3-orange?style=for-the-badge)](#-templates)

**Production-ready project templates to ship your next product in hours, not weeks.**

Each template includes authentication, deployment configs, CI/CD, and best practices built-in.

[Templates](#-templates) • [Quick Start](#-quick-start) • [Premium](#-premium-templates--49)

</div>

---

## 📦 Templates

### 1. 🍦 FastAPI + HTMX + SQLite — Micro-SaaS Starter

**Perfect for:** Side projects, micro-SaaS, internal tools, admin dashboards

| Feature | Included |
|---------|----------|
| FastAPI backend | ✅ |
| HTMX frontend (no JS framework needed) | ✅ |
| SQLite database | ✅ |
| User authentication (JWT) | ✅ |
| Docker + docker-compose | ✅ |
| Makefile with dev commands | ✅ |
| GitHub Actions CI | ✅ |
| TailwindCSS styling | ✅ |

**Quick Start:**
```bash
cd templates/fastapi-htmx-sqlite
cp .env.example .env
docker-compose up -d
# Open http://localhost:8000
```

**Tech Stack:** FastAPI · HTMX · SQLite · TailwindCSS · Docker

---

### 2. 🤖 Telegram Bot with Payments — Stripe Integration

**Perfect for:** Paid bots, digital product delivery, subscription services, SaaS bots

| Feature | Included |
|---------|----------|
| python-telegram-bot | ✅ |
| Stripe payment integration | ✅ |
| Webhook handler | ✅ |
| User database (SQLite) | ✅ |
| Subscription management | ✅ |
| Docker + docker-compose | ✅ |
| Makefile | ✅ |
| Admin commands | ✅ |

**Quick Start:**
```bash
cd templates/telegram-bot-payments
cp .env.example .env
# Edit .env with your BOT_TOKEN and STRIPE_KEY
docker-compose up -d
```

**Tech Stack:** Python · Telegram Bot API · Stripe · SQLite · Docker

---

### 3. 🧩 Chrome Extension — Manifest V3 + React

**Perfect for:** Browser extensions, SaaS tools, productivity apps

| Feature | Included |
|---------|----------|
| Manifest V3 | ✅ |
| React 18 + TypeScript | ✅ |
| Vite build system | ✅ |
| Content scripts | ✅ |
| Background service worker | ✅ |
| Popup + Options page | ✅ |
| Chrome Storage API | ✅ |
| Hot reload in dev | ✅ |

**Quick Start:**
```bash
cd templates/chrome-extension-react
npm install
npm run dev
# Load dist/ folder in chrome://extensions
```

**Tech Stack:** React · TypeScript · Vite · Chrome Manifest V3

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/tmctuyen201/starter-templates.git
cd starter-templates

# Choose a template
cd templates/fastapi-htmx-sqlite    # For web apps
cd templates/telegram-bot-payments   # For Telegram bots
cd templates/chrome-extension-react  # For browser extensions

# Follow the template's README
cp .env.example .env
```

---

## 📁 Each Template Includes

```
template/
├── README.md          # Detailed setup guide
├── Makefile           # Dev commands (make dev, make test, make deploy)
├── docker-compose.yml # One-command deployment
├── .env.example       # Environment variables template
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions CI
├── src/               # Source code
├── tests/             # Test suite
└── docs/              # Documentation
```

---

## 💎 Premium Templates — $49

Get the **complete collection** with production-ready features:

| Feature | Free | Premium ($49) |
|---------|------|---------------|
| Basic templates | ✅ | ✅ |
| Stripe full integration | ❌ | ✅ |
| OAuth (Google, GitHub) | ❌ | ✅ |
| Role-based access control | ❌ | ✅ |
| Email notifications | ❌ | ✅ |
| Deployment guides (AWS, Vercel, Railway) | ❌ | ✅ |
| CI/CD templates | ❌ | ✅ |
| Database migrations | ❌ | ✅ |
| Monitoring & logging | ❌ | ✅ |
| Priority support | ❌ | ✅ |
| Lifetime updates | ❌ | ✅ |

### 🎁 Get Premium

**👉 [Buy Premium Templates — $49](https://gumroad.com/l/starter-templates-premium)**

> 🎉 **Launch Special:** Use code `SHIP50` for 50% off!

---

## 🤝 Contributing

```bash
git clone https://github.com/tmctuyen201/starter-templates.git
cd starter-templates
# Add your template in templates/
# Submit a PR!
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**⭐ Star this repo if it helped you ship faster!**

Made with ❤️ by [@tmctuyen201](https://github.com/tmctuyen201)

[![Twitter](https://img.shields.io/twitter/follow/tmctuyen201?style=social)](https://twitter.com/tmctuyen201)

</div>
