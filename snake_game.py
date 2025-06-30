import sys
import pygame

from settings import Settings
from snake import Snake
from time import sleep

class SnakeGame:
    """A class for the games behavior and resources"""

    def __init__(self):
        """Initialize the games elements"""
        self.settings = Settings()

        # Initialize the screen 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")

        # Create the snake instance
        self.snake = Snake(self)

    def run_game(self):
        """The main loop of the game"""
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()

    def _check_events(self):
        """Check for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

    def _check_keydown_event(self, event):
        """Check the key presses"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.update_direction('r')
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.update_direction('l')
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake.update_direction('u')
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.update_direction('d')

    def _update_screen(self):
        """Update the screen each time the loops run"""

        self.screen.fill(self.settings.bgcolor)
        self.snake.draw_tail()

        # Update the screen with the new frame
        pygame.display.flip()

        # Pause between frames
        sleep(0.1)

if __name__ == "__main__":
    sg = SnakeGame()
    sg.run_game()
    