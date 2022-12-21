import pygame
import Objects

pygame.init()
size = (1200, 800)
pygame.display.set_caption('MusicDriver')
screen = pygame.display.set_mode(size)
gameIcon = pygame.image.load('sprites/car_icon.png')
pygame.display.set_icon(gameIcon)

all_sprites = Objects.all_sprites
borders = Objects.borders


def menu():
    i = 0
    FPS = 30
    clock = pygame.time.Clock()
    car = Objects.MainCar((0, 0))
    c = 10
    running = True
    carcrash = False
    while running:
        road = Objects.Road((0, 0))
        deadend = Objects.Road((0, 1200))
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and carcrash is False and i != c:
                car.rect.center = event.pos
            if event.type == pygame.AUDIO_ALLOW_ANY_CHANGE:
                pass
            if i == c:
                i = 0
        if road.rect.right == 1200:
            road.rect.right = 0
            deadend.rect.right = road.rect.right - deadend.rect.size[1]
        screen.fill("#000000")
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    menu()
