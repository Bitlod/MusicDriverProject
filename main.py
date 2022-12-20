import pygame
import Objects

pygame.init()
width, height = 1200, 800
pygame.display.set_caption('MusicDriver')
screen = pygame.display.set_mode((width, height))
FPS = 30

background = pygame.Surface((width, height))

background.fill(pygame.Color('white'))

clock = pygame.time.Clock()
gameIcon = pygame.image.load('car_icon.png')
pygame.display.set_icon(gameIcon)
car = Objects.MainCar((0, 0))
all_sprites = Objects.all_sprites
borders = Objects.borders


def menu():
    i = 0
    c = 10
    running = True
    carcrash = False
    while running:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and carcrash is False and i != c:
                car.rect.topleft = event.pos
            if event.type == pygame.AUDIO_ALLOW_ANY_CHANGE:
                pass
            if i == 10:
                i = 0

        screen.fill("#000000")
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)
        pygame.display.flip()
        screen.blit(background, (0, 0))


if __name__ == '__main__':
    menu()
