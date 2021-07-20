# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import pygame_menu
import os
import Some_Thing

WIDTH = 1280
HEIGHT = 720
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def __init__(self):
    self.bindings = {"up": pygame.K_UP,
                     "down":  pygame.K_DOWN,
                     "left":  pygame.K_LEFT,
                     "right":   pygame.K_RIGHT,
                     "lp":  pygame.K_a,
                     "mp":  pygame.K_s,
                     "hp":  pygame.K_d,
                     "lk":  pygame.K_z,
                     "mk":  pygame.K_x,
                     "hk":  pygame.K_c,
                     "pause":   pygame.K_RETURN}

    self.inputState = {"up": False,
                   "down": False,
                   "right": False,
                   "left": False,
                   "lp": False,
                   "mp": False,
                   "hp": False,
                   "lk": False,
                   "mk": False,
                   "hk": False,
                   "pause": False}

y = 790


start_game = True


class Player_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Ghost_left.png')
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 10


class Player_down(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Ghost_down.png')
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 10


class Player_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Ghost_up.png')
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 10

class Player_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Ghost_right.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = 790
        self.rect.y = 10

class Arrow_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Arrow_left.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Arrow_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Arrow_up.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Arrow_down(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Arrow_down.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Arrow_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Arrow_right.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.y = y


class Miss_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Miss_up.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Miss_down(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Miss_down.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Miss_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Miss_left.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Miss_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Miss_right.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Miss_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Miss_up.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Good_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Good_up.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Good_down(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Good_down.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Good_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Good_right.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

class Good_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Good_left.png')
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()

while start_game == True:
     y -= 1
Player = [Player_up, Player_right, Player_down, Player_left]
Arrow = [Arrow_right, Arrow_up, Arrow_down, Arrow_left]
Miss = [Miss_up, Miss_left, Miss_right, Miss_down]
Good = [Good_up, Good_left, Good_down, Good_right]



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BEEP")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player_left = Player_left()
all_sprites.add(player_left)

player_down = Player_down()
all_sprites.add(player_down)

player_up = Player_up()
all_sprites.add(player_up)

player_right = Player_right()
all_sprites.add(player_right)

arrow_right = Arrow_right()
all_sprites.add(arrow_right)



# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()


    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()

