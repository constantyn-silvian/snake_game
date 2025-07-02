class Settings:
    """Settigs for the snake game"""

    def __init__(self):
        """Initialize the settings"""

        # Settings for the screen
        self.screen_width = 1000
        self.screen_height = 700
        self.bgcolor = (0, 0, 0)

        # Setting for the snake 
        self.snake_dim = 20
        self.snake_color = (4, 184, 52)

        # Settings for the fruit
        self.fruit_dim = 20
        self.fruit_color = (255, 0, 0)
        self.fruit_value = 10

        # Where the data will be stored
        self.datapath = "data/highscore.json"