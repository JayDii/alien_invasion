import sys
from time import sleep

import pygame
from random import randint

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize Game and create Game Resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # Create play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main Loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()            
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)              

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                

    def _check_keydown_events(self,event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            print(f"Current Bullets in memory: {len(self.bullets)}")

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create alien fleet"""
        # Make an alien and keep adding aliens until the is no space left on the screen
        # With spacing = 1 alien width and 1 alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row: reset x value and increment y
            current_x = alien_width + randint(-40, 40)
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an Alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break



    def _change_fleet_direction(self):
        """Drop the entire fleet and change the movement direction."""
        self.settings.fleet_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
    
    def _update_screen(self):
        """Update images on the screen, and flip to new screen."""
        # Redraw the screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the Play Button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently draw screen visible.
        pygame.display.flip()
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

        # Get rid of bullets out of screen:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(f"Current Bullets in memory: {len(self.bullets)}")

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""

        # Remove aliens and bullets that collide
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Reset Bullets and Spawn new aliens
            self.bullets.empty()
            self._create_fleet()

    def _fire_bullet(self):
        """Create a new bullet in front of the ship and add to the bullets group"""
        if (len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        """Check if fleet is at an edge, then update the positions"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look fo aliens that hit the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to ship beeing hit by an alien."""
        # Decrement "Lives"/ Ships left
        if self.stats.ships_left > 0:
            self.stats.ships_left =- 1
        else:
            self.game_active = False

        # Get rid of any objects on screen
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Pause for a moment
        sleep(0.5)

    def _check_aliens_bottom(self):
        """Check if any alien reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
    
if __name__ ==  '__main__':
    # Make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
