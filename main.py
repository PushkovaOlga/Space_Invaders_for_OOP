import pygame
import sys
from pygame.locals import *
from Character import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')

background_img = pygame.image.load('background.jpg')

player = Player()

enemies = []
for i in range(6):
    enemy = Enemy()
    enemies.append(enemy)

bullets = []

while True:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            player.handle_movement(event)

            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.x, player.y)
                bullets.append(bullet)

    player.check_boundary()

    player.draw(screen)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

        if bullet.y < 0:
            bullets.remove(bullet)

    pygame.display.update()