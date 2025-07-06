#!/usr/bin/env python3
"""
Installation script for Snake Game
Helps users install and set up the game.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def print_banner():
    """Print the game banner."""
    print("=" * 50)
    print("🐍 SNAKE GAME INSTALLER 🐍")
    print("=" * 50)
    print()

def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ Error: Python 3.6 or higher is required!")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True

def check_dependencies():
    """Check if required dependencies are available."""
    print("\nChecking dependencies...")
    
    # Check curses module
    try:
        import curses
        print("✅ curses module is available")
    except ImportError:
        print("❌ Warning: curses module not available")
        print("   This may cause issues on Windows systems")
        print("   Consider using Windows Terminal or WSL")
        return False
    
    # Check other standard library modules
    required_modules = ['random', 'sys']
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} module is available")
        except ImportError:
            print(f"❌ Error: {module} module not available")
            return False
    
    return True

def install_game():
    """Install the game files."""
    print("\nInstalling Snake Game...")
    
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    
    # Check if snake_game.py exists
    game_file = current_dir / "snake_game.py"
    if not game_file.exists():
        print("❌ Error: snake_game.py not found!")
        return False
    
    # Create installation directory
    install_dir = Path.home() / ".snake_game"
    install_dir.mkdir(exist_ok=True)
    
    # Copy game files
    files_to_copy = [
        "snake_game.py",
        "config.py",
        "README.md",
        "LICENSE"
    ]
    
    for file_name in files_to_copy:
        source = current_dir / file_name
        if source.exists():
            destination = install_dir / file_name
            shutil.copy2(source, destination)
            print(f"✅ Copied {file_name}")
        else:
            print(f"⚠️  Warning: {file_name} not found, skipping")
    
    # Create launcher script
    launcher_content = f'''#!/usr/bin/env python3
"""
Snake Game Launcher
Automatically generated launcher script.
"""

import sys
import os

# Add the game directory to Python path
game_dir = r"{install_dir}"
sys.path.insert(0, game_dir)

# Import and run the game
try:
    import snake_game
    snake_game.main()
except ImportError as e:
    print(f"Error importing snake_game: {{e}}")
    print(f"Game directory: {{game_dir}}")
    sys.exit(1)
except Exception as e:
    print(f"Error running game: {{e}}")
    sys.exit(1)
'''
    
    launcher_file = install_dir / "run_snake_game.py"
    with open(launcher_file, 'w') as f:
        f.write(launcher_content)
    
    # Make launcher executable (Unix-like systems)
    try:
        os.chmod(launcher_file, 0o755)
    except:
        pass  # Windows doesn't support chmod
    
    print(f"✅ Created launcher script: {launcher_file}")
    
    return True

def create_desktop_shortcut():
    """Create desktop shortcut (if possible)."""
    print("\nCreating desktop shortcut...")
    
    desktop_dir = Path.home() / "Desktop"
    if not desktop_dir.exists():
        print("⚠️  Desktop directory not found, skipping shortcut creation")
        return
    
    # Create shortcut content
    shortcut_content = f'''[Desktop Entry]
Version=1.0
Type=Application
Name=Snake Game
Comment=A classic Snake game implementation in Python
Exec=python "{Path.home() / '.snake_game' / 'run_snake_game.py'}"
Icon=terminal
Terminal=true
Categories=Game;Arcade;
'''
    
    shortcut_file = desktop_dir / "snake-game.desktop"
    try:
        with open(shortcut_file, 'w') as f:
            f.write(shortcut_content)
        os.chmod(shortcut_file, 0o755)
        print(f"✅ Created desktop shortcut: {shortcut_file}")
    except Exception as e:
        print(f"⚠️  Could not create desktop shortcut: {e}")

def test_installation():
    """Test the installation by running the game briefly."""
    print("\nTesting installation...")
    
    try:
        # Import the game module
        game_dir = Path.home() / ".snake_game"
        sys.path.insert(0, str(game_dir))
        
        import snake_game
        print("✅ Game module imported successfully")
        
        # Note: We can't actually run the game here because it requires a terminal
        # and would block the installation process
        print("✅ Installation test completed")
        return True
        
    except Exception as e:
        print(f"❌ Installation test failed: {e}")
        return False

def print_usage_instructions():
    """Print usage instructions."""
    print("\n" + "=" * 50)
    print("🎮 INSTALLATION COMPLETE! 🎮")
    print("=" * 50)
    print()
    print("To play the game, you can:")
    print()
    print("1. Run from the installation directory:")
    print(f"   python {Path.home() / '.snake_game' / 'run_snake_game.py'}")
    print()
    print("2. Run directly from current directory:")
    print("   python snake_game.py")
    print()
    print("3. Use the desktop shortcut (if created)")
    print()
    print("Game Controls:")
    print("  ↑↓←→ Arrow keys: Move snake")
    print("  q or Q: Quit game")
    print()
    print("Requirements:")
    print("  - Terminal window at least 20x10 characters")
    print("  - Python 3.6 or higher")
    print("  - curses support (most Unix-like systems)")
    print()
    print("For Windows users:")
    print("  - Use Windows Terminal for best compatibility")
    print("  - Or use WSL (Windows Subsystem for Linux)")
    print("  - Or use Git Bash")
    print()
    print("Enjoy playing! 🐍")

def main():
    """Main installation function."""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠️  Some dependencies are missing, but installation will continue...")
    
    # Install the game
    if not install_game():
        print("\n❌ Installation failed!")
        sys.exit(1)
    
    # Create desktop shortcut (optional)
    try:
        create_desktop_shortcut()
    except Exception as e:
        print(f"⚠️  Could not create desktop shortcut: {e}")
    
    # Test installation
    if not test_installation():
        print("\n⚠️  Installation test failed, but files were copied")
    
    # Print usage instructions
    print_usage_instructions()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during installation: {e}")
        sys.exit(1) 