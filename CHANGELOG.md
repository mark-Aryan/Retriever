# Changelog

All notable changes to **Retriever — Campus Lost & Found** are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Email verification on student registration
- Admin moderation panel
- Push/email notifications for reach-outs
- QR code generation for printed "Found Item" posters
- OAuth login (Google Workspace campus SSO)
- Docker deployment configuration
- REST API with token auth for future mobile app

---

## [1.0.0] — 2025

### Added
- Full student registration with Roll No., Department, Year, Phone, and Email
- Secure login via email or roll number
- PBKDF2 SHA-256 password hashing (via Werkzeug)
- Post found items with title, category, location, description, and image
- Drag-and-drop image upload with Pillow auto-resize (max 1200×1200px, quality 85)
- UUID-based public item slugs (8-char uppercase, no sequential IDs exposed)
- Public item browse page with keyword search, category filter, and location filter
- Item detail page showing full description and all reach-outs (for the finder)
- Reach-out system with 30-character minimum description requirement
- One reach-out per user per item enforcement
- User dashboard — view own posts with reach-out count, and own submitted reach-outs
- Mark item as returned (`status = 'closed'`) via dashboard
- Delete item (cascades to reach-outs, removes image file from disk)
- Live platform statistics via `/api/stats` JSON endpoint
- Real-time header/footer stats via vanilla JS polling
- Mobile-first responsive design — no CSS frameworks
- Vintage editorial UI — Cormorant Garamond, Syne, DM Mono typography
- Flash messages with auto-dismiss (via JS)
- Mobile navigation menu toggle
- SQLite database with foreign key enforcement
- Auto-create `static/uploads/` directory and database on first run
- `ALLOWED` extension whitelist for uploads (png, jpg, jpeg, gif, webp)

---

## Format Reference

```
## [version] — YYYY-MM-DD

### Added      — New features
### Changed    — Changes to existing functionality
### Deprecated — Features to be removed in future versions
### Removed    — Features removed in this version
### Fixed      — Bug fixes
### Security   — Security vulnerability patches
```

---

*Maintained by Aryan Kumar Upadhyay · [CodeXploit.in](https://codexploit.in)*
