<div align="center">

# ⚡ USMANI BILLING

### `// A neon-cyberpunk billing terminal built with Streamlit`

[![Python](https://img.shields.io/badge/Python-3.9%2B-00fff0?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-ff00e6?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/STATUS-ONLINE-7c4dff?style=for-the-badge)](#)
[![Made By](https://img.shields.io/badge/MADE_BY-Mohd_Faizan_Usmani-00fff0?style=for-the-badge)](#)

<br/>



### 🔗 [**LAUNCH LIVE DEMO »**](https://usmani-billing.streamlit.app/)


</div>

---

## ◈ Overview

**Usmani Billing** is a lightweight, single-file billing / invoicing terminal built entirely in [Streamlit](https://streamlit.io/). It features a full neon cyberpunk interface — glowing cards, a scanline grid backdrop, and glassmorphic panels — while staying 100% functional as a real add-item / calculate-total / delete-item billing tool.

No database, no backend, no setup headaches — just run one file and you're billing.

---

## ▹ Features

| ⚡ | Feature |
|---|---|
| 🧾 | Add items with name, quantity & price in one form |
| 🗑️ | One-tap delete per line item (mobile-safe, stays inline on small screens) |
| Σ | Live grand-total calculation, auto-updated on every change |
| ⌫ | One-click **Purge Ledger** to clear the entire bill |
| 🎨 | Full neon / cyberpunk UI — glowing borders, gradient text, grid backdrop |
| 📱 | Responsive layout — tested on both desktop and mobile viewports |

---

## ▹ Tech Stack

- **[Streamlit](https://streamlit.io/)** — UI & app framework
- **[Pandas](https://pandas.pydata.org/)** — data handling
- **Custom CSS** — Orbitron + Share Tech Mono fonts, neon glow effects, animated hover states

---

## ▹ Getting Started

### 1. Clone / download this repo

```bash
git clone https://github.com/<your-username>/usmani-billing.git
cd usmani-billing
```

### 2. Install dependencies

```bash
pip install streamlit pandas
```

### 3. Run the app

```bash
streamlit run billing_app.py
```

The app will open automatically at `http://localhost:8501`.

---

## ▹ Deployment

To get a real, shareable **live demo link** for the badge above:

1. Push this project to a public GitHub repo.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Deploy `billing_app.py` from your repo — Streamlit Cloud gives you a free `*.streamlit.app` URL.
4. Replace the placeholder link at the top of this README with your real URL.

---

## ▹ Project Structure

```
usmani-billing/
├── billing_app.py         # Main Streamlit application
├── assets/
│   └── demo-preview.svg   # README preview banner
└── README.md               # You are here
```

---

## ▹ Roadmap

- [ ] Export bill as PDF / image
- [ ] Item categories & tags
- [ ] Local persistence (save bills between sessions)
- [ ] Multi-currency support
- [ ] Dark / neon theme toggle

---

<div align="center">

### `SYSTEM.CREDITS`

Built with ⚡ by **Mohd Faizan Usmani**

<sub>USMANI_BILLING.SYS · v1.0</sub>

</div>
