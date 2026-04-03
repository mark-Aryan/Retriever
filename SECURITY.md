# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| Latest (`main`) | ✅ Yes |
| Older branches | ❌ No |

---

## 🔐 Reporting a Vulnerability

The security of Retriever and its users is a top priority. If you have discovered a security vulnerability, please **do not** open a public GitHub issue. Public disclosure before a fix is available puts all users at risk.

### How to Report

Please report vulnerabilities via email:

**📧 security@codexploit.in** *(or your preferred contact)*

Include in your report:

- A clear description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Any suggested fix (optional but appreciated)

### What to Expect

- **Acknowledgement** within **48 hours**
- An initial assessment and severity rating within **5 business days**
- A fix or mitigation plan communicated within **14 days** for high/critical issues
- Credit in the release notes if you wish (we respect anonymity requests)

---

## 🛡️ Security Considerations for Self-Hosting

If you are deploying Retriever on your own infrastructure, please be aware of the following:

### 1. Set a Fixed Secret Key
```python
# In production, use an environment variable — never the default:
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-only-for-dev')
```
The default `os.urandom(24).hex()` generates a new key on every restart, invalidating all user sessions.

### 2. Restrict Debug Mode
Never run `app.run(debug=True)` in production. Use a production WSGI server (Gunicorn, uWSGI) instead.

### 3. File Upload Safety
Uploaded files are stored under `static/uploads/`. Ensure your web server is configured to **not execute** files in this directory.

### 4. HTTPS
Always serve over HTTPS in production. Use a reverse proxy (Nginx, Caddy) with a valid TLS certificate.

### 5. Database
The SQLite database file (`lostfound.db`) should not be web-accessible. Ensure it is outside the `static/` directory or blocked by your server config.

### 6. Rate Limiting
The current version does not include rate limiting on login or reach-out endpoints. For production deployments, configure rate limiting at the reverse proxy level or integrate Flask-Limiter.

---

## 📋 Known Limitations (Non-Security)

- No email verification on registration (planned in roadmap)
- No CAPTCHA on reach-out form (planned)
- Session tokens not invalidated server-side on logout (Flask default behaviour with cookie-based sessions)

---

*Last updated: 2025 · Aryan Kumar Upadhyay · CodeXploit.in*
