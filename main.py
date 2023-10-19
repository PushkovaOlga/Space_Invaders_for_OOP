import pygame
import sys
from main_character import MainCharacter

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaxeX by Semakov")

    flag = True
    maincharacter = MainCharacter(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_d:
                    maincharacter.rect.centerx += 1


        pygame.display.flip()
        maincharacter.output()


start_game()
