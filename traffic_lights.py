import pygame
from colors import Colors


class TrafficLights:
    def __init__(self, position, state='red'):
        self.state = state
        self.position = position

        self.image_red_light = pygame.image.load('images/red_light.png').convert_alpha()
        self.image_orange_light = pygame.image.load('images/orange_light.png').convert_alpha()
        self.image_green_light = pygame.image.load('images/green_light.png').convert_alpha()

    def change_state(self, new_state):
        self.state = new_state

    def red_light(self):
        self.change_state('red')

    def orange_light(self):
        self.change_state('orange')

    def green_light(self):
        self.change_state('green')

    def get_state(self):
        return self.state

    def draw(self, surface):
        if self.state == 'red':
            surface.blit(scale_image(self.image_red_light, 0.05), self.position)
        elif self.state == 'orange':
            surface.blit(scale_image(self.image_orange_light, 0.05), self.position)
        elif self.state == 'green':
            surface.blit(scale_image(self.image_green_light, 0.05), self.position)


# modifier la taille de l'image
def scale_image(image, scale) -> pygame.Surface:
    width = image.get_width()
    height = image.get_height()

    return pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
