# 🌶️ FastAPI + HTMX Template

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/HTMX-1.9+-blue?style=for-the-badge" alt="HTMX">
  <img src="https://img.shields.io/badge/python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

> Build modern, reactive web applications **without writing a single line of JavaScript**. HTMX + FastAPI gives you the simplicity of server-rendered HTML with the responsiveness of a SPA.

---

## ✨ Features

- ⚡ **FastAPI** — High-performance async Python web framework
- 🔄 **HTMX** — Dynamic UI updates with HTML attributes only
- 🎨 **Jinja2** — Server-side templating with template inheritance
- 📦 **SQLite** — Zero-config database via SQLAlchemy
- 🐳 **Docker** — One-command containerized deployment
- 🔥 **Hot Reload** — Instant feedback during development

## 🚀 Quick Start

```bash
pip install fastapi uvicorn jinja2 python-multipart sqlalchemy
uvicorn main:app --reload
# Open http://localhost:8000
```

## 📁 Project Structure

```
fastapi-htmx/
├── main.py              # FastAPI application
├── templates/           # Jinja2 + HTMX templates
├── static/              # CSS, JS, images
├── requirements.txt     # Python dependencies
└── Dockerfile           # Container config
```

## 🧠 How It Works

HTMX lets you make AJAX requests directly from HTML:

```html
<button hx-post="/api/like" hx-target="#likes" hx-swap="innerHTML">
  👍 Like
</button>
<span id="likes">0</span>
```

The FastAPI backend returns **HTML fragments** instead of JSON — no frontend build step needed!

## 📄 License

MIT — free for personal and commercial use.
