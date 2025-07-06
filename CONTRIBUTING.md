# Contributing to Snake Game

Thank you for your interest in contributing to the Snake Game project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When creating a bug report, please include:

- A clear and descriptive title
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Your operating system and Python version
- Any error messages or screenshots

### Suggesting Enhancements

We welcome feature requests! When suggesting enhancements, please:

- Use a clear and descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- Include mockups or examples if applicable

### Code Contributions

#### Development Setup

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature/fix
4. Make your changes
5. Test your changes thoroughly
6. Commit your changes with clear commit messages
7. Push to your fork and submit a pull request

#### Code Style Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Write docstrings for functions and classes

#### Testing

Before submitting a pull request, please:

- Test the game on different terminal sizes
- Verify all controls work correctly
- Check that collision detection works properly
- Ensure the game handles edge cases gracefully

### Pull Request Process

1. Update the README.md if needed
2. Update the requirements.txt if you add dependencies
3. Ensure your code follows the project's style guidelines
4. Add tests if applicable
5. Update documentation if needed
6. The maintainers will review your PR and provide feedback

## 🏗️ Project Structure

```
snake-game/
├── snake_game.py      # Main game logic
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT License
├── CONTRIBUTING.md   # This file
└── screenshots/      # Game screenshots
```

## 🐛 Common Issues and Solutions

### Windows Compatibility

The game uses the `curses` library which may not work in all Windows terminals. Solutions:

- Use Windows Terminal
- Use WSL (Windows Subsystem for Linux)
- Use Git Bash or similar terminal emulator

### Terminal Size Issues

If you get "Terminal window too small" error:

- Resize your terminal window
- Use a larger font size
- Check your terminal's minimum size requirements

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor" not "Moves cursor")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Examples:
```
Add high score tracking feature

- Implement score persistence
- Add high score display
- Update README with new features

Fixes #123
```

## 🎯 Areas for Contribution

We welcome contributions in these areas:

- **Game Features**: New gameplay mechanics, power-ups, levels
- **UI Improvements**: Better visual design, colors, animations
- **Performance**: Code optimization, better algorithms
- **Documentation**: Better README, code comments, tutorials
- **Testing**: Unit tests, integration tests
- **Platform Support**: Better cross-platform compatibility

## 📞 Getting Help

If you need help with contributing:

1. Check the existing issues and pull requests
2. Read the README.md for setup instructions
3. Open a new issue for questions or problems
4. Join our community discussions

## 🙏 Recognition

Contributors will be recognized in:

- The project README
- Release notes
- GitHub contributors page

Thank you for contributing to make Snake Game better! 🐍🎮 