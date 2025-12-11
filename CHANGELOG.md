# Changelog

All notable changes to RespectTheLoader will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned (Post-1.0)
- Web-based launcher interface
- Docker image for portable execution
- Multi-language support examples
- Rich `shareware-init` flow with templates
- Sample protected builds in /archive/
- Higher test coverage (>70%)

---

## [1.0.0] - 2025-12-11

### Added - First Stable Release

**Test Suite (22 tests)**
- `tests/test_ai_bot_03.py` - 8 unit tests for protection enforcement logic
  - Protected version detection
  - Mutation prevention validation
  - Default behavior for missing fields
  - Lab redirection for protected builds
- `tests/test_manifest.py` - 13 integration tests for manifest validation
  - Structure verification (versions key, paths, protection fields)
  - Archive directory existence checks
  - Protection consistency validation
  - Placeholder documentation requirements

**CLI Tooling**
- `shareware_init.py` - MVP CLI stub for initializing new repos
  - Creates `/archive/` and `/lab/` directory structure
  - Generates starter `shareware.yml` manifest
  - Updates `.gitignore` for lab exclusion
  - Provides next-steps guidance

**Version Tracking**
- `VERSION` file - Centralized version string (1.0.0)
- `tools/__init__.py` - Package init with `__version__`

**CI/CD Enhancements**
- Added `black --check` to GitHub Actions workflow
- Full lint + format + test pipeline: flake8 → black → pytest

### Changed
- `BUILD_PLAN.md` restructured:
  - Added repo status header
  - Updated to Phase 4-5 (Code Quality & Automation)
  - Added v1.0.0 Release Checklist
  - Reorganized remaining work into post-1.0 epics
- `README.md` - Added reference implementation callout

### Fixed
- Removed unused imports across codebase (subprocess, tempfile, pytest)
- Fixed bare `except` clause in `launcher_gui.py` (now catches `curses.error`)
- Fixed line length violations (E501) across all Python files
- Removed unused variable `programs` in `shareware_gen_v2.py`
- Applied consistent black formatting to all Python files

### Security
- CI workflow runs with read-only permissions
- Explicit permissions block in GitHub Actions

---

## [0.9.0] - 2025-11-27

### Added - Repository Standardization

**Core Infrastructure**
- `LICENSE` - MIT License for open source distribution
- `.gitignore` - Python artifacts and /lab/ directory exclusion
- `requirements.txt` - Python dependency management (PyYAML)
- `requirements-dev.txt` - Development dependencies (pytest, black, flake8, isort)
- `BUILD_PLAN.md` - Comprehensive standardization roadmap
- `.flake8` - Linting configuration (88 char max, black-compatible)
- `.pre-commit-config.yaml` - Pre-commit hooks configuration

**Community Health Files**
- `CODE_OF_CONDUCT.md` - Contributor Covenant 2.1
- `CONTRIBUTING.md` - Detailed contribution guidelines
- `SECURITY.md` - Security policy and vulnerability reporting
- `CHANGELOG.md` - This file

**Documentation**
- Expanded `README.md` with:
  - Installation instructions
  - Quick start guide
  - Architecture overview
  - Usage examples for developers and AI agents
  - Complete project documentation links
- `archive/README.md` - Protected builds directory documentation
- `lab/README.md` - Experimental workspace guidelines

**Directory Structure**
- Created `/archive/` directory for protected canonical builds
- Created `/lab/` directory for experimental workspace (gitignored)
- Both directories include comprehensive README files

**GitHub Infrastructure**
- `.github/workflows/ci.yml` - Multi-version Python test matrix (3.8-3.11)
- `.github/workflows/greetings.yml` - Welcome automation
- `.github/workflows/release.yml` - Release automation
- `.github/ISSUE_TEMPLATE/` - Bug, feature, and documentation templates
- `.github/PULL_REQUEST_TEMPLATE.md` - PR guidelines

**Testing**
- `tests/test_smoke.py` - Basic smoke test for pytest infrastructure

### Changed
- README.md transformed from minimal demo description to comprehensive project documentation
- Repository now follows standard open source project structure

### Improved
- Clear separation between protected and experimental spaces
- Comprehensive onboarding documentation for new contributors
- Professional presentation suitable for public standard adoption

---

## [0.1.0] - 2025-11-26

### Added - Initial Concept

**Core Demonstration**
- `shareware.yml` - Manifest defining 6 protected versions (v387-v392)
- `launcher_gui.py` - Windows 95-inspired retro launcher interface
- `shareware_gen_v2.py` - Generates 500 shareware program names
- `LAUNCH_GUI.sh` - Shell script to launch GUI
- `tools/ai_bot_03.py` - AI bot demonstrating governance compliance

**Governance Framework**
- `THE_BOOK_OF_STULATIONS.md` - Creative "sacred law" governance document
- `AI_BOT_03 – SYSTEM LOG.md` - AI self-governance demonstration log
- `🜂 GEMINI_ORACLE_NODE – COSMIC SYSTEM MESSAGE.md` - Oracle validation response

**Documentation**
- `README.md` - Basic project description
- `LAUNCHER_README.md` - Comprehensive launcher documentation
- `.gitattributes` - Git configuration with thematic commentary

**Features**
- Protection pattern for golden builds
- Curses-based TUI with mouse support
- 16-color VGA palette aesthetic
- Keyboard and mouse navigation
- 500 synthetic shareware programs with 6 real versions

---

## Version History Summary

| Version | Date | Milestone |
|---------|------|-----------|
| **1.0.0** | 2025-12-11 | First stable release - tests, tooling, CI |
| **0.9.0** | 2025-11-27 | Repository standardization |
| **0.1.0** | 2025-11-26 | Initial concept demonstration |

---

## Semantic Versioning

This project follows [SemVer](https://semver.org/):

- **MAJOR** (1.x.x): Breaking changes to manifest format or protection semantics
- **MINOR** (x.1.x): New features, tools, or backward-compatible additions
- **PATCH** (x.x.1): Bug fixes, documentation updates, minor improvements

---

## Links

- **Repository**: https://github.com/stusatwork-oss/respecttheloader
- **Issue Tracker**: https://github.com/stusatwork-oss/respecttheloader/issues
- **Releases**: https://github.com/stusatwork-oss/respecttheloader/releases

---

*Respect the Loader. Track the Changes. Know the History.*
