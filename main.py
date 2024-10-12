import pygame
from pygame import locals as const

from road_segment import draw_dashed_line, RoadSegment

COLOR_WHITE = (255, 255, 255)


def main():

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    # line_up = pygame.draw.line(screen, (255, 255, 255), (0, 100), (1280, 100), 5)

    road_segment1 = RoadSegment((0, 100))
    road_segment2 = RoadSegment((80, 100))
    road_segment3 = RoadSegment((450, 230), False)

    run = True

    while run:

        screen.fill('black')

        road_segment1.draw(screen)
        road_segment2.draw(screen)
        road_segment3.draw(screen)

        for event in pygame.event.get():
            if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                run = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
