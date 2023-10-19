import pygame
import random

# Загрузка изображений игрока, врага и пули
player_img = pygame.image.load('hero.png')
enemy_img = pygame.image.load('en.png')
bullet_img = pygame.image.load('bullet.png')

# Класс игрока
class Player:
    def __init__(self):
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 370
        self.rect.bottom = 480
        self.speed = 5

    def handle_movement(self, event):
        if event.key == pygame.K_LEFT:
            self.rect.x -= self.speed
        elif event.key == pygame.K_RIGHT:
            self.rect.x += self.speed

    def check_boundary(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Класс врага
class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 736)
        self.rect.y = random.randint(50, 150)
        self.speed = 2

    def move(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed *= -1
            self.rect.y += 40

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Основной игровой цикл
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.jpg')

player = Player()
enemies = []
for _ in range(5):
    enemy = Enemy()
    enemies.append(enemy)
bullets = []

running = True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.append(bullet)
            else:
                player.handle_movement(event)

    player.check_boundary()
    player.draw(screen)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    pygame.display.flip()

pygame.quit()