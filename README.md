<div align="center">

<a href="https://github.com/mark-Aryan/Retriever">
  <img src="https://readme-typing-svg.demolab.com?font=Syne&weight=800&size=42&duration=3000&pause=1000&color=C41E1E&center=true&vCenter=true&width=700&lines=Retriever;Campus+Lost+%26+Found;Find+What+Matters." alt="Retriever - Campus Lost and Found Platform" />
</a>

<br/>

<p align="center">
  <b>A peer-to-peer campus lost and found platform — built for students, by students.</b><br/>
  <i>Every lost item has a story. Retriever helps write the ending.</i>
</p>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/Flask-3.1.0-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Pillow-11.1.0-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Pillow"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Active"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-blueviolet?style=for-the-badge" alt="PRs Welcome"/>
</p>

<p align="center">
  <a href="#-about">About</a> ·
  <a href="#-features">Features</a> ·
  <a href="#-demo">Demo</a> ·
  <a href="#-installation">Installation</a> ·
  <a href="#-api-reference">API</a> ·
  <a href="#-tech-stack">Tech Stack</a> ·
  <a href="#-contributing">Contributing</a> ·
  <a href="#-license">License</a>
</p>

---

</div>

## 📖 About

**Retriever** is a full-stack, peer-to-peer campus lost and found web application designed to connect students with their misplaced belongings. Built with a lightweight Flask backend and a typographically rich, mobile-first vanilla frontend, Retriever prioritizes privacy, authentic ownership verification, and a seamless campus experience.

> 🎓 Developed as a Final Year Major Project · A Campus Technology Initiative by [Aryan Kumar Upadhyay](https://codexploit.in)

Whether you found someone's ID card near the library or lost your headphones in the canteen — Retriever bridges the gap without friction.

```
Lost something? → Browse live posts → Reach out with a genuine description → Get it back.
Found something? → Post it in 60 seconds → Wait for the real owner to reach out. → Mark it returned.
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔒 Privacy-First Authentication
Full student registration using real college credentials (Roll No., Department, Year). Contact details remain completely hidden until a user logs in — no cold calls, no spam.

</td>
<td width="50%">

### 🕵️ Genuine Reach-Out System
Claim requests require a **minimum 30-character description** proving familiarity with the item. Multiple students can reach out — the finder sees all requests with full claimant details.

</td>
</tr>
<tr>
<td width="50%">

### 🖼️ Smart Image Processing
Every uploaded image is automatically resized (max 1200×1200px) and compressed using **Pillow** before saving — keeping the platform fast and storage lean without sacrificing quality.

</td>
<td width="50%">

### 📊 Live Platform Statistics
Real-time counters for active items, recovered items, total users, and reach-outs — dynamically fetched via a lightweight `/api/stats` JSON endpoint and rendered client-side with vanilla JS.

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Powerful Search & Filter
Full-text search across titles and descriptions, plus category and location filters — all wired up as URL parameters so search results are shareable and bookmarkable.

</td>
<td width="50%">

### 📱 Mobile-First Responsive Design
Crafted with semantic HTML5 and pure CSS3 — no frameworks, no bloat. A vintage editorial aesthetic with crisp typography ensures a premium experience on any screen size.

</td>
</tr>
</table>

**More features at a glance:**
- 🧾 Public browsing — no login required to view items
- 🗂️ Category and location tagging per item
- 📬 Per-item reach-out inbox visible only to the finder
- ✅ Mark item as returned / delete post from dashboard
- 🛡️ PBKDF2 SHA-256 password hashing via Werkzeug
- 🔑 UUID-based public item IDs (no sequential DB IDs exposed)
- 🧹 Auto-deletes image file on item deletion

---

## 🎬 Demo

<div align="center">

> 📸 *Replace the placeholder below with your actual demo GIF or screenshot.*

<img src="demo-animation.gif" alt="Retriever - Campus Lost and Found Demo" width="90%" style="border-radius: 10px; box-shadow: 0 8px 24px rgba(0,0,0,0.15);" />

</div>

### Screenshots

| Browse | Item Detail | Dashboard |
|--------|-------------|-----------|
| ![Browse](docs/screenshots/browse.png) | ![Item Detail](docs/screenshots/detail.png) | ![Dashboard](docs/screenshots/dashboard.png) |

---

## ⚙️ Installation

### Prerequisites

- Python **3.9+**
- `pip` (comes with Python)
- Git

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/mark-Aryan/Retriever.git
cd retriever

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Visit **http://localhost:5000** — the SQLite database and upload directory are created automatically on first run.

### Environment Variables *(optional)*

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | random (each restart) | Flask session secret. Set a fixed value in production. |
| `UPLOAD_FOLDER` | `static/uploads` | Directory for uploaded images |
| `MAX_CONTENT_LENGTH` | `10MB` | Max file upload size |

> ⚠️ **Production Note:** The default `app.secret_key = os.urandom(24).hex()` generates a new key on every restart, which invalidates all active sessions. In production, set a fixed secret key via environment variable.

---

## 📁 Project Structure

```
retriever/
├── app.py                  ← Flask backend — all routes, auth, DB, API, uploads
├── requirements.txt        ← Python dependencies
├── lostfound.db            ← Auto-created SQLite database (gitignored)
├── static/
│   ├── css/
│   │   └── style.css       ← Complete white + red vintage UI (no frameworks)
│   ├── js/
│   │   └── main.js         ← Live stats polling, mobile menu, flash auto-dismiss
│   └── uploads/            ← Uploaded item images (gitignored)
├── templates/
│   ├── base.html           ← Master layout — topbar, navbar, footer
│   ├── index.html          ← Browse, search, filter
│   ├── item.html           ← Item detail + reach-out form
│   ├── upload.html         ← Post found item + drag-and-drop upload
│   ├── dashboard.html      ← User's active posts and submitted reach-outs
│   ├── login.html          ← Login page
│   └── register.html       ← Student registration
├── docs/
│   └── screenshots/        ← App screenshots for README
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
└── LICENSE
```

---

## 🌐 API Reference

Retriever exposes a minimal public JSON API for live statistics.

### `GET /api/stats`

Returns real-time platform statistics.

**Response:**
```json
{
  "active": 42,
  "closed": 17,
  "users": 120,
  "reachouts": 89
}
```

| Field | Type | Description |
|---|---|---|
| `active` | integer | Number of currently active (unresolved) items |
| `closed` | integer | Number of items marked as returned |
| `users` | integer | Total registered students |
| `reachouts` | integer | Total ownership reach-out submissions |

---

## 🗄️ Database Schema

```sql
-- Registered students
CREATE TABLE users (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    email      TEXT UNIQUE NOT NULL,
    roll       TEXT UNIQUE NOT NULL,
    dept       TEXT NOT NULL,
    year       TEXT NOT NULL,
    phone      TEXT NOT NULL,
    password   TEXT NOT NULL,            -- PBKDF2 SHA-256 hashed
    avatar     TEXT DEFAULT NULL,
    created_at TEXT DEFAULT (datetime('now','localtime'))
);

-- Found item listings
CREATE TABLE items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    uid         TEXT UNIQUE NOT NULL,    -- Public-facing 8-char UUID slug
    user_id     INTEGER NOT NULL REFERENCES users(id),
    title       TEXT NOT NULL,
    category    TEXT NOT NULL,
    location    TEXT NOT NULL,
    description TEXT NOT NULL,
    image       TEXT NOT NULL,
    status      TEXT DEFAULT 'active',  -- 'active' | 'closed'
    created_at  TEXT DEFAULT (datetime('now','localtime'))
);

-- Ownership claim requests
CREATE TABLE reachouts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id     INTEGER NOT NULL REFERENCES items(id),
    user_id     INTEGER NOT NULL REFERENCES users(id),
    description TEXT NOT NULL,          -- Min 30 characters required
    status      TEXT DEFAULT 'pending',
    created_at  TEXT DEFAULT (datetime('now','localtime'))
);
```

---

## 🏗️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python 3.9 + Flask 3.1 | Routing, auth, business logic |
| Auth | Flask-Login + Werkzeug | Session management + PBKDF2 password hashing |
| Database | SQLite3 | Zero-config, file-based relational DB |
| Image Processing | Pillow 11.1 | Auto-resize + compress on upload |
| Frontend | HTML5 + CSS3 + Vanilla JS | UI — no frameworks, no build step |
| Typography | Cormorant Garamond · Syne · DM Mono | Brand typography via Google Fonts |

---

## 🗺️ Roadmap

- [ ] Email verification on registration
- [ ] Admin moderation panel
- [ ] Push / email notifications when a reach-out is received
- [ ] QR code generation for printed "Found Item" posters
- [ ] OAuth login (Google Workspace for campus SSO)
- [ ] REST API with token auth for mobile app
- [ ] Docker deployment config

---

## 🤝 Contributing

Contributions are what make open source incredible. Any contribution you make is **greatly appreciated**.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on code style, commit messages, and the review process.

---

## 🔐 Security

If you discover a security vulnerability, please **do not** open a public issue. Follow the responsible disclosure process outlined in [SECURITY.md](SECURITY.md).

---

## 📜 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a full history of releases and changes.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for full terms.

---

## 👨‍💻 Author

<div align="center">

**Aryan Kumar Upadhyay**

*Founder, CodeXploit.in · Campus Technology Initiative*

[![Website](https://img.shields.io/badge/Website-codexploit.in-C41E1E?style=for-the-badge&logo=firefox&logoColor=white)](https://codexploit.in)
[![GitHub](https://img.shields.io/badge/GitHub-@mark-Aryan-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mark-Aryan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)

</div>

---

<div align="center">

<sub>Built with ❤️ as a Final Year Major Project · <a href="https://codexploit.in">CodeXploit Campus Technology Initiative</a></sub>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=DM+Mono&size=13&duration=4000&pause=1000&color=999999&center=true&vCenter=true&width=500&lines=Made+for+students.+Built+with+purpose.;Because+every+lost+item+deserves+to+be+found." alt="Footer tagline" />

</div>
