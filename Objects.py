import pygame
import random

# Группы спрайтов для всего
decorations = pygame.sprite.Group()
main_car = pygame.sprite.Group()
borders = pygame.sprite.Group()
cars1 = pygame.sprite.Group()
cars2 = pygame.sprite.Group()
cars3 = pygame.sprite.Group()
cars4 = pygame.sprite.Group()


# класс границы дороги (сверху и снизу, чтоб не ехать по траве)
class Border(pygame.sprite.Sprite):
    size = (1200, 50)  # размер границы

    def __init__(self, pos):
        super().__init__(borders)
        self.add(borders)
        self.image = pygame.Surface(Border.size)
        self.image.fill(pygame.Color('#808080'))
        self.rect = pygame.Rect(pos, Border.size)


# класс верхних двух рядов вражеских машин
class EnemyCar(pygame.sprite.Sprite):
    # понимает, в какой ряд добавить машину
    def __init__(self, pos, x, cr):
        if cr == 'c1':
            super().__init__(cars1)
            self.add(cars1)

        if cr == 'c2':
            super().__init__(cars2)
            self.add(cars2)

        if cr == 'c3':
            super().__init__(cars3)
            self.add(cars3)

        if cr == 'c4':
            super().__init__(cars4)
            self.add(cars4)

        # ---

        self.truck = False  # проверка на грузовик
        self.car = random.randint(0, 1)
        if self.car == 0:
            self.image = pygame.image.load('sprites/truck.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
            self.rect.y = 295 + x
            self.truck = True
        else:
            self.image = pygame.image.load('sprites/enemy_car.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
            self.rect.y = 300 + x
            self.truck = False

    # функция обновления (передвижение врага)
    def update(self, *args):
        self.rect.left -= 6
        if pygame.sprite.spritecollideany(self, main_car) and self.truck is False:
            self.image = pygame.image.load('sprites/destroyed_enemy_car.png').convert_alpha()

        if pygame.sprite.spritecollideany(self, main_car) and self.truck is True:
            self.image = pygame.image.load('sprites/destroyed_truck.png').convert_alpha()

        if self.rect.x in range(-100, -50):
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)

    # функция стопа (при столкновении)
    def stop(self, *args):
        self.rect.x += 6


# класс нижних двух рядов вражеских машин
class EnemyCar2(pygame.sprite.Sprite):
    # не буду описывать почти тоже самое, опишу лишь другое
    def __init__(self, pos, x, cr):
        if cr == 'c1':
            super().__init__(cars1)
            self.add(cars1)

        if cr == 'c2':
            super().__init__(cars2)
            self.add(cars2)

        if cr == 'c3':
            super().__init__(cars3)
            self.add(cars3)

        if cr == 'c4':
            super().__init__(cars4)
            self.add(cars4)

        # ---

        self.truck = False
        self.car = random.randint(0, 1)
        if self.car == 0:
            self.image = pygame.image.load('sprites/truck2.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
            self.rect.y = 295 + x
            self.truck = True
        else:
            self.image = pygame.image.load('sprites/enemy_car2.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
            self.rect.y = 300 + x
            self.truck = False

    def update(self, *args):
        self.rect.left -= 4
        if pygame.sprite.spritecollideany(self, main_car) and self.truck is False:
            self.image = pygame.image.load('sprites/destroyed_enemy_car2.png').convert_alpha()

        if pygame.sprite.spritecollideany(self, main_car) and self.truck is True:
            self.image = pygame.image.load('sprites/destroyed_truck2.png').convert_alpha()

        if self.rect.x in range(-500, -450):
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)

        if self.rect.x in range(2350, 2500):
            self.rect.x = random.randint(-300, -100) + random.randint(-100, 100)

    def stop(self, *args):
        self.rect.x += 4

    # функция передвижения при столкновении с другим рядом или границей для реалистичной скорости
    def revert(self, *args):
        self.rect.x += 8


# класс главной машины
class MainCar(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(main_car)
        self.add(main_car)
        self.image = pygame.image.load('sprites/main_car.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 420

    # проверка на столкновение с чем-то
    def update(self):
        if pygame.sprite.spritecollideany(self, cars1):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True, 'c1'

        if pygame.sprite.spritecollideany(self, cars2):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True, 'c2'

        if pygame.sprite.spritecollideany(self, cars3):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True, 'c3'

        if pygame.sprite.spritecollideany(self, cars4):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True, 'c4'

        if pygame.sprite.spritecollideany(self, borders):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True, 'b'

        else:
            return False


# класс дороги
class Road(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(decorations)
        self.add(decorations)
        self.image = pygame.image.load('sprites/road.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 350

    # движение дороги
    def update(self, *args):
        self.rect.left -= 5
