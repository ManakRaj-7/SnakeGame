#!/usr/bin/env python3
"""
Configuration file for Snake Game
Contains all game settings and constants.
"""

# Game Settings
GAME_TITLE = "SNAKE GAME"
GAME_INSTRUCTIONS = "Use arrow keys to move, 'q' to quit"
GAME_OVER_MESSAGE = "Game Over! Final Score: {}"
THANKS_MESSAGE = "Thanks for playing!"

# Terminal Requirements
MIN_TERMINAL_HEIGHT = 10
MIN_TERMINAL_WIDTH = 20
TERMINAL_TOO_SMALL_MESSAGE = "Terminal window too small. Please resize to at least {}x{}."

# Game Elements
SNAKE_HEAD_CHAR = '#'
SNAKE_BODY_CHAR = '#'
FOOD_CHAR = '*'
EMPTY_CHAR = ' '

# Game Speed
GAME_SPEED_MS = 100  # Milliseconds between game updates

# Controls
QUIT_KEYS = ['q', 'Q']
ARROW_KEYS = {
    'UP': 'KEY_UP',
    'DOWN': 'KEY_DOWN', 
    'LEFT': 'KEY_LEFT',
    'RIGHT': 'KEY_RIGHT'
}

# Scoring
SCORE_INCREMENT = 1
SCORE_DISPLAY_FORMAT = "SNAKE GAME - Score: {}"

# Snake Initial Settings
INITIAL_SNAKE_LENGTH = 3
SNAKE_START_X_RATIO = 4  # Start at 1/4 of screen width
SNAKE_START_Y_RATIO = 2  # Start at 1/2 of screen height

# Food Settings
FOOD_MARGIN = 2  # Minimum distance from walls

# Colors (if supported)
try:
    import curses
    # Color pairs for different game elements
    COLOR_PAIRS = {
        'snake': 1,
        'food': 2,
        'score': 3,
        'border': 4
    }
except ImportError:
    COLOR_PAIRS = {}

# Game States
GAME_STATES = {
    'RUNNING': 'running',
    'PAUSED': 'paused',
    'GAME_OVER': 'game_over',
    'QUIT': 'quit'
}

# Difficulty Levels (future feature)
DIFFICULTY_LEVELS = {
    'EASY': {'speed': 150, 'food_value': 1},
    'NORMAL': {'speed': 100, 'food_value': 1},
    'HARD': {'speed': 75, 'food_value': 2},
    'EXPERT': {'speed': 50, 'food_value': 3}
}

# Default difficulty
DEFAULT_DIFFICULTY = 'NORMAL'

# High Score Settings (future feature)
HIGH_SCORE_FILE = 'high_scores.txt'
MAX_HIGH_SCORES = 10

# Sound Settings (future feature)
SOUND_ENABLED = False
SOUND_EFFECTS = {
    'eat_food': 'eat.wav',
    'game_over': 'game_over.wav',
    'level_up': 'level_up.wav'
}

# Debug Settings
DEBUG_MODE = False
DEBUG_INFO = {
    'show_fps': False,
    'show_coordinates': False,
    'show_collision_boxes': False
}

# Version Information
GAME_VERSION = "1.0.0"
GAME_AUTHOR = "Snake Game Developer"
GAME_DESCRIPTION = "A classic Snake game implementation in Python using curses" 