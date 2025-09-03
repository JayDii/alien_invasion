class GameStats:
    """Track Statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Stats that can change throughout the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
