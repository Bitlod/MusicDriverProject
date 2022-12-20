import pygame
import os
import sys
import random

all_sprites = pygame.sprite.Group()
borders = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# class EnemyCar(pygame.sprite.Sprite):
#     image = load_image('enemy_car.png')
#     distance_height = [200, 400, 600, 800]
#
#     def __init__(self, *group):
#         super().__init__(*group)
#         self.image = EnemyCar.image
#         self.rect = self.image.get_rect()
#         self.rect.y = random.randint(self.distance_height[0], self.distance_height[3])
#
#     def update(self):
#         self.rect = self.rect.move(random.randrange(3) - 1,
#                                    random.randrange(3) - 1)


# class Truck(EnemyCar):
#     truck_image = load_image('truck.png')


class MainCar(pygame.sprite.Sprite):
    size = (20, 20)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(all_sprites)
        self.image = pygame.image.load('main_car.png').convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, *args):
        if pygame.sprite.spritecollideany(self):
            self.image = load_image('destroyed_main_car.png')
            self.carcrash = True


class Border(pygame.sprite.Sprite):
    size = (50, 10)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(borders)
        self.image = pygame.Surface(Border.size)
        self.image.fill(pygame.Color('#808080'))
        self.rect = pygame.Rect(pos, Border.size)


class Road(pygame.sprite.Sprite):
    size = (20, 20)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(all_sprites)
        self.image = pygame.image.load('road.png').convert()
        self.rect = self.image.get_rect()
