# ⚡ Richmack Workspace

<div align="center">

```text
 ____  ___ ____ _   _ __  __    _    ____ _  __
|  _ \|_ _/ ___| | | |  \/  |  / \  / ___| |/ /
| |_) || | |   | |_| | |\/| | / _ \| |   | ' /
|  _ < | | |___|  _  | |  | |/ ___ \ |___| . \
|_| \_\___\____|_| |_|_|  |_/_/   \_\____|_|\_\

                 W O R K S P A C E
```

### 🖥️ One terminal. Multiple applications. One workspace.

**Richmack Workspace** is a keyboard-first terminal application launcher and package manager for the Richmack PyPI software ecosystem.

Install, update, manage, and launch independent Richmack applications from one Textual interface.

</div>

---

## 📖 Overview

Richmack Workspace provides a central terminal interface for the growing collection of Richmack applications distributed through PyPI.

Instead of remembering multiple package names, installation commands, executable names, and environments, Workspace provides a single command:

```bash
richmack
```

From there, applications can be selected and managed directly from the TUI.

The goal is simple:

```text
                    ⚡ RICHMACK WORKSPACE
                              │
             ┌────────────────┼────────────────┐
             │                │                │
         Discovery       Management        Launcher
             │                │                │
             └────────────────┼────────────────┘
                              │
                  Independent PyPI Apps
                              │
       ┌──────────┬───────────┼───────────┬──────────┐
       │          │           │           │          │
      🪄         🧠          🍯          ⚙️         📜
     Wize      Language      Pot        Exerx      Hebrew
    Wizard      Ninja      of Mannah     Eye        Study
                              │
                             ♟️
                           JinnLab
```

Each program remains an independent application.

Workspace does **not** merge the programs into one large Python package. Instead, it acts as the terminal front door to the ecosystem.

---

# ✨ Features

Richmack Workspace currently provides:

- 🖥️ Native Textual terminal interface
- ⌨️ Keyboard-first navigation
- 📦 PyPI application installation
- 🔄 Application updates
- 🚀 Application launching
- 🗑️ Application removal
- 🧱 Isolated Python virtual environments
- 🔍 Automatic console entry-point detection
- 📊 Installed-version detection
- 🗃️ SQLite activity history
- 📝 Per-application package-management logs
- 🎨 Richmack ASCII branding
- 🧭 Persistent keyboard instructions
- 🛡️ Dependency isolation between applications
- 🔌 Modular application catalog
- 🍎 macOS support
- 🐧 Linux support

---

# 🧰 Applications

Richmack Workspace currently manages six applications.

## 🪄 Wize Wizard

**PyPI package**

```text
wize-wizard
```

Wize Wizard is a strategy, planning, estimation, and project-thinking environment.

It combines structured strategic reasoning with project analysis tools while keeping each major function modular.

Core areas include:

- 🧭 Strategy development
- ❓ Structured Why analysis
- 🎯 Want, Wish, and Dream reasoning
- 🧮 PERT estimation
- 📊 Stress and uncertainty analysis
- 📈 Charts and project visualization
- 💬 Communications planning
- ✅ Desires and task management
- 📓 Journaling
- 📤 Export tools
- 🎓 Course and learning components

Wize Wizard's structured strategy system uses statements such as:

```text
As a __________,

I need to ______________________________

so that I can __________________________

because _______________________________.
```

The same structured format can be applied through multiple levels of reasoning.

Wize Wizard is designed to move from:

```text
Idea
  ↓
Need
  ↓
Purpose
  ↓
Deeper Why
  ↓
Strategy
  ↓
Estimate
  ↓
Execution
```

---

## 🧠 Language Ninja

**PyPI package**

```text
language-ninja
```

Language Ninja is a terminal language-analysis and training environment.

It is designed around working with language interactively rather than treating language analysis as a collection of disconnected command-line scripts.

Areas include:

- 📝 Text analysis
- 🧠 NLP workflows
- 💭 Sentiment analysis
- 📚 Language training
- 🔎 Text inspection
- 🗒️ Notes
- 📤 Data export
- ⌨️ Keyboard-first terminal interaction

Language Ninja gives language-oriented workflows their own dedicated TUI while remaining accessible directly through Richmack Workspace.

---

## 🍯 Pot of Mannah

**PyPI package**

```text
pot-of-mannah
```

Pot of Mannah is a terminal-based nutrition and training intelligence application.

It provides a dedicated environment for working with food, nutrition, exercise, and related personal training information.

The application is designed around the same philosophy as the rest of the Richmack ecosystem:

```text
Data
  ↓
Organization
  ↓
Analysis
  ↓
Useful terminal interface
```

Pot of Mannah remains an independent package while Richmack Workspace handles its installation and launch environment.

---

## ⚙️ ExerxEye

**PyPI package**

```text
ExerxEye
```

ExerxEye is an exercise and workout intelligence TUI.

Its focus is organizing physical training into a terminal workflow that can support exercise selection, workout construction, tracking, and analysis.

Areas include:

- 🏋️ Exercise management
- 🔁 Repetition-based workouts
- 🎲 Workout generation
- 📋 Workout construction
- 📈 Progress analysis
- 💾 Saved workout data
- ⌨️ Fast keyboard navigation

Exercise categories can include movements such as:

```text
Push-ups
Pull-ups
Squats
Burpees
Jumping jacks
Mountain climbers
```

ExerxEye gives the Richmack ecosystem a dedicated physical-training application without coupling its dependencies to the other tools.

---

## 📜 Hebrew Fuzzy Study

**PyPI package**

```text
hebrew-fuzzy-study
```

Hebrew Fuzzy Study is a Hebrew lexical search, Tanakh reading, and study workstation.

It combines fuzzy searching with a terminal-oriented study environment.

Major capabilities include:

- 🔤 Hebrew lexical searching
- 🔎 Fuzzy matching
- 📖 Tanakh reading
- 🧠 Study workflows
- 📝 Annotation
- 📚 Scholar/reference tools
- 💾 Local study data
- ⌨️ Keyboard-first navigation

The project is designed to make Hebrew text exploration practical from the terminal.

Rather than requiring an exact spelling for every lookup, fuzzy-search functionality can assist with finding relevant lexical material when the search input is incomplete or approximate.

---

## ♟️ JinnLab

**PyPI package**

```text
jinnlab
```

JinnLab is a game-theory laboratory for exploring strategic interaction from the terminal.

It provides an environment for running and studying computational game-theory experiments.

Areas include:

- ♟️ Game-theory strategy analysis
- 🤝 Cooperation and defection
- ⚔️ Axelrod-style matches
- 🧬 Moran processes
- 🏆 Strategy tournaments
- 📊 Results analysis
- 🔬 Experimental strategy comparison

JinnLab can be used to examine how different strategies behave across repeated interactions and changing populations.

Conceptually:

```text
Strategy A
     │
     ▼
Repeated Interaction
     ▲
     │
Strategy B

     ↓

Scores
Survival
Cooperation
Defection
Population change
```

This makes JinnLab the experimental strategy laboratory within Richmack Workspace.

---

# 🏗️ Architecture

Richmack Workspace deliberately uses an isolated application architecture.

```text
Richmack Workspace
        │
        ├── Textual UI
        │
        ├── Application Catalog
        │
        ├── Package Manager
        │
        ├── Launcher
        │
        ├── SQLite Activity Database
        │
        └── Application Environments
                │
                ├── wize-wizard/
                │      └── .venv/
                │
                ├── language-ninja/
                │      └── .venv/
                │
                ├── pot-of-mannah/
                │      └── .venv/
                │
                ├── exerxeye/
                │      └── .venv/
                │
                ├── hebrew-fuzzy-study/
                │      └── .venv/
                │
                └── jinnlab/
                       └── .venv/
```

## 🧱 Why isolated environments?

Installing every application into the same Python environment creates dependency risk.

For example:

```text
Application A
    └── requires library==1.x

Application B
    └── requires library==2.x
```

A shared environment can eventually create conflicts.

Richmack Workspace instead gives each managed application its own environment:

```text
Workspace
   │
   ├── App A → Environment A
   ├── App B → Environment B
   └── App C → Environment C
```

This allows individual Richmack projects to evolve independently.

---

# 📦 Installation

## Install from PyPI

Once the package is available from PyPI:

```bash
python3 -m pip install richmack-workspace
```

Then launch:

```bash
richmack
```

The alternate executable is:

```bash
richmack-workspace
```

---

# 🍎 Development Installation on macOS

Clone the repository:

```bash
git clone git@github.com:iamrichmack111/richmack-workspace.git
```

Enter it:

```bash
cd richmack-workspace
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install Workspace:

```bash
python -m pip install -e .
```

Launch:

```bash
richmack
```

---

# 🐧 Development Installation on Linux

Clone:

```bash
git clone git@github.com:iamrichmack111/richmack-workspace.git
cd richmack-workspace
```

Install:

```bash
chmod +x install.sh
./install.sh
```

Activate:

```bash
source .venv/bin/activate
```

Launch:

```bash
richmack
```

---

# ⌨️ Keyboard Controls

Richmack Workspace is designed to be usable primarily from the keyboard.

| Key | Action |
|---|---|
| `↑` | Move selection up |
| `↓` | Move selection down |
| `ENTER` | Launch selected application |
| `G` | Get/install selected application |
| `U` | Update selected application |
| `X` | Remove selected application |
| `R` | Refresh Workspace |
| `Q` | Quit |

The controls are also displayed directly inside the Workspace interface.

---

# 📥 Installing an Application

Select an application:

```text
🪄 Wize Wizard
🧠 Language Ninja
🍯 Pot of Mannah
⚙️ ExerxEye
📜 Hebrew Fuzzy Study
♟️ JinnLab
```

Press:

```text
G
```

Workspace then performs the package-management workflow:

```text
Selected Application
        ↓
Create Application Directory
        ↓
Create Isolated .venv
        ↓
Upgrade pip
        ↓
Install Package from PyPI
        ↓
Inspect Package Metadata
        ↓
Detect Console Entry Point
        ↓
Record Installation
        ↓
Ready to Launch
```

---

# 🚀 Launching Applications

Highlight an installed application and press:

```text
ENTER
```

Workspace temporarily suspends its own Textual interface.

The selected application then receives control of the terminal.

```text
Richmack Workspace
        │
        │ ENTER
        ▼
   Selected TUI
        │
        │ Quit application
        ▼
Richmack Workspace
```

When the child application exits, control returns to Workspace.

---

# 🔄 Updating Applications

Highlight an installed application and press:

```text
U
```

Workspace runs the equivalent package upgrade inside that application's isolated environment.

Package-manager output is intentionally **not printed directly over the TUI**.

Instead:

```text
Update requested
      ↓
Background worker
      ↓
pip upgrade
      ↓
Log file
      ↓
Refresh application status
```

This prevents pip output from corrupting the Textual screen.

---

# 📝 Logs

Installation and update output is stored in per-application log files.

Conceptually:

```text
logs/
├── wize-wizard.log
├── language-ninja.log
├── pot-of-mannah.log
├── exerxeye.log
├── hebrew-fuzzy-study.log
└── jinnlab.log
```

If an installation or update fails, Workspace reports the corresponding log location.

This keeps the interface clean while preserving debugging information.

---

# 🗃️ Activity Database

Workspace uses SQLite to maintain local activity history.

Events can include:

```text
INSTALL
UPDATE
LAUNCH
UNINSTALL
```

Example:

```text
2026-07-26 14:22   wize-wizard          launch
2026-07-26 13:51   jinnlab              update
2026-07-26 11:03   hebrew-fuzzy-study   launch
2026-07-26 09:44   language-ninja       install
```

The activity database gives Workspace the foundation for future statistics such as:

- 📊 Most-used application
- 🚀 Total launches
- 🕐 Recent applications
- 📅 Usage by day
- 🔄 Update history
- 📦 Installation history

---

# 🔍 Automatic Entry-Point Detection

Workspace does not need to assume that every PyPI package uses the same executable name as its package.

After installation, Workspace examines Python package metadata and searches for:

```text
console_scripts
```

For example:

```text
PyPI Package
    ↓
hebrew-fuzzy-study
    ↓
Package Metadata
    ↓
console_scripts
    ↓
Detected executable
```

This makes the launcher more flexible as the Richmack package ecosystem grows.

---

# 🗂️ Project Structure

```text
richmack-workspace/
│
├── .github/
│   └── workflows/
│       └── publish.yml
│
├── richmack_workspace/
│   ├── __init__.py
│   ├── app.py
│   ├── catalog.py
│   ├── db.py
│   ├── manager.py
│   └── paths.py
│
├── tests/
│   └── test_catalog.py
│
├── .gitignore
├── install.sh
├── pyproject.toml
└── README.md
```

### `app.py`

The main Textual application.

Handles:

- UI composition
- navigation
- keyboard bindings
- application details
- install/update workers
- launching
- notifications

### `catalog.py`

Defines applications available through Workspace.

Each catalog entry contains information such as:

```python
WorkspaceApp(
    name="JinnLab",
    package="jinnlab",
    emoji="♟️",
    description="Game theory laboratory",
    slug="jinnlab",
)
```

### `manager.py`

Handles application lifecycle operations:

```text
Install
Update
Inspect
Launch
Remove
```

### `db.py`

Handles SQLite activity records.

### `paths.py`

Determines platform-appropriate locations for Workspace data, applications, logs, and databases.

---

# 🧪 Testing

Install pytest:

```bash
python -m pip install pytest
```

Run tests:

```bash
pytest -q
```

The test suite can be expanded as Workspace develops to cover:

- Catalog integrity
- Package detection
- Environment creation
- Entry-point discovery
- Database operations
- Application lifecycle behavior

---

# 📦 Building the Python Package

Install the build system:

```bash
python -m pip install --upgrade build
```

Clean old builds:

```bash
rm -rf dist build *.egg-info
```

Build:

```bash
python -m build
```

Expected output:

```text
dist/
├── richmack_workspace-X.Y.Z-py3-none-any.whl
└── richmack_workspace-X.Y.Z.tar.gz
```

---

# 🔁 CI/CD

Richmack Workspace uses GitHub Actions for package publishing.

The intended release pipeline is:

```text
Development
     ↓
Git Commit
     ↓
Push main
     ↓
Version Tag
     ↓
GitHub Release
     ↓
GitHub Actions
     ↓
Build Wheel + Source Distribution
     ↓
PyPI Trusted Publishing
     ↓
richmack-workspace on PyPI
```

This allows releases to be driven by versioned Git tags instead of manually uploading package files.

---

# 🏷️ Release Workflow

Example version:

```text
v0.1.3
```

Create the tag:

```bash
git tag -a v0.1.3 -m "Richmack Workspace v0.1.3"
```

Push it:

```bash
git push origin v0.1.3
```

Create the GitHub release:

```bash
gh release create v0.1.3 \
  --title "Richmack Workspace v0.1.3" \
  --notes "Richmack Workspace release."
```

The publishing workflow can then build and publish the corresponding Python distribution.

---

# 🛣️ Roadmap

## 🔹 Current Foundation

- ✅ Textual launcher
- ✅ PyPI package installation
- ✅ Independent virtual environments
- ✅ Application updating
- ✅ Application removal
- ✅ Console-entrypoint detection
- ✅ SQLite activity history
- ✅ Background package-management operations
- ✅ Package logs
- ✅ Richmack ASCII interface

## 🔹 Application Management

Planned improvements include:

- 🔄 Update All
- 🟢 Update-available indicators
- 🔍 Application search
- ⭐ Favorites
- 🩺 Environment health checks
- 🔧 Repair environment
- 📦 Installed-only view
- 🆕 Available-app view
- 📊 Version comparison

## 🔹 Workspace Intelligence

Future Workspace releases can add:

- 📈 Launch statistics
- 🕐 Recently used applications
- 📊 Usage reports
- 🔔 Update notifications
- 💾 Shared configuration
- 🧭 Application categories
- 🔗 Cross-application navigation

## 🔹 Richmack Project Layer

A future shared project layer could allow applications to work on common project resources while remaining independently packaged.

```text
                Richmack Project
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   Wize Wizard     JinnLab      Other Tools
        │             │             │
        └─────────────┼─────────────┘
                      │
               Shared Project Data
```

## 🔹 Long-Term Direction

Richmack Workspace is designed as a foundation for a larger terminal computing environment.

```text
Individual TUIs
       ↓
PyPI Applications
       ↓
Richmack Workspace
       ↓
Shared Services
       ↓
Terminal Application Platform
       ↓
Richmack OS
```

The long-term objective is a small, modular, terminal-oriented environment where applications can remain independently developed while sharing a common launcher and workspace architecture.

---

# 🧩 Design Philosophy

Richmack Workspace follows several principles.

### 🧱 Modular

Every major program remains independently installable.

### ⌨️ Keyboard First

Core operations should not require a mouse.

### 🖥️ Terminal Native

The terminal is treated as the primary interface rather than a fallback interface.

### 🔒 Isolated

Applications should not unnecessarily share dependency environments.

### 🔌 Extensible

Adding another Richmack application should require minimal modification to Workspace.

### 📦 Distributable

Applications can be independently versioned and distributed through PyPI.

### 🧠 Integrated Without Being Monolithic

Workspace creates a common environment without forcing every project into one codebase.

---

# ➕ Adding Another Richmack Application

New applications can be registered in the Workspace catalog.

Conceptually:

```python
WorkspaceApp(
    name="New Richmack App",
    package="new-richmack-app",
    emoji="🔷",
    description="Description of the application.",
    slug="new-richmack-app",
)
```

Workspace can then manage the package using the same lifecycle:

```text
Discover
   ↓
Install
   ↓
Detect
   ↓
Launch
   ↓
Update
   ↓
Remove
```

This means the Workspace architecture can grow with the application ecosystem.

---

# 🖥️ Richmack Terminal Ecosystem

Richmack Workspace represents the management layer connecting independent terminal projects.

```text
                      USER
                       │
                       ▼
              ⚡ RICHMACK WORKSPACE
                       │
       ┌───────────────┼────────────────┐
       │               │                │
   PRODUCTIVITY     LEARNING        ANALYSIS
       │               │                │
       ▼               ▼                ▼
  🪄 Wize Wizard   📜 Hebrew Study   ♟️ JinnLab
                       │
                 🧠 Language Ninja
                       │
                HEALTH / TRAINING
                       │
                 ┌─────┴─────┐
                 ▼           ▼
             🍯 Mannah     ⚙️ ExerxEye
```

---

# 👨‍💻 Author

**Jeremy Franklin**

GitHub:

```text
iamrichmack111
```

Richmack Workspace is part of the broader Richmack terminal software ecosystem.

---

# 📄 License

See the repository license for the terms governing this project.

---

<div align="center">

## ⚡ RICHMACK WORKSPACE

### Build tools independently. Operate them together.

```text
Install → Select → Launch → Work → Return
```

🪄 🧠 🍯 ⚙️ 📜 ♟️

</div>
