# 🧩 Chrome Extension Template

<p align="center">
  <img src="https://img.shields.io/badge/Manifest-V3-green?style=for-the-badge&logo=googlechrome" alt="Manifest V3">
  <img src="https://img.shields.io/badge/HTML-5-orange?style=for-the-badge&logo=html5" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS-3-blue?style=for-the-badge&logo=css3" alt="CSS3">
  <img src="https://img.shields.io/badge/JS-ES6-yellow?style=for-the-badge&logo=javascript" alt="JavaScript">
</p>

> A modern Chrome extension template with Manifest V3. Clean popup UI, background service worker, and content script — ready to customize and publish to the Chrome Web Store.

---

## ✨ Features

- 📋 **Manifest V3** — Latest Chrome extension standard
- 🎨 **Popup UI** — Clean, responsive popup interface
- 🔔 **Notifications** — Chrome notifications API
- 💾 **Storage** — Chrome storage API for persistent data
- 🧩 **Content Script** — Inject into web pages
- ⚡ **Service Worker** — Background processing with Manifest V3
- 🧪 **Ready for Chrome Web Store** — Proper metadata and icons

## 🚀 Quick Start

```bash
# 1. Clone or download this template
# 2. Open Chrome → chrome://extensions
# 3. Enable "Developer mode" (top right)
# 4. Click "Load unpacked" → select this directory
# 5. Click the extension icon in the toolbar!
```

## 📁 Project Structure

```
chrome-extension/
├── manifest.json        # Extension configuration
├── popup.html           # Popup UI
├── popup.js             # Popup logic
├── popup.css            # Popup styles
├── background.js        # Service worker
├── content.js           # Content script (injected into pages)
├── icons/               # Extension icons (16, 48, 128px)
└── README.md            # This file
```

## 🎨 Customization

### Change Extension Name
Edit `manifest.json` → `name` and `short_name` fields.

### Add Permissions
Edit `manifest.json` → `permissions` array. Available permissions:
- `storage` — Save data locally
- `activeTab` — Access current tab
- `notifications` — Show system notifications
- `tabs` — Access browser tabs

### Modify Popup
Edit `popup.html` for layout, `popup.css` for styles, `popup.js` for logic.

## 📦 Publishing to Chrome Web Store

1. Create a ZIP of this directory
2. Go to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)
3. Pay one-time $5 developer fee
4. Upload your ZIP
5. Fill in listing details and screenshots
6. Submit for review

## 📄 License

MIT — free for personal and commercial use.
