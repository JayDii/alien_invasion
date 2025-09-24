import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font Settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_ammo_left()
        

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)

        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display Score at top right cornor
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =  self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn Highscore into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        high_score_str = f"Highscore: {high_score_str}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center Highscore at the top center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ammo_left(self):
        """Display the Shots ready depending on the bullet amount allowed"""
        current_ammo = self.settings.bullets_allowed - len(self.ai_game.bullets)
        ammo_str = f"Energy: {current_ammo} / {self.settings.bullets_allowed}"
        self.ammo_image = self.font.render(ammo_str, True, self.text_color, self.settings.bg_color)

        # Display on bottom right
        self.ammo_rect = self.ammo_image.get_rect()
        self.ammo_rect.right = self.screen_rect.right - 20
        self.ammo_rect.bottom = self.screen_rect.bottom - 20

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.high_score_rect.bottom + 10


    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw scores and level on screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ammo_image, self.ammo_rect)
        self.ships.draw(self.screen)

    def check_new_high_score(self):
        """Check if there is a new highscore"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    