import pygame
import sys
from Hero import MainCharacter

def start_game ():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaceX by Andrei")

    flag = True
    hero = MainCharacter(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.flip()
            hero.output()

start_game()