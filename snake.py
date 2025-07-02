import pygame

from settings import Settings

class Snake:
    """A class for the snakes behavior and proprieties"""

    def __init__(self, s_game):
        """Initialize the snakes elements"""
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        # Position the snakes first parts and store its dimension"""
        self.snake_dim = self.settings.snake_dim
        
        self.snake_tail = []
        for i in range(4):
            self.snake_tail.append((self.settings.screen_width // 2 - 3 * self.snake_dim + i * self.snake_dim, self.settings.screen_height // self.snake_dim // 2 * self.snake_dim))

        # Moving flags and last direction and curent direction
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.last_dir = 'r'
        self.cur_dir = 'r'

    def update(self):
        """Check the direction the snake is moving and update its position"""
        
        new_x, new_y = self._get_new_positions()

        # Check if going inside yourself and update the snakes position
        if not (new_x, new_y) in self.snake_tail:
            self.last_dir = self.cur_dir
        else:
            self.cur_dir = self.last_dir
            self.update_direction(self.cur_dir)
            new_x, new_y = self._get_new_positions()

        self.snake_tail.append((new_x, new_y))
        self.snake_tail.pop(0)

    def _get_new_positions(self):
        """Return the new positions where the snake will be heading"""
        if self.moving_right:
            new_x = self.snake_tail[-1][0] + self.snake_dim
            new_y = self.snake_tail[-1][1]
        elif self.moving_left:
            new_x = self.snake_tail[-1][0] - self.snake_dim
            new_y = self.snake_tail[-1][1]
        elif self.moving_up:
            new_x = self.snake_tail[-1][0] 
            new_y = self.snake_tail[-1][1] - self.snake_dim
        elif self.moving_down:
            new_x = self.snake_tail[-1][0]
            new_y = self.snake_tail[-1][1] + self.snake_dim
        
        return new_x, new_y

    def update_direction(self, dir):
        """Update the direction based on the functions input"""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.cur_dir = dir

        if dir == 'r':
            self.moving_right = True
        elif dir == 'l':
            self.moving_left = True
        elif dir == 'u':
            self.moving_up = True
        elif dir == 'd':
            self.moving_down = True
    
    def append_tail(self):
        """Makes the snake bigger with """
        self.snake_tail.append(self.snake_tail[-1])

    def collide_edges(self):
        """Check if the snake collides with the edges"""
        frontx, fronty = self.snake_tail[-1]
        return frontx < 0 or frontx >= self.settings.screen_width or fronty < 0 or fronty >= self.settings.screen_height
    
    def collide_himself(self):
        """Check if the snake collides with himself"""
        if self.snake_tail[-1] in self.snake_tail[:-1]:
            return True
        return False

    def draw_tail(self):
        """Draw the snake and his tail"""
        for x, y in self.snake_tail:
            rect = pygame.rect.Rect(x, y, self.snake_dim, self.snake_dim)
            self.screen.fill(self.settings.snake_color, rect)