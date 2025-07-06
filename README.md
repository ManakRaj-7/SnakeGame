# 🐍 Snake Game

A classic Snake game implementation in Python using the curses library for terminal-based gameplay.

![Snake Game](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey.svg)

## 🎮 Features

- **Classic Snake Gameplay**: Control a snake to eat food and grow longer
- **Terminal-Based Interface**: Clean, responsive terminal UI using curses
- **Score Tracking**: Real-time score display
- **Collision Detection**: Game ends when snake hits walls or itself
- **Cross-Platform**: Works on Windows, macOS, and Linux terminals
- **Simple Controls**: Arrow keys for movement, 'q' to quit

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- A terminal/command prompt that supports curses (most Unix-like systems)
- For Windows: Windows Terminal or WSL recommended

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Run the game**
   ```bash
   python snake_game.py
   ```

## 🎯 How to Play

### Controls
- **↑** Arrow Up: Move snake up
- **↓** Arrow Down: Move snake down
- **←** Arrow Left: Move snake left
- **→** Arrow Right: Move snake right
- **q** or **Q**: Quit game

### Game Rules
1. Control the snake using arrow keys
2. Eat the food (`*`) to grow and increase your score
3. Avoid hitting the walls or your own tail
4. Try to achieve the highest score possible!

### Game Elements
- **Snake Head**: `#` (the part you control)
- **Snake Body**: `#` (follows the head)
- **Food**: `*` (eat this to grow)
- **Walls**: Terminal boundaries (avoid these)

## 📁 Project Structure

```
snake-game/
├── snake_game.py      # Main game file
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── .gitignore        # Git ignore file
├── LICENSE           # MIT License
└── screenshots/      # Game screenshots (if any)
```

## 🛠️ Development

### Running the Game
```bash
python snake_game.py
```

### Requirements
The game uses only Python standard library modules:
- `curses` - Terminal UI library
- `random` - Random number generation
- `sys` - System-specific parameters

## 🐛 Troubleshooting

### Common Issues

**"Terminal window too small"**
- Resize your terminal window to at least 20x10 characters
- Use a larger terminal window or font size

**"curses not supported" (Windows)**
- Use Windows Terminal instead of Command Prompt
- Or use WSL (Windows Subsystem for Linux)
- Alternative: Use Git Bash or similar terminal emulator

**Game not responding to keys**
- Make sure your terminal supports arrow key input
- Try running in a different terminal emulator

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic Snake game
- Built with Python's curses library
- Thanks to the Python community for excellent documentation

## 📊 Game Statistics

- **Language**: Python 3.6+
- **Dependencies**: None (uses only standard library)
- **Lines of Code**: ~120
- **License**: MIT

---

**Enjoy playing! 🐍🎮**

If you like this project, please give it a ⭐ star on GitHub! 