import random
import curses
import sys

def main():
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Check if terminal is large enough
    if sh < 10 or sw < 20:
        curses.endwin()
        print("Terminal window too small. Please resize to at least 20x10.")
        sys.exit(1)
    
    # Create game window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)
    
    # Initialize snake in the center
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    
    # Initialize food
    food = [sh//2, sw//2]
    w.addch(int(food[0]), int(food[1]), '*')
    
    # Initialize direction
    key = curses.KEY_RIGHT
    score = 0
    
    # Game title and instructions
    w.addstr(0, 2, "SNAKE GAME - Score: 0")
    w.addstr(1, 2, "Use arrow keys to move, 'q' to quit")
    
    try:
        while True:
            # Get user input
            next_key = w.getch()
            
            # Handle quit
            if next_key == ord('q') or next_key == ord('Q'):
                break
                
            # Prevent reverse direction
            if next_key == curses.KEY_DOWN and key != curses.KEY_UP:
                key = next_key
            elif next_key == curses.KEY_UP and key != curses.KEY_DOWN:
                key = next_key
            elif next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
                key = next_key
            elif next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
                key = next_key
            
            # Check for collision with walls or self
            if (snake[0][0] in [0, sh-1] or 
                snake[0][1] in [0, sw-1] or 
                snake[0] in snake[1:]):
                break
            
            # Calculate new head position
            new_head = [snake[0][0], snake[0][1]]
            
            if key == curses.KEY_DOWN:
                new_head[0] += 1
            elif key == curses.KEY_UP:
                new_head[0] -= 1
            elif key == curses.KEY_LEFT:
                new_head[1] -= 1
            elif key == curses.KEY_RIGHT:
                new_head[1] += 1
            
            # Add new head
            snake.insert(0, new_head)
            
            # Check if food is eaten
            if snake[0] == food:
                score += 1
                w.addstr(0, 2, f"SNAKE GAME - Score: {score}")
                
                # Generate new food position
                food = None
                while food is None:
                    nf = [
                        random.randint(2, sh-3),
                        random.randint(2, sw-3)
                    ]
                    food = nf if nf not in snake else None
                w.addch(food[0], food[1], '*')
            else:
                # Remove tail
                tail = snake.pop()
                w.addch(int(tail[0]), int(tail[1]), ' ')
            
            # Draw snake head
            w.addch(int(snake[0][0]), int(snake[0][1]), '#')
            
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up
        curses.endwin()
        print(f"Game Over! Final Score: {score}")
        print("Thanks for playing!")

if __name__ == "__main__":
    main()

