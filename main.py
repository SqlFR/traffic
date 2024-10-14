import pygame
from pygame import locals as const

from road_segment import RoadSegment
from colors import Colors


def main():

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    # rect_lights = pygame.Rect(40, 40, 30, 12)

    road_segment1 = RoadSegment((0, 100))
    road_segment2 = RoadSegment((80, 100))
    road_segment3 = RoadSegment((160, 100), has_traffic_lights=True)
    road_segment4 = RoadSegment((240, 20), False)
    road_segment5 = RoadSegment((280, 100))
    road_segment6 = RoadSegment((240, 140), False)
    road_segment7 = RoadSegment((320, 100))

    screen.fill((59, 59, 59))

    # pygame.draw.rect(screen, Colors.BLACK.value, rect_lights, 2)

    road_segment1.draw(screen)
    road_segment2.draw(screen)
    road_segment3.draw(screen)
    road_segment4.draw(screen)
    road_segment5.draw(screen)
    road_segment6.draw(screen)
    road_segment7.draw(screen)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                run = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
