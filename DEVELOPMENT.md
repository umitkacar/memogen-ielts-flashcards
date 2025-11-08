# 🛠️ MEMOGEN Development Guide

Complete guide for contributing to MEMOGEN with modern Python tooling.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Git Workflow](#git-workflow)
- [Release Process](#release-process)

---

## 🎯 Prerequisites

### Required Tools

```bash
# Python 3.11 or higher
python --version  # Should be >= 3.11

# pip (comes with Python)
pip --version

# Git
git --version
```

### Recommended Tools

- **Hatch**: Modern Python project manager
- **Pre-commit**: Git hook framework
- **VS Code** or **PyCharm** with Python extensions

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/umitkacar/MEMOGEN.git
cd MEMOGEN
```

### 2. Install Hatch

```bash
# Using pip
pip install hatch

# Or using pipx (recommended)
pipx install hatch
```

### 3. Set Up Development Environment

```bash
# Install all development dependencies
hatch env create

# Activate the environment
hatch shell

# Install pre-commit hooks
pre-commit install
```

### 4. Verify Installation

```bash
# Run tests
hatch run test

# Check code quality
hatch run lint:check

# Start development server
hatch run memogen --serve
```

---

## 🔄 Development Workflow

### Project Structure

```
MEMOGEN/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD
├── src/
│   └── memogen/            # Main Python package
│       ├── __init__.py
│       ├── cli.py          # Command-line interface
│       ├── server.py       # Web server
│       └── models.py       # Pydantic data models
├── tests/                  # Test suite
│   ├── conftest.py        # Pytest fixtures
│   ├── test_models.py
│   └── test_cli.py
├── index.html              # Main flashcard app
├── pyproject.toml          # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md
```

### Common Tasks

#### Run the Web Server

```bash
# Using hatch
hatch run memogen --serve

# Or directly with Python
python -m memogen.cli --serve --port 8000

# Or simple HTTP server
python -m http.server 8000
```

#### Run Tests

```bash
# All tests
hatch run test

# With coverage
hatch run test-cov

# Specific test file
hatch run pytest tests/test_models.py

# Specific test
hatch run pytest tests/test_models.py::TestVocabularyCard::test_create_valid_card

# Watch mode (requires pytest-watch)
hatch run ptw
```

#### Code Quality Checks

```bash
# Run all checks
hatch run lint:all

# Individual checks
hatch run ruff check .          # Linting
hatch run black --check .       # Formatting check
hatch run mypy src tests        # Type checking

# Auto-fix issues
hatch run lint:format           # Format code
hatch run ruff check --fix .    # Fix linting issues
```

---

## 🧪 Testing

### Writing Tests

Tests are located in the `tests/` directory and use **pytest**.

**Example test:**

```python
def test_vocabulary_card_creation(sample_easy_card):
    """Test creating a vocabulary card."""
    assert sample_easy_card.word == "ABUNDANT"
    assert sample_easy_card.level == DifficultyLevel.EASY
```

### Test Coverage

```bash
# Generate coverage report
hatch run test-cov

# View HTML report
hatch run cov-report
# Opens browser at http://localhost:8000
```

### Test Markers

```bash
# Run only unit tests
hatch run pytest -m unit

# Run only integration tests
hatch run pytest -m integration

# Skip slow tests
hatch run pytest -m "not slow"
```

---

## ✨ Code Quality

### Tools Used

| Tool | Purpose | Configuration |
|------|---------|--------------|
| **Ruff** | Linting & formatting | `pyproject.toml` |
| **Black** | Code formatting | `pyproject.toml` |
| **isort** | Import sorting | `pyproject.toml` |
| **mypy** | Static type checking | `pyproject.toml` |
| **pytest** | Testing framework | `pyproject.toml` |
| **bandit** | Security checking | `pyproject.toml` |

### Pre-commit Hooks

Pre-commit hooks run automatically before each commit:

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate

# Skip hooks (not recommended)
git commit --no-verify
```

### Code Style Guidelines

**Python:**
- Line length: 100 characters
- Use type hints for all functions
- Follow Google docstring style
- Use Pydantic for data validation
- Prefer f-strings over .format()

**Example:**

```python
def process_card(card: VocabularyCard) -> dict[str, str]:
    """Process a vocabulary card.

    Args:
        card: The vocabulary card to process

    Returns:
        Processed card data as dictionary

    Raises:
        ValueError: If card is invalid
    """
    if not card.word:
        raise ValueError("Card must have a word")

    return {
        "word": card.word.upper(),
        "level": card.level.value,
    }
```

---

## 🌳 Git Workflow

### Branch Strategy

```bash
# Create feature branch
git checkout -b feature/add-new-vocabulary

# Create fix branch
git checkout -b fix/correct-pronunciation

# Create docs branch
git checkout -b docs/update-readme
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new IELTS vocabulary deck
fix: correct pronunciation for "ephemeral"
docs: update installation instructions
style: format code with black
refactor: simplify card filtering logic
test: add tests for difficulty levels
chore: update dependencies
```

### Pull Request Process

1. **Create branch** from `main`
2. **Make changes** and commit
3. **Push** to your fork
4. **Open PR** with description
5. **Pass CI checks** (linting, tests, type checking)
6. **Get review** from maintainers
7. **Merge** when approved

---

## 📦 Building & Packaging

### Build Package

```bash
# Build distribution packages
hatch build

# Output: dist/memogen-1.0.0.tar.gz
#         dist/memogen-1.0.0-py3-none-any.whl
```

### Install Locally

```bash
# Install in development mode
pip install -e .

# Install from built package
pip install dist/memogen-1.0.0-py3-none-any.whl
```

---

## 🚀 Release Process

### Version Bumping

Edit `src/memogen/__init__.py`:

```python
__version__ = "1.1.0"  # Update version
```

### Create Release

```bash
# 1. Update version
# 2. Update CHANGELOG.md
# 3. Commit changes
git commit -m "chore: bump version to 1.1.0"

# 4. Create tag
git tag -a v1.1.0 -m "Release v1.1.0"

# 5. Push with tags
git push origin main --tags

# 6. Build and publish (when ready)
hatch build
hatch publish
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Pre-commit hooks failing
```bash
# Update hooks
pre-commit autoupdate

# Clear cache
pre-commit clean
```

**Issue**: Tests failing
```bash
# Clear pytest cache
rm -rf .pytest_cache

# Reinstall dependencies
hatch env prune
hatch env create
```

**Issue**: Type errors with mypy
```bash
# Clear mypy cache
rm -rf .mypy_cache

# Run with verbose output
hatch run mypy --verbose src
```

---

## 📚 Resources

### Documentation
- [Hatch Documentation](https://hatch.pypa.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pre-commit Documentation](https://pre-commit.com/)

### Project Links
- [GitHub Repository](https://github.com/umitkacar/MEMOGEN)
- [Live Demo](https://umitkacar.github.io/MEMOGEN/)
- [Issue Tracker](https://github.com/umitkacar/MEMOGEN/issues)

---

## 🤝 Getting Help

- 💬 [GitHub Discussions](https://github.com/umitkacar/MEMOGEN/discussions)
- 🐛 [Report Issues](https://github.com/umitkacar/MEMOGEN/issues)
- 📧 Email: contact@memogen.com

---

**Happy Coding! 🎉**
