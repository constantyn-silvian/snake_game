import pygame.font

class ScoreBoard:
    """A scoreboard for the snake game"""

    def __init__(self, s_game):
        """Initialize the scoreboards elements"""
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = s_game.stats
        self.settings = s_game.settings

        # Make the font for scoring information
        self.font = pygame.font.SysFont(None, 28)

        # Make the score and highscore initially show
        self.prep_score()
        self.prep_highscore()

    def prep_score(self):
        """Render the score as an image and position it"""
        formated_score = "{:,}".format(self.stats.score)
        score_str = f"score: {formated_score}"
        self.score_img = self.font.render(score_str, True, (255, 255, 255))
        self.score_img_rect = self.score_img.get_rect()

        # Position the score
        self.score_img_rect.x = 10
        self.score_img_rect.y = 10
    
    def prep_highscore(self):
        """Render the highscore as an image and position it"""
        formated_highscore = "{:,}".format(self.stats.highscore)
        score_str = f"highscore: {formated_highscore}"
        self.high_score_img = self.font.render(score_str, True, (255, 255, 255))
        self.high_score_img_rect = self.high_score_img.get_rect()

        # Position the highscore
        self.high_score_img_rect.x = self.settings.screen_width - self.high_score_img_rect.width - 10
        self.high_score_img_rect.y = 10
    
    def prep_game_over_msg(self):
        """Prepare the game over msg"""
        formated_score = "{:,}".format(self.stats.score)
        game_over_msg = f"Game Over! Your score is {formated_score}"
        self.game_over_image = self.font.render(game_over_msg, True, (255, 255, 255))
        self.game_over_image_rect = self.game_over_image.get_rect()

        # Position the msg
        self.game_over_image_rect.center = self.screen_rect.center

    def show_game_over_msg(self):
        """Show this msg when the game ends"""
        self.screen.blit(self.game_over_image, self.game_over_image_rect)

    def show_score(self):
        """Draws the stats to the screen"""
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.high_score_img, self.high_score_img_rect)

    def check_high_score(self):
        """Update to a new highscore if needed"""
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()
