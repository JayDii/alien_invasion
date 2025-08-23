import pygame

import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Just a Blue Screen")





def check_events():
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)  

while True:
    check_events()
    screen.fill((50, 100, 200))
    pygame.display.flip()