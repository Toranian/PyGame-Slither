import os, sys, time
import pygame
from settings import *

# Game display: 6 | Title: 7 | Game Exit: 8 | Initialization: 9-10
# Lead X & Y |
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slither")
gameExit = False
init = pygame.init()
print("{} Successes, {} Failures".format(init[0], init[1]))

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

# Game loop
while not gameExit:
    # Event handler | Quit: 16 |
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lead_x_change = -10
            if event.key == pygame.K_d:
                lead_x_change = 10

    # Border detections
    if lead_x >= WIDTH:
        lead_x = 0
    elif lead_x == 0:
        lead_x = WIDTH

    lead_x += lead_x_change
    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
