import pygame
import Objects
import sys
import os
import random
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

decor1 = Objects.decor1
decor2 = Objects.decor2
decor3 = Objects.decor3
decor4 = Objects.decor4

light1 = Objects.light1
light2 = Objects.light2
light3 = Objects.light3
light4 = Objects.light4
light5 = Objects.light5
light6 = Objects.light6

clock = pygame.time.Clock()
end_points = 0
FPS = 60

# загрузить картинку для чего-либо
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


# убить программу
def terminate():
    pygame.quit()
    sys.exit()


# стартовый экран
def start_screen():
    intro_text = ["MusicDriver", "",
                  "Правила игры",
                  "Двигай мышкой и уворачивайся от мошын",
                  "Не ударься в края дороги, они кусаются!",
                  "спрайты не оч, но как умею",
                  "",
                  '',
                  '',
                  '',
                  'Нажми сюда',
                  '',
                  '',
                  '                              ЛКМ-бибип',
                  '                     колесо-музыка с АП',
                  '                ПКМ-переключатель паузы'
                  ]

    fon = pygame.transform.scale(load_image('sprites/fon_car.jpg'), size)
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

result = 0


def main():
    global result
    FPS = 60
    # музыка и звуки
    gudok = pygame.mixer.Sound('audio/gudok.mp3')

    playlist = ['soundtracks/1.mp3', 'soundtracks/2.mp3', 'soundtracks/3.mp3', 'soundtracks/4.mp3', 'soundtracks/5.mp3',
                'soundtracks/6.mp3']
    count = 0
    pause_count = 1  # счетчик паузы

    # ---

    # границы
    border1 = Objects.Border((0, 300))
    border2 = Objects.Border((0, 600))

    # ---

    MainCar = Objects.MainCar((0, 0))  # главная машина

    # ---

    # дорога
    road = Objects.Road((0, 0))
    deadend = Objects.Road((0, 1200))

    # ---

    coords = [53, 118, 183, 248]  # координаты полос
    # вражеские машины
    enemies1 = [Objects.EnemyCar((), coords[0], 'c1')]
    enemies2 = [Objects.EnemyCar((), coords[1], 'c2')]
    enemies3 = [Objects.EnemyCar2((), coords[2], 'c3')]
    enemies4 = [Objects.EnemyCar2((), coords[3], 'c4')]

    decor_list1 = [Objects.Decor(random.randint(0, 2), 0, 0)]
    decor_list2 = [Objects.Decor(random.randint(0, 2), 0, 1)]
    decor_list3 = [Objects.Decor(random.randint(0, 2), 0, 2)]
    decor_list4 = [Objects.Decor(random.randint(0, 2), 0, 3)]

    decor_list5 = [Objects.Light(4, 0, 4)]
    decor_list6 = [Objects.Light(5, 0, 4)]

    decor_list7 = [Objects.Light(6, 0, 4)]
    decor_list8 = [Objects.Light(7, 0, 4)]

    decor_list9 = [Objects.Light(8, 0, 4)]
    decor_list10 = [Objects.Light(9, 0, 4)]

    # проверка на возможность проезда между врагами
    if enemies1[0].rect.x - enemies2[0].rect.x <= 200 and enemies1[0].rect.x >= enemies2[0].rect.x:
        enemies1[0].rect.x += 300
    if enemies2[0].rect.x - enemies1[0].rect.x <= 200 and enemies2[0].rect.x >= enemies1[0].rect.x:
        enemies2[0].rect.x += 300

    # ---

    #  координаты машиныю нужно чтобы она перемещалась по полосам, иначе игра сильно багается
    coords1 = [-12, 53, 118, 183, 248, 313]
    MainCar.rect.y = 300 + coords1[2]
    MainCar.rect.x = 250
    coords_count = 2

    running = True
    while running:
        if MainCar.update() is True:
            pygame.mixer.music.stop()
        for event in pygame.event.get():
            # выход из программы
            if event.type == pygame.QUIT:
                running = False
            if MainCar.update() is True:
                pygame.mixer.music.stop()
                return
            # движение машины за курсором
            if event.type == pygame.MOUSEMOTION and MainCar.update() is False:
                MainCar.rect.center = event.pos

            if event.type == pygame.KEYDOWN and MainCar.update() is False:
                if event.key == pygame.K_s:
                    if coords_count < 5:
                        coords_count += 1
                    MainCar.rect.y = 300 + coords1[coords_count]
                if event.key == pygame.K_w:
                    if coords_count >= 0:
                        coords_count -= 1
                    MainCar.rect.y = 300 + coords1[coords_count]

            # Отдельная вкладка для мыши
            if True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # левая кнопка мыши, гудок
                    if event.button == 1:
                        gudok.play()

                    # правая кнопка мыши, пауза
                    if event.button == 3:
                        print(pause_count)
                        if pause_count == 1:
                            pause_count = 0
                            pygame.mixer.music.pause()

                        else:
                            pause_count = 1
                            pygame.mixer.music.unpause()

                    # нажатие колеса мыши, трек заново
                    if event.button == 2:
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

                    # колесо вверх, след. трек
                    if event.button == 4:
                        count += 1
                        if count >= len(playlist):
                            count = 0
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

                    # колесо вниз, пред. трек
                    if event.button == 5:
                        count -= 1
                        if count <= -1:
                            count = len(playlist) - 1
                        pygame.mixer.music.load(f'{playlist[count]}')
                        pygame.mixer.music.play()

                # левая кнопка мыши, отпустить гудок
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        gudok.stop()

        # ---

        # далее проверка на то, где игрок проиграл (в какой полосе или у границы дороги) и тогда что нужно остановить
        # и какую музыку включить
        if MainCar.update() == (True, 'c1'):
            return

        if MainCar.update() == (True, 'c2'):
            return

        if MainCar.update() == (True, 'c3'):
            return

        if MainCar.update() == (True, 'c4'):
            return

        if MainCar.update() == (True, 'b'):
            return
        # ---

        # переместить спрайт дороги если закончился
        if road.rect.left == 0:
            road.rect.left = 200
            deadend.rect.left = road.rect.left - deadend.rect.size[1]

        # ---

        # заливка цветом и обновление всего для цикла
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

        decor1.update(random.randint(0, 2))
        decor1.draw(screen)
        decor2.update(random.randint(0, 2))
        decor2.draw(screen)
        decor3.update(random.randint(0, 2))
        decor3.draw(screen)
        decor4.update(random.randint(0, 2))
        decor4.draw(screen)

        light1.update(4)
        light1.draw(screen)
        light2.update(5)
        light2.draw(screen)
        light3.update(6)
        light3.draw(screen)
        light4.update(7)
        light4.draw(screen)
        light5.update(8)
        light5.draw(screen)
        light6.update(9)
        light6.draw(screen)

        # ---
        clock.tick(FPS)
        pygame.display.flip()
        FPS += 0.01
        if FPS >= 240:
            FPS = 240
        result += 0.5
    pygame.quit()


def end_screen():
    global result
    pygame.mixer.music.stop()
    crash = pygame.mixer.Sound('audio/avaria.mp3')
    crash.play()
    #запись лучшего результата в файл
    with open('best_res.txt', 'r', encoding='utf=8') as best:
        bester = best.readline()
        best.close()
    with open('best_res.txt', 'w', encoding='utf=8') as best:
        if result > int(bester):
            bester = int(result)
            print(bester)
            best.write(str(bester))
        else:
            best.write(str(bester))
        best.close()

    intro_text = ["",
                  '',
                  '',
                  '',
                  '',
                  '               ВЫ УВОЛЕНЫ!',
                  f'              Ваш счёт:{int(result)}',
                  f'           Лучший результат:{bester}',
                  '          Чтобы выйти с позором,',
                  '           Нажмите на экран',
                  '']

    screen.fill('black')
    font = pygame.font.Font('shrift/Shrifty.ttf', 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, bool(1), pygame.Color('red'))
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


if __name__ == '__main__':
    start_screen()
    main()
    end_screen()
