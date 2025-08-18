import sys

import pygame

class AlienInvasion:
    """Overall Class to manage game assets and behavior."""

    def __init__(self):
        """Initilize Game and create Game Resources."""

        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main Loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently draw screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ ==  '__main__':
    # Make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
