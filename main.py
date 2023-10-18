import pygame
import sys
from main_character import MainCharacter

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaxeX by Pushkova")
    maincharacter = MainCharacter(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        maincharacter.output()
        pygame.display.flip()


start_game()
