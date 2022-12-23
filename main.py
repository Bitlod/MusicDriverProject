import pygame
import Objects

pygame.init()
size = (1200, 800)
pygame.display.set_caption('MusicDriver')
screen = pygame.display.set_mode(size)
gameIcon = pygame.image.load('sprites/car_icon.png')
pygame.display.set_icon(gameIcon)

all_sprites = Objects.all_sprites


def menu():
    i = 0
    FPS = 30
    clock = pygame.time.Clock()
    MainCar = Objects.MainCar((0, 0))
    c = 10
    running = True
    carcrash = False
    road = Objects.Road((0, 0))
    deadend = Objects.Road((0, 1200))
    while running:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and carcrash is False and i != c:
                MainCar.rect.center = event.pos
            if event.type == pygame.AUDIO_ALLOW_ANY_CHANGE:
                pass
            if i == c:
                i = 0
        if road.rect.left == 0:
            road.rect.left = 200
            deadend.rect.left = road.rect.left - deadend.rect.size[1]
        screen.fill("#000000")
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    menu()
