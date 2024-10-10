import pygame
from pygame import locals as const


def main():

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                run = False

        screen.fill('black')

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
