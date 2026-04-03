# Contributing to Retriever

Thank you for your interest in contributing to **Retriever — Campus Lost & Found**! 🎉

Every contribution — bug fixes, new features, documentation improvements, or feedback — is warmly welcomed. This guide will help you get started.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Branch Naming](#branch-naming)
- [Commit Messages](#commit-messages)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Style Guide](#style-guide)

---

## 🤝 Code of Conduct

By participating in this project, you agree to uphold a respectful and inclusive environment. Be kind, constructive, and professional in all interactions.

---

## 🛠️ How to Contribute

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/retriever.git
   cd retriever
   ```
3. **Set up** the development environment (see below).
4. **Create a branch** for your change.
5. **Make your changes**, write tests if applicable, and ensure everything works.
6. **Push** to your fork and **open a Pull Request**.

---

## 🧪 Development Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python app.py
```

The app will be available at `http://localhost:5000`.

---

## 🌿 Branch Naming

Use clear, lowercase, hyphenated branch names:

| Type | Format | Example |
|---|---|---|
| Feature | `feature/short-description` | `feature/email-verification` |
| Bug Fix | `fix/short-description` | `fix/image-upload-crash` |
| Documentation | `docs/short-description` | `docs/api-reference` |
| Refactor | `refactor/short-description` | `refactor/db-helpers` |
| Hotfix | `hotfix/short-description` | `hotfix/session-key` |

---

## 💬 Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<optional scope>): <short summary>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```
feat(auth): add email verification on registration
fix(upload): handle non-RGB images before thumbnail resize
docs(readme): add API reference table
chore(deps): bump Pillow to 11.1.0
```

- Use present tense ("add feature" not "added feature")
- Keep the summary under 72 characters
- Reference issues where relevant: `Closes #42`

---

## 📬 Pull Request Guidelines

- PRs should be **focused** — one feature or fix per PR.
- Include a clear **description** of what changed and why.
- Link to the related issue if applicable.
- Screenshots or a short demo GIF are appreciated for UI changes.
- Ensure your branch is **up to date** with `main` before opening the PR:
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```
- All CI checks (if configured) must pass before review.

---

## 🐛 Reporting Bugs

Before filing a bug report, please check if the issue already exists.

When opening a new bug, include:

- **Environment** — OS, Python version, browser
- **Steps to reproduce** — as detailed as possible
- **Expected behaviour** — what should have happened
- **Actual behaviour** — what actually happened
- **Screenshots or error logs** — if applicable

Use the [Bug Report issue template](.github/ISSUE_TEMPLATE/bug_report.md) (if present).

---

## 💡 Suggesting Features

Feature requests are welcome! Please open an issue with:

- A clear **title** and **description** of the feature
- Why it would be **valuable** to campus users
- Any proposed **implementation approach** (optional)

---

## 🎨 Style Guide

### Python

- Follow [PEP 8](https://pep8.org/) conventions.
- Use 4-space indentation.
- Functions and variables: `snake_case`. Classes: `PascalCase`.
- Keep route functions focused — extract complex logic to helpers.
- Always close database connections (`db.close()`) or use a context manager.

### HTML / CSS

- Use semantic HTML5 elements (`<main>`, `<section>`, `<article>`, etc.).
- Follow the existing **white + red vintage editorial** design language.
- Typography hierarchy: Cormorant Garamond (display) → Syne (UI headings) → DM Mono (labels/mono).
- Mobile-first: write base styles for small screens, then use `min-width` media queries.
- No CSS frameworks — keep it pure CSS3.

### JavaScript

- Vanilla JS only — no jQuery, no bundlers.
- Use `const` and `let`; avoid `var`.
- Descriptive function names; comment non-obvious logic.

---

## 🙏 Thank You

Every contributor makes Retriever better for students everywhere. Your effort matters.

*— Aryan Kumar Upadhyay, CodeXploit.in*
