import sys
import pygame

from time import sleep
from settings import Settings
from snake import Snake
from fruit import Fruit
from game_stats import GameStats
from scoreboard import ScoreBoard
class SnakeGame:
    """A class for the games behavior and resources"""

    def __init__(self):
        """Initialize the games elements"""
        pygame.init()
        self.settings = Settings()

        # Initialize the screen 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")

        # Create the stats and scoreboard intance
        self.stats = GameStats()
        self.sb = ScoreBoard(self)

        # Create the snake instance
        self.snake = Snake(self)

        # Create the fruit instance
        self.fruit = Fruit(self)

    def run_game(self):
        """The main loop of the game"""
        while True:
            self._check_events()
            self._update_snake()
            self._update_screen()

    def _check_events(self):
        """Check for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_highscore()
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

    def _update_snake(self):
        """Update the snakes position and checks collisions"""
        self.snake.update()

        # Check if the snakes collides with himself or the border
        self._check_collide_snake()

        # Check collision with the fruit
        self._check_collide_fruit_snake()

    def _check_collide_snake(self):
        """Check collision between snake and edges and himself"""
        if self.snake.collide_edges() or self.snake.collide_himself():
            # Show the game over msg and update the screen one last time
            self.sb.prep_game_over_msg()
            self.sb.show_game_over_msg()
            pygame.display.flip()
            
            # Save the highscore and close the game
            self.stats.save_highscore()
            sleep(2)
            sys.exit()
            
    def _check_collide_fruit_snake(self):
        """Check collision with the fruit"""
        fruit_pos = (self.fruit.rect.x, self.fruit.rect.y)
        snake_tail = self.snake.snake_tail
        if fruit_pos in snake_tail:
            self._collide_snake_fruit(fruit_pos)

    def _collide_snake_fruit(self, new_pos):
        """Reposition the fruit if the snake eats it and make the snake and score bigger"""
        self.fruit.random_position_fruit()
        self.snake.append_tail()
        self.stats.score += self.settings.fruit_value
        self.sb.prep_score()
        self.sb.check_high_score()

    def _update_screen(self):
        """Update the screen each time the loops run"""

        self.screen.fill(self.settings.bgcolor)
        self.snake.draw_tail()
        self.fruit.draw_fruit()
        self.sb.show_score()

        # Update the screen with the new frame
        pygame.display.flip()

        # Pause between frames
        sleep(0.1)

if __name__ == "__main__":
    sg = SnakeGame()
    sg.run_game()
    