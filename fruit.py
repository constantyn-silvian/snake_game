import pygame

from settings import Settings
from random import randint

class Fruit:
    """A class for the fruits behavior and proprieties"""

    def __init__(self, s_game):
        """Initialize the fruits attributes"""
        
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.snake_tail = s_game.snake.snake_tail

        # Make the fruit start at the begining at a random pos and store its dimension
        self.fruit_dim = self.settings.fruit_dim

        self.random_position_fruit()

    def random_position_fruit(self):
        """Positions the fruit at a random pos on the screen and not inside the snake"""
        posx, posy = self._random_positions()
        while (posx, posy) in self.snake_tail:
            posx, posy = self._random_positions()

        self.rect = pygame.rect.Rect(posx, posy, self.fruit_dim, self.fruit_dim)

    def _random_positions(self):
        """Return a random pos on the screen"""
        return randint(0, self.settings.screen_width // self.fruit_dim - 1) * self.fruit_dim, randint(0, self.settings.screen_height // self.fruit_dim - 1) * self.fruit_dim
    
    def draw_fruit(self):
        """Draw the fruit to the screen"""
        self.screen.fill(self.settings.fruit_color, self.rect)