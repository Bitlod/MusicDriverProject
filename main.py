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
cars1 = Objects.cars1
cars2 = Objects.cars2
cars3 = Objects.cars3
cars4 = Objects.cars4
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


def avaria():
    pygame.mixer.music.load('audio/avaria.mp3')
    pygame.mixer.music.play()


def main():
    music = pygame.mixer.Sound('audio/avaria.mp3')
    tormoz = pygame.mixer.Sound('audio/tormoz.mp3')
    gudok = pygame.mixer.Sound('audio/gudok.mp3')

    playlist = ['soundtracks/1.mp3', 'soundtracks/2.mp3', 'soundtracks/3.mp3', 'soundtracks/4.mp3', 'soundtracks/5.mp3']
    count = 0

    i = 0
    border1 = Objects.Border((0, 300))
    border2 = Objects.Border((0, 600))

    MainCar = Objects.MainCar((0, 0))

    running = True

    road = Objects.Road((0, 0))
    deadend = Objects.Road((0, 1200))

    coords = [53, 118, 183, 248]
    enemies1 = []
    enemies2 = []
    enemies3 = []
    enemies4 = []

    enemies1.append(Objects.EnemyCar((), coords[0], 'c1'))
    enemies2.append(Objects.EnemyCar((), coords[1], 'c2'))
    enemies3.append(Objects.EnemyCar2((), coords[2], 'c3'))
    enemies4.append(Objects.EnemyCar2((), coords[3], 'c4'))

    if enemies1[0].rect.x - enemies2[0].rect.x <= 200 and enemies1[0].rect.x >= enemies2[0].rect.x:
        enemies1[0].rect.x += 300
    if enemies2[0].rect.x - enemies1[0].rect.x <= 200 and enemies2[0].rect.x >= enemies1[0].rect.x:
        enemies2[0].rect.x += 300

    while running:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and MainCar.update() is False:
                MainCar.rect.center = event.pos

            # Отдельная вкладка для мыши
            if True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gudok.play()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        gudok.stop()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # левая кнопка мыши
                        pygame.mixer.music.pause()

                    if event.button == 3:  # правая кнопка мыши
                        pygame.mixer.music.unpause()

                    if event.button == 2:  # средняя кнопка мыши
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

                    if event.button == 4:  # колесо вверх
                        count += 1
                        if count >= len(playlist):
                            count = 0
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

                    if event.button == 5:  # колесо вниз
                        count -= 1
                        if count <= -1:
                            count = len(playlist) - 1
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

        # ---

        if MainCar.update() == (True, 'c1'):
            enemies1[0].stop()
            enemies2[0].stop()
            road.rect.left = 0
            if music is not None:
                music.play()
                music = None

        if MainCar.update() == (True, 'c2'):
            enemies1[0].stop()
            enemies2[0].stop()
            road.rect.left = 0
            if music is not None:
                music.play()
                music = None

        if MainCar.update() == (True, 'c3'):
            enemies3[0].stop()
            enemies4[0].stop()
            road.rect.left = 0
            if music is not None:
                music.play()
                music = None

        if MainCar.update() == (True, 'c4'):
            enemies3[0].stop()
            enemies4[0].stop()
            road.rect.left = 0
            if music is not None:
                music.play()
                music = None

        if MainCar.update() == (True, 'b'):
            road.rect.left = 0
            enemies3[0].revert()
            enemies4[0].revert()
            if tormoz is not None:
                tormoz.play()
                tormoz = None

        if road.rect.left == 0:
            road.rect.left = 200
            deadend.rect.left = road.rect.left - deadend.rect.size[1]

        screen.fill("#212621")
        pygame.draw.rect(screen, 'gray', border1)
        pygame.draw.rect(screen, 'gray', border2)
        decorations.update()
        decorations.draw(screen)
        maincar.update()
        maincar.draw(screen)

        cars1.update()
        cars1.draw(screen)
        cars2.update()
        cars2.draw(screen)
        cars3.update()
        cars3.draw(screen)
        cars4.update()
        cars4.draw(screen)

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    start_screen()
    main()
