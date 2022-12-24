import random

import pygame
import Objects
import sys
import os

pygame.init()
size = (1200, 800)
pygame.display.set_caption('MusicDriver')
screen = pygame.display.set_mode(size)
gameIcon = pygame.image.load('sprites/car_icon.png')
pygame.display.set_icon(gameIcon)
borders = Objects.borders
decorations = Objects.decorations
maincar = Objects.main_car
cars = Objects.cars
FPS = 60
clock = pygame.time.Clock()


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


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["MusicDriver", "",
                  "Правила игры",
                  "Двигай мышкой и уворачивайся от мошын",
                  "Не ударься в края дороги, они кусаются!",
                  "спрайты не оч, но как умею",
                  "приходится выводить их построчно"
                  '',
                  '',
                  '',
                  'Нажми сюда']

    fon = pygame.transform.scale(load_image('sprites/lil_tree.png'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('shrift/Shrifty.ttf', 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, bool(1), pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.x = 10
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def main():
    i = 0
    border1 = Objects.Border((0, 300))
    border2 = Objects.Border((0, 600))
    MainCar = Objects.MainCar((0, 0))
    running = True
    carcrash = False
    road = Objects.Road((0, 0))
    deadend = Objects.Road((0, 1200))

    coords = [53, 118, 183, 248]
    count = random.randint(1, 3)
    enemies = []
    for j in range(count):
        enemy = Objects.EnemyCar((1000, 0), coords[random.randint(0, 3)])
        enemies.append(enemy)

    while running:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and carcrash is False:
                MainCar.rect.center = event.pos
            if event.type == pygame.AUDIO_ALLOW_ANY_CHANGE:
                pass
            if MainCar.update() is True:
                carcrash = True
        if carcrash is True:
            road.rect.left = 0
            for j in enemies:
                j.stop()
        if road.rect.left == 0:
            road.rect.left = 200
            deadend.rect.left = road.rect.left - deadend.rect.size[1]

        if enemies[0].rect.left == 0:
            enemies.clear()
            count = random.randint(1, 3)
            for j in range(count):
                enemy = Objects.EnemyCar((1000, 0), coords[random.randint(0, 3)])
                enemies.append(enemy)

        screen.fill("#212621")
        pygame.draw.rect(screen, 'gray', border1)
        pygame.draw.rect(screen, 'gray', border2)
        decorations.update()
        decorations.draw(screen)
        maincar.update()
        maincar.draw(screen)
        cars.update()
        cars.draw(screen)
        cars.update()
        cars.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    start_screen()
    main()
