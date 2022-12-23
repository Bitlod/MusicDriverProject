import pygame

decorations = pygame.sprite.Group()
maincar = pygame.sprite.Group()
borders = pygame.sprite.Group()
cars = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    size = (1200, 50)

    def __init__(self, pos):
        super().__init__(borders)
        self.add(borders)
        self.image = pygame.Surface(Border.size)
        self.image.fill(pygame.Color('#808080'))
        self.rect = pygame.Rect(pos, Border.size)


class MainCar(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(maincar)
        self.add(maincar)
        self.image = pygame.image.load('sprites/main_car.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 420

    def update(self):
        if pygame.sprite.spritecollideany(self, cars) or pygame.sprite.spritecollideany(self, borders):
            self.image = pygame.image.load('sprites/destroyed_main_car.png').convert_alpha()
            return True


class Road(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(decorations)
        self.add(decorations)
        self.image = pygame.image.load('sprites/road.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 350

    def update(self, *args):
        self.rect.left -= 5
