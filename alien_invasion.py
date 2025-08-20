import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage game assets and behavior."""

    def __init__(self):
        """Initilize Game and create Game Resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main Loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()            
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Set movement flags when left or right key are pressed
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True


            elif event.type == pygame.KEYUP:
                # Remove movement flags when keys are released
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to new screen."""
        # Redraw the screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently draw screen visible.
        pygame.display.flip()


if __name__ ==  '__main__':
    # Make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
