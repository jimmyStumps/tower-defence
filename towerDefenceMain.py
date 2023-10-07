import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 760
SCREEN_HEIGHT = 680
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((127, 63, 0))

# Background tiles
grass = pygame.image.load("grass.png").convert()
shrub = pygame.image.load("shrub.png").convert()
path = pygame.image.load("path0.png").convert()
path_corner = pygame.image.load("path1.png").convert()
path_t = pygame.image.load("path2.png").convert()
path_cross = pygame.image.load("path3.png").convert()
wizard_house = pygame.image.load("wizard_house.png").convert()
wizard_house.set_colorkey((0,0,0), RLEACCEL)

# Game Board
x = 0
y = 0
tile = grass
with open("level1.txt", "r") as level:
    for line in level:
        for c in line:
            match c:
                case "S":
                    tile = shrub
                case "X":
                    tile = path_cross
                case "W":
                    wizard_x = x
                    wizard_y = y
                case _:
                    tile = grass
            screen.blit(tile, (TILE_WIDTH*(x),TILE_HEIGHT*(y)+40))
            x += 1
        y += 1
        x = 0
        # TODO fix magic numbers
    screen.blit(wizard_house, (TILE_WIDTH*(wizard_x)-8,TILE_HEIGHT*(wizard_y)-8+40))

# Create clock
clock = pygame.time.Clock()

# Custom Events


# Main loop
running = True
while running:
    for event in pygame.event.get():
        # Quit the game from user input
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)