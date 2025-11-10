# Contributing to DevForge

Thank you for considering contributing to DevForge! 🔥

## Ways to Contribute

- **Add New Frameworks**: Create scaffolders for new frameworks
- **Improve Existing Scaffolders**: Enhance templates and structures
- **Fix Bugs**: Report and fix issues
- **Improve Documentation**: Make docs better
- **Write Tests**: Add test coverage

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/devforge.git
   cd devforge
   ```

3. Install in development mode:
   ```bash
   pipx install -e .
   ```

4. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Adding a New Framework

See [TUTORIAL.md](TUTORIAL.md) for a complete step-by-step guide.

Quick overview:
1. Create `devforge/scaffolders/yourframework.py`
2. Extend `FrameworkScaffolder` base class
3. Register in `devforge/scaffolders/__init__.py`
4. Add CLI option in `devforge/cli.py`
5. Test thoroughly
6. Submit PR

## Development Guidelines

### Code Style
- Use clear, descriptive variable names
- Add docstrings to all classes and methods
- Follow PEP 8 style guide
- Use type hints where appropriate

### Testing
- Test your scaffolder with actual framework CLI
- Verify all features are created correctly
- Test error handling (missing tools, etc.)
- Run: `python test_architecture.py`

### Documentation
- Update README.md if adding new features
- Add examples to TUTORIAL.md for new frameworks
- Include docstrings in your code

## Pull Request Process

1. Update documentation
2. Test your changes thoroughly
3. Update version in `setup.py` and `pyproject.toml` if needed
4. Submit PR with clear description
5. Wait for review

## Code Review

All submissions require review. We'll:
- Check code quality
- Verify tests pass
- Review documentation
- Test functionality

## Questions?

Open an issue or reach out to isakamtweve69@gmail.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
