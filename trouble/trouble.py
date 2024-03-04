import pygame
import sys
import random

# Initialize PyGame
pygame.init()

# Window setup
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Digital Trouble")

# Game loop flag
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
