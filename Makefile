.PHONY: help install test lint format clean serve build docs

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "🎴 MEMOGEN - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

install: ## Install dependencies
	@echo "📦 Installing dependencies..."
	pip install hatch
	hatch env create
	pre-commit install
	@echo "✅ Installation complete!"

test: ## Run tests
	@echo "🧪 Running tests..."
	hatch run test

test-cov: ## Run tests with coverage
	@echo "🧪 Running tests with coverage..."
	hatch run test-cov

test-watch: ## Run tests in watch mode
	@echo "👀 Running tests in watch mode..."
	hatch run ptw

lint: ## Run linting checks
	@echo "🔍 Running linting..."
	hatch run lint:check

format: ## Format code
	@echo "🎨 Formatting code..."
	hatch run lint:format

type-check: ## Run type checking
	@echo "🔤 Running type checks..."
	hatch run mypy src tests

clean: ## Clean build artifacts
	@echo "🧹 Cleaning..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Clean complete!"

serve: ## Start development server
	@echo "🚀 Starting development server..."
	@echo "🌐 Access at: http://localhost:8000"
	hatch run memogen --serve

build: ## Build package
	@echo "📦 Building package..."
	hatch build
	@echo "✅ Build complete! Check dist/ directory"

docs: ## Open coverage report
	@echo "📊 Opening coverage report..."
	hatch run cov-report

pre-commit: ## Run pre-commit hooks
	@echo "🔧 Running pre-commit hooks..."
	pre-commit run --all-files

update: ## Update dependencies
	@echo "⬆️ Updating dependencies..."
	hatch env prune
	hatch env create
	pre-commit autoupdate

check-all: lint type-check test ## Run all checks
	@echo "✅ All checks passed!"

ci: ## Simulate CI pipeline locally
	@echo "🔄 Running CI pipeline..."
	@$(MAKE) lint
	@$(MAKE) type-check
	@$(MAKE) test-cov
	@echo "✅ CI pipeline passed!"
