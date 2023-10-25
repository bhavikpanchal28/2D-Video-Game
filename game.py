import os
import random
import math
import pygame 
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Adventurer")             # Sets the name of the window

BG_COLOR = (255, 255, 255)              # Background color
WIDTH, HEIGHT = 1000, 800
FPS = 60                # Frames per second
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()              # Creates a clock  

    run = True
    while run:
        clock.tick(FPS)         # 60 frames per second
        for event in pygame.event.get():                
            if event.type == pygame.QUIT:               
                run = False


if __name__ == "__main__":                      # If the file is run directly
    main(window)