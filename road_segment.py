import pygame
from colors import Colors
from traffic_light import TrafficLight


LENGTH = 80  # Définit la longeur de la route
OFFSET_DASH = 20  # Crée un décalage pour la ligne pointillée
OFFSET_BOTTOM = 40  # Crée un décalage pour la ligne du bas


class RoadSegment:

    def __init__(self, start_pos: tuple, horizontal: bool = True, has_traffic_lights: bool = False):
        self.start_pos = start_pos
        self.horizontal = horizontal
        self.has_traffic_lights = has_traffic_lights
        self.traffic_light = None
        self.length = LENGTH
        self.offset_dash = OFFSET_DASH
        self.offset_bottom = OFFSET_BOTTOM

        if self.has_traffic_lights:
            self.traffic_light = TrafficLight()

    def define_pos_top_line(self):
        x_start, y_start = self.start_pos

        if self.horizontal:
            x_end, y_end = x_start + self.length, y_start
            pos_top_line = (x_start, y_start), (x_end, y_end)
        else:
            x_end, y_end = x_start, y_start + self.length
            pos_top_line = (x_start, y_start), (x_end, y_end)

        return pos_top_line

    def define_pos_dash_line(self):
        x_start, y_start = self.start_pos

        if self.horizontal:
            x_end, y_end = x_start + self.length, y_start
            pos_dash_line = (x_start, y_start + self.offset_dash), (x_end, y_end + self.offset_dash)
        else:
            x_end, y_end = x_start, y_start + self.length
            pos_dash_line = (x_start + self.offset_dash, y_start), (x_end + self.offset_dash, y_end)

        return pos_dash_line

    def define_pos_lines(self):

        x_start, y_start = self.start_pos

        # Si la route est horizontale
        if self.horizontal:
            x_end, y_end = x_start + self.length, y_start

            # Définir les positions pour les trois lignes
            pos_bottom_line = (x_start, y_start + self.offset_bottom), (x_end, y_end + self.offset_bottom)
        # Si la route est verticale
        else:
            x_end, y_end = x_start, y_start + self.length

            # Définir les positions pour les trois lignes
            pos_bottom_line = (x_start + self.offset_bottom, y_start), (x_end + self.offset_bottom, y_end)

        return pos_bottom_line, x_end, y_end

    def draw(self, surface):

        pos_bottom_line, x_end, y_end = self.define_pos_lines()
        pos_top_line = self.define_pos_top_line()
        pos_dash_line = self.define_pos_dash_line()

        if self.traffic_light:
            self.traffic_light.draw(surface, (x_end - 5, y_end + 50))

        # Dessiner les lignes
        pygame.draw.line(surface, Colors.WHITE.value, *pos_top_line, width=3)
        draw_dashed_line(surface, *pos_dash_line)
        pygame.draw.line(surface, Colors.WHITE.value, *pos_bottom_line, width=3)


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



