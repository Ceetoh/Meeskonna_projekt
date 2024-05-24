


import pygame
import sys
import random
from settings import Settings

pygame.init()

BLOCK_SIZE = 50
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE*2)



gm_settings = Settings()

SW, SH = 800, 800


screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
pygame.display.set_caption(gm_settings.caption)
clock = pygame.time.Clock()

def drawgrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#ffffff", rect, 1)

drawgrid()

running = True
while running:
#    screen.fill(gm_settings.bg_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(10)