<p align="center">
  <img alt="Build Status" src="https://img.shields.io/github/actions/workflow/status/rfc391/SentinelOps/ci.yml?branch=main">
  <img alt="License" src="https://img.shields.io/github/license/rfc391/SentinelOps">
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-blue">
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macOS-lightgrey">
</p>


# 🛰️ SentinelOps

**SentinelOps** is a cross-platform tactical security framework designed for cyber defense, surveillance, and automated intelligence operations. It’s built to run efficiently on servers, laptops, and field systems across Linux, Windows, and macOS.

---

## 🚀 Features

- 🔐 Encrypted communication & secure module handling
- 🧠 AI-powered analytics and log correlation
- 📡 Surveillance modules with optional GUI overlay
- ⚙️ Real-time metrics and threat detection (Prometheus/Grafana/Suricata)
- 🌐 Web-based dashboard (Cloudflare Zero Trust ready)
- 📦 Built-in support for `.deb`, `.exe`, and `.AppImage` packages
- 🛡️ Hardened deployment for military-grade scenarios

---

## 🖥️ Cross-Platform Support

| OS          | Installer       | Status       |
|-------------|------------------|--------------|
| Ubuntu/Debian | `.deb`            | ✅ Supported |
| Windows 10+  | `.exe` (via PyInstaller) | ✅ Supported |
| Linux (universal) | `.AppImage`    | ✅ Supported |
| macOS        | Homebrew (planned) | 🚧 WIP      |

---

## 🧭 Quick Start

```bash
# Linux/WSL/macOS
git clone https://github.com/rfc391/SentinelOps.git
cd SentinelOps
pip install -r requirements.txt
python3 src/main.py
```

```powershell
# Windows
git clone https://github.com/rfc391/SentinelOps.git
cd SentinelOps
pip install -r requirements.txt
python src/main.py
```

---

## 📂 Folder Structure

- `src/` – All core modules and application logic
- `docs/` – User and developer documentation
- `installers/` – Dockerfile, packaging, and OS-specific build scripts
- `tests/` – Unit and integration tests
- `templates/` – Web GUI files (HTML, CSS)
- `scripts/` – Automation scripts for deployment and backups

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/
```

---

## 🔄 CI/CD

- ✅ GitHub Actions for automated testing, linting, and packaging
- ✅ CodeQL for security scanning
- ✅ DockerHub or GHCR support (planned)

---

## 📦 Build Installers

```bash
# Build .deb package
./scripts/build_deb.sh

# Build .AppImage
./scripts/build_appimage.sh

# Build Windows .exe
pyinstaller --onefile src/main.py
```

---

## 🤝 Contributing

Please see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for how to get started.

---

## 📜 License

MIT License © [rfc391](https://github.com/rfc391)

---

## 🛰️ Live Demo

![demo](https://user-images.githubusercontent.com/demo-placeholder.gif)

---
