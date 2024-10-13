import pygame
from colors import Colors


class TrafficLight:
    def __init__(self):
        self.state = 'red'

    def change_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def draw(self, surface, position):

        if self.state == 'red':
            color = Colors.RED.value
        elif self.state == 'green':
            color = Colors.GREEN.value
        else:
            color = Colors.ORANGE.value

        # Dessine un cercle représentant le feu de signalisation
        pygame.draw.circle(surface, color, position, 10)
