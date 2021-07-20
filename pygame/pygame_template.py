
# Cпрайт игрока и управление
import pygame
import random
import sys
from pygame.color import THECOLORS
import pygame_menu

WIDTH = 858
HEIGHT = 535
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BEEP")
clock = pygame.time.Clock()

class player_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()


class player_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill()
        self.rect = self.image.get_rect()


class player_up(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/Arrow_up.png')
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 40
        self.rect.center = (WIDTH / 3, HEIGHT / 3)


class player_down(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/Arrow_down.png')
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 60
        self.rect.center = (WIDTH / 1, HEIGHT / 1)


all_sprites = pygame.sprite.Group()

player_down = player_down()
all_sprites.add(player_down)

player_up = player_up()
all_sprites.add(player_up)

player_right = player_right()
all_sprites.add(player_right)

player_left = player_left()
all_sprites.add(player_left)


done = False

all_sprites.update()

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False




pygame.quit()