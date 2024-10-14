import pygame
from colors import Colors
from traffic_light import TrafficLight


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


class RoadSegment:

    def __init__(self, start_pos: tuple, horizontal: bool = True, has_traffic_lights: bool = False):
        self.start_pos = start_pos
        self.horizontal = horizontal
        self.has_traffic_lights = has_traffic_lights
        self.traffic_light = None

        if self.has_traffic_lights:
            self.traffic_light = TrafficLight()

    def draw(self, surface):
        x_start, y_start = self.start_pos

        # Définit la longueur par défaut du bloc de route à 80 pixels
        length = 80

        # Crée des décalages pour les lignes pointillées et les lignes du bas
        offset_dash = 20
        offset_bottom = 40

        # Si la route est horizontale
        if self.horizontal:
            x_end, y_end = x_start + length, y_start

            # Définir les positions pour les trois lignes
            pos_top_line = (x_start, y_start), (x_end, y_end)
            pos_dash_line = (x_start, y_start + offset_dash), (x_end, y_end + offset_dash)
            pos_bottom_line = (x_start, y_start + offset_bottom), (x_end, y_end + offset_bottom)
        # Si la route est verticale
        else:
            x_end, y_end = x_start, y_start + length

            # Définir les positions pour les trois lignes
            pos_top_line = (x_start, y_start), (x_end, y_end)
            pos_dash_line = (x_start + offset_dash, y_start), (x_end + offset_dash, y_end)
            pos_bottom_line = (x_start + offset_bottom, y_start), (x_end + offset_bottom, y_end)

        if self.traffic_light:
            self.traffic_light.draw(surface, (x_end - 5, y_end + 50))

        # Dessiner les lignes
        pygame.draw.line(surface, Colors.WHITE.value, *pos_top_line, width=3)
        draw_dashed_line(surface, *pos_dash_line)
        pygame.draw.line(surface, Colors.WHITE.value, *pos_bottom_line, width=3)





