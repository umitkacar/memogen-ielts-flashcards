# Contributing to MEMO-IMAGEN

First off, thank you for considering contributing to MEMO-IMAGEN! 🎉

It's people like you that make MEMO-IMAGEN such a great tool for learning with AI.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Node.js 20+ and npm
- Python 3.11+ (for AI/ML components)
- Git
- Expo CLI (`npm install -g expo-cli`)

### Fork & Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
```bash
git clone https://github.com/YOUR_USERNAME/MEMO-IMAGEN.git
cd MEMO-IMAGEN
```

3. Add the upstream repository:
```bash
git remote add upstream https://github.com/umitkacar/MEMO-IMAGEN.git
```

4. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

## 🤝 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details** (OS, Node version, etc.)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the proposed feature**
- **Explain why this enhancement would be useful**
- **List examples of how the feature would be used**

### 🔧 Code Contributions

#### Types of Contributions We're Looking For:

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance improvements
- 🧪 Test coverage improvements
- 🌐 Translations

## 💻 Development Setup

### Installation

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.example .env

# Edit .env with your API keys
# Add your OpenAI, Anthropic, AWS, etc. keys

# Start development server
npm start
```

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

### Building

```bash
# Build for production
npm run build

# Build iOS (requires macOS)
npm run ios

# Build Android
npm run android
```

## 🔄 Pull Request Process

### Before Submitting

1. **Ensure your code follows our style guidelines**
2. **Update documentation** if you're changing functionality
3. **Add tests** for new features
4. **Ensure all tests pass**
5. **Update the README.md** if needed
6. **Keep commits clean and descriptive**

### Submitting a Pull Request

1. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

2. **Create a Pull Request** from your fork to our `main` branch

3. **Fill out the PR template** with:
   - Description of changes
   - Related issue numbers
   - Screenshots (for UI changes)
   - Testing steps

4. **Wait for review** - maintainers will review your PR and may request changes

5. **Address feedback** - make requested changes and push updates

6. **Celebrate!** 🎉 Once approved, your PR will be merged

### PR Title Format

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

- `feat: add user authentication`
- `fix: resolve memory leak in image generation`
- `docs: update installation instructions`
- `style: format code with prettier`
- `refactor: simplify API client logic`
- `test: add unit tests for AI service`
- `chore: update dependencies`

## 🎨 Style Guidelines

### JavaScript/TypeScript

We use ESLint and Prettier for code formatting:

```bash
# Lint code
npm run lint

# Fix linting issues
npm run lint:fix

# Format code
npm run format
```

**Key conventions:**
- Use TypeScript for type safety
- Use functional components with hooks
- Follow React best practices
- Write meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

### Commit Messages

- Use the imperative mood ("Add feature" not "Added feature")
- Limit the first line to 72 characters
- Reference issues and pull requests after the first line
- Use conventional commit format

**Example:**
```
feat: add image generation with Stable Diffusion

- Integrate SDXL model
- Add prompt engineering utilities
- Create UI for image generation

Closes #123
```

### File Naming

- React components: `PascalCase.tsx`
- Utilities: `camelCase.ts`
- Constants: `UPPER_SNAKE_CASE.ts`
- Types/Interfaces: `PascalCase.types.ts`

### Documentation

- Document all public APIs
- Use JSDoc comments for functions
- Update README for user-facing changes
- Add inline comments for complex logic

## 🧪 Testing Guidelines

### Writing Tests

- Write unit tests for utilities and services
- Write integration tests for features
- Write E2E tests for critical user flows
- Aim for >80% code coverage
- Mock external dependencies (APIs, databases)

### Test Structure

```typescript
describe('FeatureName', () => {
  describe('methodName', () => {
    it('should do something specific', () => {
      // Arrange
      const input = setupTestData();

      // Act
      const result = methodName(input);

      // Assert
      expect(result).toBe(expected);
    });
  });
});
```

## 🌐 Translation Contributions

We welcome translations! To add a new language:

1. Create a new file: `src/i18n/locales/[language-code].json`
2. Translate all keys from `en.json`
3. Add the language to `src/i18n/config.ts`
4. Test the translation in the app
5. Submit a PR

## 💬 Community

### Getting Help

- 💬 [GitHub Discussions](https://github.com/umitkacar/MEMO-IMAGEN/discussions) - for questions and discussions
- 🐛 [GitHub Issues](https://github.com/umitkacar/MEMO-IMAGEN/issues) - for bugs and feature requests
- 📧 Email - contact the maintainers

### Recognition

Contributors will be:
- Added to the Contributors section in README
- Mentioned in release notes
- Granted contributor badge on GitHub

## 📚 Resources

- [React Native Documentation](https://reactnative.dev/docs/getting-started)
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)
- [Stable Diffusion Guide](https://huggingface.co/docs/diffusers)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to MEMO-IMAGEN!** 🚀💙

Your efforts help make AI-powered education accessible to everyone!
