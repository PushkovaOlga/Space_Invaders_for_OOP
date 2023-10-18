import pygame

class MainCharacter():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/pixil-frame-0 (1).png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        self.screen.blit(self.image, self.rect)