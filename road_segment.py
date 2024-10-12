import pygame


WHITE_COLOR = (255, 255, 255)


# Fonction pour dessiner une ligne pointillée
def draw_dashed_line(surface: pygame.Surface, start_pos: tuple, end_pos: tuple,
                     width: int = 3, dash_length: int = 5):
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
    dash_step = dash_length
    dashes = int(length // dash_step)
    for i in range(dashes):
        start_dash_x = x1 + dx * i * dash_step
        start_dash_y = y1 + dy * i * dash_step
        end_dash_x = x1 + dx * (i + 0.5) * dash_step  # Segment visible
        end_dash_y = y1 + dy * (i + 0.5) * dash_step

        # Dessine le segment visible
        pygame.draw.line(surface, WHITE_COLOR, (start_dash_x, start_dash_y), (end_dash_x, end_dash_y), width)


class RoadSegment:

    def __init__(self, start_pos: tuple, horizontal: bool = True):
        self.start_pos = start_pos
        self.horizontal = horizontal

    def draw(self, surface):

        x_start_pos_all_lines, y_start_top_line = self.start_pos

        # Définit longeur du bloc de route par défault de 80 pixels
        x_end_pos, y_end_pos = (self.start_pos[0] + 80, self.start_pos[1])

        # Définit la position de la ligne pointillée par apport à la top line
        y_start_pos_dash_line = y_start_top_line + 20
        y_end_pos_dash_line = y_end_pos + 20

        # Définit la position de la ligne bottom par apport à la top line
        y_start_pos_bottom_line = y_start_top_line + 40
        y_end_pos_bottom_line = y_end_pos + 40

        pygame.draw.line(surface, WHITE_COLOR, (x_start_pos_all_lines, y_start_top_line),
                         (x_end_pos, y_end_pos), 3)
        draw_dashed_line(surface, (x_start_pos_all_lines, y_start_pos_dash_line),
                         (x_end_pos, y_end_pos_dash_line))
        pygame.draw.line(surface, WHITE_COLOR, (x_start_pos_all_lines, y_start_pos_bottom_line),
                         (x_end_pos, y_end_pos_bottom_line), 3)


# def draw_dashed_line_test(start_pos: tuple, end_pos: tuple):
#     # Calcule le vecteur directionnel entre le point de départ et d'arrivée
#     x1, y1 = start_pos
#     x2, y2 = end_pos
#     dx = x2 - x1
#     dy = y2 - y1
#     print(dy ** 2)
#     length = (dx ** 2 + dy ** 2) ** 0.5
#
#     print('dx: ', dx)
#     print('dy: ', dy)
#     print('length: ', length)
#
#
# draw_dashed_line_test((50, 10), (50, 100))
