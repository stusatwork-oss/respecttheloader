# Contributing to RespectTheLoader

First off, thank you for considering contributing to RespectTheLoader! It's people like you who make this pattern useful for the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Contribution Workflow](#contribution-workflow)
- [Style Guidelines](#style-guidelines)
- [The Sacred Law](#the-sacred-law)

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots** if applicable

Use the bug report template when filing issues.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear title** describing the enhancement
- **Provide detailed description** of the proposed functionality
- **Explain why this enhancement would be useful**
- **List any alternative solutions** you've considered

### Pull Requests

We actively welcome your pull requests:

1. Fork the repo and create your branch from the main branch
2. If you've added code, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the style guidelines
6. Issue the pull request!

---

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- pip

### Setup Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR-USERNAME/respecttheloader.git
cd respecttheloader

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install development dependencies (optional)
pip install pytest pytest-cov black flake8 mypy isort

# 4. Create a branch for your changes
git checkout -b feature/your-feature-name

# 5. Make your changes in the /lab/ directory first!
mkdir -p lab/your-feature
cd lab/your-feature
# ... develop and test ...

# 6. When stable, promote to appropriate location
# (See "The Sacred Law" section below)
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tools --cov=. --cov-report=html

# Run specific test file
pytest tests/test_ai_bot.py
```

### Code Formatting

We use `black` for code formatting:

```bash
# Format all Python files
black .

# Check formatting without modifying
black --check .
```

### Linting

```bash
# Run flake8
flake8 *.py tools/

# Run mypy for type checking
mypy *.py tools/
```

---

## Contribution Workflow

### 1. Choose What to Contribute

Check our [BUILD_PLAN.md](BUILD_PLAN.md) for areas needing work:

- **Good first issues**: Labeled `good-first-issue`
- **Documentation**: Improvements to docs
- **Tools**: New utilities or enhancements
- **Tests**: Increased coverage
- **Features**: New functionality

### 2. Develop in /lab/

**IMPORTANT**: Follow the RespectTheLoader pattern:

```bash
# Start in the lab
cd lab/
mkdir my-contribution
cd my-contribution

# Develop freely here - it's gitignored!
# Test thoroughly before promoting
```

### 3. Promote When Ready

When your work is stable:

```bash
# For new tools
cp lab/my-contribution/tool.py tools/

# For documentation
cp lab/my-contribution/DOCS.md ./

# Never modify protected archives without explicit maintainer approval
```

### 4. Submit Pull Request

```bash
# Add your changes (NOT the /lab/ directory!)
git add tools/tool.py
git add docs/DOCS.md

# Commit with clear message
git commit -m "Add feature: Brief description

Detailed explanation of what this changes and why.

Fixes #123"

# Push to your fork
git push origin feature/your-feature-name

# Open pull request on GitHub
```

---

## Style Guidelines

### Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests liberally

Example:
```
Add manifest validator tool

- Validates shareware.yml schema
- Checks for duplicate version entries
- Ensures all paths exist

Fixes #42
```

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use type hints where possible
- Write docstrings for all public functions/classes

Example:
```python
def validate_manifest(manifest_path: str) -> bool:
    """
    Validate the shareware manifest file.

    Args:
        manifest_path: Path to the shareware.yml file

    Returns:
        True if valid, False otherwise

    Raises:
        FileNotFoundError: If manifest file doesn't exist
    """
    # Implementation
    pass
```

### Documentation Style

- Use Markdown for all documentation
- Include code examples where appropriate
- Keep line length reasonable (80-100 chars)
- Use proper heading hierarchy
- Link to related documents

---

## The Sacred Law

When contributing to RespectTheLoader, you must **Respect the Loader**:

### Protection Rules

1. **NEVER modify files marked `protected: true`** in shareware.yml
2. **ALWAYS develop in /lab/ first** before promoting to archive
3. **DO NOT commit /lab/ contents** (it's gitignored for a reason)
4. **READ THE_BOOK_OF_STULATIONS.md** to understand the philosophy

### What You Can Modify

✅ **Allowed**:
- Tools and utilities
- Documentation (non-archived)
- Tests
- Build scripts
- New features in /lab/
- Non-protected versions (where `protected: false`)

❌ **Forbidden** (without maintainer approval):
- Protected archive versions
- shareware.yml (structure changes)
- THE_BOOK_OF_STULATIONS.md (sacred text)
- Existing manifest entries

### When in Doubt

1. Ask in the issue or discussion
2. Develop in /lab/ and show your work
3. Wait for maintainer guidance
4. Respect the boundaries

---

## Recognition

Contributors will be:
- Listed in CHANGELOG.md for their contributions
- Credited in release notes
- Added to a CONTRIBUTORS.md file (coming soon)
- Acknowledged in commit messages

---

## Questions?

- **General questions**: Open a discussion on GitHub
- **Bug reports**: Use issue templates
- **Security concerns**: See [SECURITY.md](SECURITY.md)
- **Feature ideas**: Open an enhancement issue

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

*Thank you for helping us Respect the Loader!*

*The archive is eternal. The lab is your playground. Contribute wisely.*
