# ⚡ Richmack Workspace

**Richmack Workspace** is a keyboard-first Textual launcher and package manager for the Richmack terminal application ecosystem.

## 🚀 Current application catalog

- 🧙 **Wize Wizard** — `wize-wizard`
- 🥷 **Language Ninja** — `language-ninja`
- 🍯 **Pot of Mannah** — `pot-of-mannah`
- 💪 **ExerxEye** — `ExerxEye`
- 📜 **Hebrew Fuzzy Study** — `hebrew-fuzzy-study`
- 🧞 **JinnLab** — `jinnlab`

Each managed application is installed in its **own isolated virtual environment**, so dependencies from one Richmack application do not break another.

## 🧠 Architecture

```text
Richmack Workspace
        │
        ├── App Catalog
        │
        ├── SQLite Activity Registry
        │
        └── Managed Application Environments
                │
                ├── wize-wizard/.venv
                ├── language-ninja/.venv
                ├── pot-of-mannah/.venv
                ├── exerxeye/.venv
                ├── hebrew-fuzzy-study/.venv
                └── jinnlab/.venv
```

Managed data is stored under the platform-specific user data directory. On macOS this is typically under:

```text
~/Library/Application Support/richmack-workspace/
```

## 🛠️ Development install

```bash
cd richmack-workspace
chmod +x install.sh
./install.sh
source .venv/bin/activate
richmack
```

Or:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
richmack
```

## ⌨️ Keyboard controls

| Key | Action |
|---|---|
| `↑` / `↓` | Select an application |
| `Enter` | Launch selected application |
| `G` | Get/install |
| `U` | Update |
| `X` | Remove |
| `R` | Refresh |
| `Q` | Quit |

## 📦 How installation works

When you select an application and press `G`, Workspace:

1. Creates an isolated virtual environment.
2. Upgrades pip inside that environment.
3. Installs the selected package from PyPI.
4. Reads the installed package metadata.
5. Detects the package's `console_scripts` entry point.
6. Records the operation in SQLite.

When you press `Enter`, Workspace suspends its own Textual interface and gives the terminal to the selected child TUI. When the child program exits, you return to Richmack Workspace.

## 🧪 Test

```bash
python -m pip install pytest
pytest -q
```

## 📦 Build

```bash
python -m pip install build
python -m build
```

Expected output:

```text
dist/
├── richmack_workspace-0.1.0-py3-none-any.whl
└── richmack_workspace-0.1.0.tar.gz
```

## 🌐 Future roadmap

### v0.2
- PyPI latest-version lookup
- Update-available indicator
- Update All
- Installed-only view
- Launch counters

### v0.3
- Application search
- Favorites
- Shared Richmack theme/config
- Health checks
- Broken-environment repair

### v1.0
- Richmack account/workspace profile
- Shared project registry
- Cross-application file handoff
- Richmack Workspace plugin manifest
- Optional remote package catalog

---

**Richmack Workspace** is intended to become the terminal front door for the wider Richmack software ecosystem.


## ✨ v0.1.1 interface improvements

- Added large **RICHMACK WORKSPACE** ASCII branding.
- Added an always-visible keyboard instruction strip.
- Increased application-menu row height and spacing.
- Replaced human-character emojis with more neutral symbols.
- Package installation and update output is now redirected to per-app log files instead of being printed over the Textual display.
- Package-manager failures show the log location in the TUI.

Logs are stored in the Workspace data directory under:

```text
logs/<application>.log
```
