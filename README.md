# 🕹️ RespectTheLoader

**A pattern for protecting golden builds from accidental modification**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

---

## What is This?

**RespectTheLoader** is a repository structure pattern that protects "golden builds" - canonical, versioned artifacts - from accidental modification by humans or AI agents. It provides:

- **Protected Archives**: Immutable versioned builds marked in a manifest
- **Safe Sandboxes**: Git-ignored experimental workspaces
- **Clear Governance**: Human-readable rules enforced by tools
- **Retro Interface**: Windows 95-inspired shareware launcher UI

This is both a **working demonstration** and a **template** you can adopt for your own projects.

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/stusatwork-oss/respecttheloader.git
cd respecttheloader

# Install dependencies
pip install -r requirements.txt

# Launch the retro shareware launcher
python launcher_gui.py
# or
./LAUNCH_GUI.sh
```

### First Run

The launcher presents a Windows 95-style interface with 500 "shareware programs". Programs 387-392 are the real GLITCHDEX MALL versions defined in `shareware.yml`.

Use mouse or keyboard:
- **Arrow keys**: Navigate
- **Enter**: Launch selected program
- **Mouse**: Click to select and launch
- **ESC**: Exit

---

## The Pattern

### Core Components

1. **`shareware.yml`** - Manifest defining canonical versions

```yaml
versions:
  - name: "GLITCHDEX MALL v387"
    path: "archive/v387-glitchdex-mall-alpha"
    protected: true
    # ... more metadata ...
```

2. **`/archive/`** - Protected golden builds (committed to git)

```
archive/
├── v387-glitchdex-mall-alpha/     # protected: true
├── v388-glitchdex-mall-beta/      # protected: true
└── v392-glitchdex-mall-current/   # protected: false (editable)
```

3. **`/lab/`** - Experimental workspace (.gitignored)

```
lab/
└── my-experiment/    # Safe sandbox for development
```

4. **Tools & Launchers** - Enforcement and UX

- `tools/ai_bot_03.py` - AI bot that respects protection rules
- `launcher_gui.py` - Retro shareware launcher interface

### Philosophy

The project uses a humorous "sacred law" framework (**THE_BOOK_OF_STULATIONS.md**) to communicate serious governance principles:

> *"Thou shalt not modify that which is marked `protected: true` in the manifest"*

This makes the rules memorable and the constraints clear to both humans and AI agents.

---

## Usage

### For Developers

**Experimenting with protected builds:**

```bash
# DON'T: Modify protected archives directly
cd archive/v387-glitchdex-mall-alpha
# ❌ This violates the sacred law!

# DO: Work in the lab
cd lab/
mkdir v387-experiment
# ✅ Safe experimentation
```

**Promoting lab work to archive:**

```bash
# 1. Finalize work in lab
cd lab/my-feature

# 2. Create new version
mkdir -p ../../archive/v393-new-feature
cp -r * ../../archive/v393-new-feature/

# 3. Update shareware.yml
# Add entry for v393 with protected: true

# 4. Commit archive only
git add archive/v393-new-feature shareware.yml
git commit -m "Archive v393: Add new feature"
```

### For AI Agents

The `tools/ai_bot_03.py` demonstrates how AI agents should interact:

```python
# Read the manifest
with open("shareware.yml") as f:
    manifest = yaml.safe_load(f)

# Check protection status
for version in manifest["versions"]:
    if version.get("protected"):
        # Redirect to lab for experiments
        workspace = "lab/"
    else:
        # Safe to modify
        workspace = version["path"]
```

Run the AI bot:

```bash
python tools/ai_bot_03.py
```

---

## Architecture

```
respecttheloader/
├── .gitignore                    # Excludes /lab/ and Python artifacts
├── .gitattributes               # Protection rules for sacred files
├── LICENSE                      # MIT License
├── README.md                    # This file
├── BUILD_PLAN.md               # Standardization roadmap
├── CONTRIBUTING.md             # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Community standards
├── SECURITY.md                 # Security policy
├── CHANGELOG.md                # Version history
├── requirements.txt            # Python dependencies
├── shareware.yml               # Manifest of protected versions
│
├── THE_BOOK_OF_STULATIONS.md   # Governance "sacred text"
├── LAUNCHER_README.md          # Detailed launcher docs
├── AI_BOT_03 – SYSTEM LOG.md   # AI self-governance log
├── 🜂 GEMINI_ORACLE_NODE...md   # Oracle response
│
├── launcher_gui.py             # Main GUI launcher
├── shareware_gen_v2.py         # Program list generator
├── LAUNCH_GUI.sh              # Launch script
│
├── archive/                    # Protected golden builds
│   ├── README.md
│   └── (version directories)
│
├── lab/                        # Experimental workspace (.gitignored)
│   └── README.md
│
└── tools/                      # Utility scripts
    └── ai_bot_03.py           # AI agent demonstrating compliance
```

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed design documentation.

---

## Documentation

- **[BUILD_PLAN.md](./BUILD_PLAN.md)** - Roadmap for standardization
- **[LAUNCHER_README.md](./LAUNCHER_README.md)** - Detailed launcher guide
- **[THE_BOOK_OF_STULATIONS.md](./THE_BOOK_OF_STULATIONS.md)** - Governance framework
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute
- **[SECURITY.md](./SECURITY.md)** - Security policy

---

## Why This Pattern?

### Problems It Solves

1. **Accidental Overwrites**: Protected builds can't be modified accidentally
2. **Version Drift**: Clear separation between stable and experimental
3. **AI Safety**: AI agents learn to respect boundaries
4. **Build Archaeology**: Old versions preserved exactly as they were
5. **Development Freedom**: Safe sandbox for experimentation

### Use Cases

- **Build Archives**: Preserve release candidates and stable versions
- **Configuration Management**: Protect production configs while testing
- **Data Pipelines**: Lock canonical datasets while iterating
- **Documentation**: Freeze versioned docs while drafting
- **AI Agent Safety**: Teach agents about boundaries

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

Key areas for contribution:
- Additional tools and integrations
- Multi-language support
- Web-based launcher
- Cloud storage adapters
- Testing and validation

---

## License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

---

## Acknowledgments

This project is a conceptual demonstration exploring:
- Human-AI collaboration boundaries
- Creative governance frameworks
- Retro computing aesthetics
- Software archaeology practices

Inspired by the shareware era of 1995-1998 and the need for clear artifact management in modern AI-assisted development.

---

## Status

This repository is under active standardization. See [BUILD_PLAN.md](./BUILD_PLAN.md) for progress.

**Current Version**: 0.9.0 (Pre-release)

---

*Respect the Loader. The archive is eternal. The lab is chaos.*
