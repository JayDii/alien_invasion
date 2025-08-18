import sys

import pygame

class AlienInvasion:
    """Overall Class to manage game assets and behavior."""

    def __init__(self):
        """Initilize Game and create Game Resources."""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main Loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently draw screen visible.
            pygame.display.flip()

if __name__ ==  '__main__':
    # Make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
