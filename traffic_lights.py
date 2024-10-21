import pygame
from colors import Colors


class TrafficLights:
    def __init__(self, position_road, localisation_traffic_lights, state):
        self.state = state
        self.position_road = position_road
        self.localisation = localisation_traffic_lights  # Renseigne vers où se trouve le carrefour par apport au segment de route

        self.red_light = pygame.image.load('images/red_light.png').convert_alpha()
        self.orange_light = pygame.image.load('images/orange_light.png').convert_alpha()
        self.green_light = pygame.image.load('images/green_light.png').convert_alpha()

        x, y = self.position_road

        if self.localisation == 'Right':
            self.position_traffic_lights = x + 125, y + 45
            self.green_light = pygame.transform.rotate(self.green_light, -90)
            self.red_light = pygame.transform.rotate(self.red_light, -90)
        elif self.localisation == 'Bottom':
            self.position_traffic_lights = x - 20, y + 125
            self.green_light = pygame.transform.rotate(self.green_light, 180)
            self.red_light = pygame.transform.rotate(self.red_light, 180)
        elif self.localisation == 'Left':
            self.position_traffic_lights = x - 80, y - 18
            self.green_light = pygame.transform.rotate(self.green_light, 90)
            self.red_light = pygame.transform.rotate(self.red_light, 90)
        elif self.localisation == 'Top':
            self.position_traffic_lights = x + 45, y - 80

    def change_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def draw(self, surface):

        if self.state == 'red':
            surface.blit(scale_image(self.red_light, 0.05), self.position_traffic_lights)
        elif self.state == 'orange':
            surface.blit(scale_image(self.orange_light, 0.05), self.position_traffic_lights)
        elif self.state == 'green':
            surface.blit(scale_image(self.green_light, 0.05), self.position_traffic_lights)


        # Dessine un cercle représentant le feu de signalisation
        # pygame.draw.circle(surface, color, self.position_traffic_lights, 5)


def scale_image(image, scale):
    width = image.get_width()
    height = image.get_height()

    return pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
