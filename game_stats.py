import os, json

from settings import Settings

class GameStats:
    """Stats for the snake game"""

    def __init__(self):
        """Initialize the stats"""
        self.settings = Settings()
        self.highscore = self.load_highscore()
        self.reset_stats()

    def save_highscore(self):
        """Save the highscore in the data folder"""
        datapath = self.settings.datapath
        os.makedirs(os.path.dirname(datapath), exist_ok=True)
        with open(datapath, 'w') as f:
            json.dump({"Highscore": self.highscore}, f)

    def load_highscore(self):
        """Load highscore from the data folder"""
        datapath = self.settings.datapath
        try:
            with open(datapath, 'r') as f:
                data = json.load(f)
                return data.get("Highscore", 0)
        except (json.JSONDecodeError, ValueError, FileNotFoundError, AttributeError):
            return 0
        
    def reset_stats(self):
        """Stats that can change during the game"""
        self.score = 0
    