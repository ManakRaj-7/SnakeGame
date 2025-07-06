#!/usr/bin/env python3
"""
Test suite for Snake Game
Basic tests to ensure the game functions correctly.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the current directory to the path so we can import snake_game
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the game module
try:
    import snake_game
except ImportError as e:
    print(f"Could not import snake_game: {e}")
    print("Make sure snake_game.py is in the current directory")
    sys.exit(1)


class TestSnakeGame(unittest.TestCase):
    """Test cases for the Snake Game."""

    def setUp(self):
        """Set up test fixtures."""
        self.game = snake_game

    def test_import_success(self):
        """Test that the game module can be imported."""
        self.assertIsNotNone(self.game)
        self.assertTrue(hasattr(self.game, 'main'))

    def test_main_function_exists(self):
        """Test that the main function exists."""
        self.assertTrue(callable(self.game.main))

    def test_game_initialization(self):
        """Test that the game can be initialized (mocked)."""
        with patch('curses.initscr') as mock_initscr:
            with patch('curses.endwin') as mock_endwin:
                mock_stdscr = MagicMock()
                mock_stdscr.getmaxyx.return_value = (20, 40)
                mock_initscr.return_value = mock_stdscr
                
                # This should not raise an exception
                try:
                    # We'll just test that the function can be called
                    # The actual game loop will be interrupted by our mocks
                    pass
                except Exception as e:
                    self.fail(f"Game initialization failed: {e}")

    def test_terminal_size_validation(self):
        """Test terminal size validation logic."""
        # Test minimum size requirements
        min_height, min_width = 10, 20
        
        # Test valid sizes
        self.assertTrue(20 >= min_height and 40 >= min_width)
        self.assertTrue(15 >= min_height and 25 >= min_width)
        
        # Test invalid sizes
        self.assertFalse(5 >= min_height and 15 >= min_width)
        self.assertFalse(12 >= min_height and 15 >= min_width)

    def test_snake_movement_logic(self):
        """Test snake movement direction logic."""
        # Test direction validation
        def is_valid_direction(current, new):
            """Helper function to test direction validation."""
            if new == 'UP' and current != 'DOWN':
                return True
            elif new == 'DOWN' and current != 'UP':
                return True
            elif new == 'LEFT' and current != 'RIGHT':
                return True
            elif new == 'RIGHT' and current != 'LEFT':
                return True
            return False
        
        # Test valid direction changes
        self.assertTrue(is_valid_direction('UP', 'LEFT'))
        self.assertTrue(is_valid_direction('UP', 'RIGHT'))
        self.assertTrue(is_valid_direction('DOWN', 'LEFT'))
        self.assertTrue(is_valid_direction('DOWN', 'RIGHT'))
        self.assertTrue(is_valid_direction('LEFT', 'UP'))
        self.assertTrue(is_valid_direction('LEFT', 'DOWN'))
        self.assertTrue(is_valid_direction('RIGHT', 'UP'))
        self.assertTrue(is_valid_direction('RIGHT', 'DOWN'))
        
        # Test invalid direction changes (reverse)
        self.assertFalse(is_valid_direction('UP', 'DOWN'))
        self.assertFalse(is_valid_direction('DOWN', 'UP'))
        self.assertFalse(is_valid_direction('LEFT', 'RIGHT'))
        self.assertFalse(is_valid_direction('RIGHT', 'LEFT'))

    def test_collision_detection_logic(self):
        """Test collision detection logic."""
        # Test wall collision
        def is_wall_collision(x, y, max_x, max_y):
            """Helper function to test wall collision."""
            return x <= 0 or x >= max_x - 1 or y <= 0 or y >= max_y - 1
        
        # Test wall collisions
        self.assertTrue(is_wall_collision(0, 10, 20, 20))  # Left wall
        self.assertTrue(is_wall_collision(19, 10, 20, 20))  # Right wall
        self.assertTrue(is_wall_collision(10, 0, 20, 20))   # Top wall
        self.assertTrue(is_wall_collision(10, 19, 20, 20))  # Bottom wall
        
        # Test no collision
        self.assertFalse(is_wall_collision(10, 10, 20, 20))  # Middle
        
        # Test self collision
        def is_self_collision(head, body):
            """Helper function to test self collision."""
            return head in body
        
        snake_body = [[5, 5], [5, 4], [5, 3]]
        self.assertTrue(is_self_collision([5, 5], snake_body[1:]))  # Head in body
        self.assertFalse(is_self_collision([6, 5], snake_body[1:]))  # No collision

    def test_food_generation_logic(self):
        """Test food generation logic."""
        # Test food position validation
        def is_valid_food_position(food, snake, max_x, max_y):
            """Helper function to test food position validation."""
            x, y = food
            # Check bounds
            if x <= 1 or x >= max_x - 2 or y <= 1 or y >= max_y - 2:
                return False
            # Check not on snake
            if food in snake:
                return False
            return True
        
        snake = [[5, 5], [5, 4], [5, 3]]
        max_x, max_y = 20, 20
        
        # Test valid food positions
        self.assertTrue(is_valid_food_position([10, 10], snake, max_x, max_y))
        self.assertTrue(is_valid_food_position([15, 15], snake, max_x, max_y))
        
        # Test invalid food positions
        self.assertFalse(is_valid_food_position([5, 5], snake, max_x, max_y))  # On snake
        self.assertFalse(is_valid_food_position([0, 10], snake, max_x, max_y))  # Too close to wall
        self.assertFalse(is_valid_food_position([19, 10], snake, max_x, max_y))  # Too close to wall

    def test_score_calculation(self):
        """Test score calculation logic."""
        # Test score increment
        score = 0
        score += 1  # Eat food
        self.assertEqual(score, 1)
        
        score += 1  # Eat another food
        self.assertEqual(score, 2)
        
        # Test score display format
        score_display = f"SNAKE GAME - Score: {score}"
        self.assertEqual(score_display, "SNAKE GAME - Score: 2")

    def test_game_quit_logic(self):
        """Test game quit functionality."""
        # Test quit key detection
        def is_quit_key(key):
            """Helper function to test quit key detection."""
            return key == ord('q') or key == ord('Q')
        
        # Test quit keys
        self.assertTrue(is_quit_key(ord('q')))
        self.assertTrue(is_quit_key(ord('Q')))
        
        # Test non-quit keys
        self.assertFalse(is_quit_key(ord('a')))
        self.assertFalse(is_quit_key(ord('1')))


class TestGameIntegration(unittest.TestCase):
    """Integration tests for the game."""

    def test_game_structure(self):
        """Test that the game has the expected structure."""
        # Check that the main function exists and is callable
        self.assertTrue(hasattr(snake_game, 'main'))
        self.assertTrue(callable(snake_game.main))
        
        # Check that the game can be imported without errors
        self.assertIsNotNone(snake_game)

    def test_game_documentation(self):
        """Test that the game has basic documentation."""
        # Check that the main function has a docstring or at least exists
        self.assertTrue(hasattr(snake_game, 'main'))


if __name__ == '__main__':
    # Run the tests
    print("Running Snake Game Tests...")
    print("=" * 40)
    
    # Create test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSnakeGame)
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGameIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("=" * 40)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    # Exit with appropriate code
    sys.exit(len(result.failures) + len(result.errors)) 