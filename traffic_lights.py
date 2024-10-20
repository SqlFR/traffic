import pygame
from colors import Colors


class TrafficLights:
    def __init__(self, position_road, localisation_traffic_lights):
        self.state = 'red'
        self.position_road = position_road
        self.localisation = localisation_traffic_lights

        x, y = self.position_road

        if self.localisation == 'Right':
            self.position_road = x + 70, y + 50
        elif self.localisation == 'Bottom':
            self.position_road = x - 10, y + 70
        elif self.localisation == 'Left':
            self.position_road = x + 10, y - 10
        elif self.localisation == 'Top':
            self.position_road = x + 50, y + 10

    def change_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def draw(self, surface):
        if self.state == 'red':
            color = Colors.RED.value
        elif self.state == 'green':
            color = Colors.GREEN.value
        else:
            color = Colors.ORANGE.value

        # Dessine un cercle représentant le feu de signalisation
        pygame.draw.circle(surface, color, self.position_road, 5)

