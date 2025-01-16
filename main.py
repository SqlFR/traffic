import time

import pygame
from pygame import locals as const

from road_segment import RoadSegment
from traffic_lights import TrafficLights


def main():

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    traffic_lights1 = TrafficLights((100, 100))

    road_segment1 = RoadSegment((0, 100))
    road_segment2 = RoadSegment((80, 100))
    road_segment3 = RoadSegment((160, 100))
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

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    def round_light(traffic_light, current_time):
        if current_time < 10000:
            traffic_light.green_light()
        elif current_time < 11500:
            traffic_light.orange_light()
        else:
            traffic_light.red_light()

    while run:
        traffic_lights1.draw(screen)

        # Calculate elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time
        round_light(traffic_lights1, elapsed_time % 21500)  # Cycle every 21,5 seconds

        for event in pygame.event.get():
            if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                run = False

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()



