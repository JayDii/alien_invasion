class Settings:
    """A class to store all game wide settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (94, 104, 115)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self. bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Alien Settings
        self.fleet_drop_speed = 10

        # fleet_direction of 1 indicates right; -1 represent left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How Quickly Alien points increase per level
        self.alien_points_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.alien_points_scale)
        print(f"New Level Reached. Each Alien grants: {self.alien_points} points now.")

