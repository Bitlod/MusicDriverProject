import pygame
import random
# Файл с результатами
# Группы спрайтов для всего
decorations = pygame.sprite.Group()
main_car = pygame.sprite.Group()
borders = pygame.sprite.Group()
cars1 = pygame.sprite.Group()
cars2 = pygame.sprite.Group()
cars3 = pygame.sprite.Group()
cars4 = pygame.sprite.Group()

decor1 = pygame.sprite.Group()
decor2 = pygame.sprite.Group()
decor3 = pygame.sprite.Group()
decor4 = pygame.sprite.Group()

light1 = pygame.sprite.Group()
light2 = pygame.sprite.Group()
light3 = pygame.sprite.Group()
light4 = pygame.sprite.Group()
light5 = pygame.sprite.Group()
light6 = pygame.sprite.Group()


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
        self.speed = random.randint(5, 20)
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
        self.rect.left -= self.speed
        if pygame.sprite.spritecollideany(self, main_car) and self.truck is False:
            self.image = pygame.image.load('sprites/destroyed_enemy_car.png').convert_alpha()

        if pygame.sprite.spritecollideany(self, main_car) and self.truck is True:
            self.image = pygame.image.load('sprites/destroyed_truck.png').convert_alpha()

        if self.rect.x in range(-100, -50):
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)

    # функция стопа (при столкновении)
    def again(self, *args):
        if self.rect.left == 0:
            return True
        else:
            return False


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
        self.speed = random.randint(2, 10)
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
        self.rect.left += self.speed
        if pygame.sprite.spritecollideany(self, main_car) and self.truck is False:
            self.image = pygame.image.load('sprites/destroyed_enemy_car2.png').convert_alpha()

        if pygame.sprite.spritecollideany(self, main_car) and self.truck is True:
            self.image = pygame.image.load('sprites/destroyed_truck2.png').convert_alpha()

        if self.rect.x in range(-500, -450):
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)

        if self.rect.x in range(2350, 2500):
            self.rect.x = random.randint(-300, -100) + random.randint(-100, 100)

    def again(self, *args):
        if self.rect.right == 0:
            return True
        else:
            return False


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


class Decor(pygame.sprite.Sprite):
    def __init__(self, rand, x, clas):
        self.object = rand

        if clas == 0:
            super().__init__(decor2)
            self.add(decor2)
            # ---

            if self.object == 0:
                self.image = pygame.image.load('sprites/house.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 30

            elif self.object == 1:
                self.image = pygame.image.load('sprites/hrusevka.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 30

            elif self.object == 2:
                self.image = pygame.image.load('sprites/lil_tree.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 30

        if clas == 1:
            super().__init__(decor2)
            self.add(decor2)
            # ---

            if self.object == 0:
                self.image = pygame.image.load('sprites/house.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 130

            elif self.object == 1:
                self.image = pygame.image.load('sprites/hrusevka.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 130

            elif self.object == 2:
                self.image = pygame.image.load('sprites/lil_tree.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 130

        if clas == 2:
            super().__init__(decor3)
            self.add(decor3)
            # ---

            if self.object == 0:
                self.image = pygame.image.load('sprites/house.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 200

            elif self.object == 1:
                self.image = pygame.image.load('sprites/hrusevka.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 200

            elif self.object == 2:
                self.image = pygame.image.load('sprites/lil_tree.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 200

        if clas == 3:
            super().__init__(decor4)
            self.add(decor4)

            # ---

            if self.object == 0:
                self.image = pygame.image.load('sprites/house.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 800

            elif self.object == 1:
                self.image = pygame.image.load('sprites/hrusevka.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 800

            elif self.object == 2:
                self.image = pygame.image.load('sprites/lil_tree.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
                self.rect.y = 800

    # функция обновления (передвижение врага)
    def update(self, rand):
        self.rect.left -= 3

        if self.rect.x in range(-100, -50):
            self.rect.x = random.randint(1500, 1900) + random.randint(-300, 400)
            self.object = random.randint(0, 2)


class Light(pygame.sprite.Sprite):
    def __init__(self, rand, x, clas):
        self.object = rand
        if clas == 4:

            # ---

            if self.object == 4:
                super().__init__(light1)
                self.add(light1)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 1500
                self.rect.y = 280

            if self.object == 5:
                super().__init__(light2)
                self.add(light2)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 1500
                self.rect.y = 570

            if self.object == 6:
                super().__init__(light3)
                self.add(light3)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 2100
                self.rect.y = 280

            if self.object == 7:
                super().__init__(light4)
                self.add(light4)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 2100
                self.rect.y = 570

            if self.object == 8:
                super().__init__(light5)
                self.add(light5)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 2700
                self.rect.y = 280

            if self.object == 9:
                super().__init__(light6)
                self.add(light6)
                self.image = pygame.image.load('sprites/light.png').convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x = 2700
                self.rect.y = 570

    def update(self, rand):
        self.rect.left -= 5

        if self.rect.x in range(-100, -50):
            if rand == 4:
                self.rect.x = self.rect.x = 1500

            if rand == 5:
                self.rect.x = self.rect.x = 1500

            if rand == 6:
                self.rect.x = self.rect.x = 2100

            if rand == 7:
                self.rect.x = self.rect.x = 2100

            if rand == 8:
                self.rect.x = self.rect.x = 2700

            if rand == 9:
                self.rect.x = self.rect.x = 2700