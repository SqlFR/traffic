import pygame
from colors import Colors
from traffic_lights import TrafficLights


LENGTH = 80  # Définit la longeur de la section route
OFFSET_DASH = 20  # Crée un décalage par apport à la ligne top(horizontal)/gauche(vertical) pour la ligne pointillée
OFFSET_BOTTOM = 40  # Crée un décalage par apport à la ligne top(horizontal)/gauche(vertical) pour la ligne opposée


class RoadSegment:

    def __init__(self, start_pos: tuple, horizontal: bool = True, localisation_traffic_lights: str = None):
        self.start_pos = start_pos
        self.horizontal = horizontal  # Sens de la route
        self.traffic_lights = TrafficLights(start_pos, localisation_traffic_lights) if localisation_traffic_lights else None
        self.length = LENGTH
        self.offset_dash = OFFSET_DASH
        self.offset_bottom = OFFSET_BOTTOM
        self.x_start, self.y_start = self.start_pos
        self.x_end = self.x_start + self.length if horizontal else self.x_start
        self.y_end = self.y_start if horizontal else self.y_start + self.length

    # Definie le positionnement des lignes en ajoutant un décalage à la ligne pointillée et opposée
    def define_position_lines(self, offset):
        return ((self.x_start, self.y_start + offset), (self.x_end, self.y_end + offset)) if self.horizontal \
            else ((self.x_start + offset, self.y_start), (self.x_end + offset, self.y_end))

    # Dessine la section de route avec le feu de traffic si nécessaire
    def draw(self, surface):

        lines = [
            self.define_position_lines(0),  # Top
            self.define_position_lines(self.offset_dash),  # Pointillé
            self.define_position_lines(self.offset_bottom)  # Opposé
        ]

        pygame.draw.line(surface, Colors.WHITE.value, *lines[0], width=3)
        draw_dashed_line(surface, *lines[1])
        pygame.draw.line(surface, Colors.WHITE.value, *lines[2], width=3)

        if self.traffic_lights:
            self.traffic_lights.draw(surface)


# Fonction pour dessiner une ligne pointillée
def draw_dashed_line(surface: pygame.Surface, start_pos: tuple, end_pos: tuple):
    # Calcule le vecteur directionnel entre le point de départ et d'arrivée
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5

    # Normaliser le vecteur directionnel
    dx /= length
    dy /= length

    # Diviser la ligne en segments visibles et invisibles
    dash_step = 10
    dashes = int(length // dash_step)
    for i in range(dashes):
        start_dash_x = x1 + dx * i * dash_step
        start_dash_y = y1 + dy * i * dash_step
        end_dash_x = x1 + dx * (i + 0.5) * dash_step  # Segment visible
        end_dash_y = y1 + dy * (i + 0.5) * dash_step

        # Dessine le segment visible
        pygame.draw.line(surface, Colors.WHITE.value, (start_dash_x, start_dash_y),
                         (end_dash_x, end_dash_y), 3)



