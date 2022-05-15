import pygame
import random

pygame.font.init()

s_width = 800
s_height =700
play_width = 300
play_height = 600
top_left_x = (s_width - play_width)//2
top_left_y = (s_height - play_height)

shapeO_1 = [[1, 1],
            [1, 1]]

shapeO_2 = [[1, 1],
            [1, 1]]

shapeO_3 = [[1, 1],
            [1, 1]]

shapeO_4 = [[1, 1],
            [1, 1]]
O = [
    shapeO_1, shapeO_2, shapeO_3, shapeO_4
]


shapeI_1 = [[2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]]

shapeI_2 = [[2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

shapeI_3 = [[2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]]

shapeI_4 = [[2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

I = [
    shapeI_1, shapeI_2, shapeI_3, shapeI_4
]
shapeS_1 = [[0, 3, 3],
            [3, 3, 0],
            [0, 0, 0]]

shapeS_2 = [[3, 0, 0],
            [3, 3, 0],
            [0, 3, 0]]

shapeS_3 = [[0, 3, 3],
            [3, 3, 0],
            [0, 0, 0]]

shapeS_4 = [[3, 0, 0],
            [3, 3, 0],
            [0, 3, 0]]

S = [
    shapeS_1, shapeS_2, shapeS_3, shapeS_4
]
shapeZ_1 = [[4, 4, 0],
            [0, 4, 4],
            [0, 0, 0]]

shapeZ_2 = [[0, 4, 0],
            [4, 4, 0],
            [4, 0, 0]]

shapeZ_3 = [[4, 4, 0],
            [0, 4, 4],
            [0, 0, 0]]

shapeZ_4 = [[0, 4, 0],
            [4, 4, 0],
            [4, 0, 0]]

Z = [
    shapeZ_1, shapeZ_2, shapeZ_3, shapeZ_4
]
shapeL_1 = [[5, 0, 0],
            [5, 0, 0],
            [5, 5, 0]]

shapeL_2 = [[5, 5, 5],
            [5, 0, 0],
            [0, 0, 0]]

shapeL_3 = [[5, 5, 0],
            [0, 5, 0],
            [0, 5, 0]]

shapeL_4 = [[0, 0, 5],
            [5, 5, 5],
            [0, 0, 0]]

L = [
    shapeL_1, shapeL_2, shapeL_3, shapeL_4
]
shapeJ_1 = [[0, 6, 0],
            [0, 6, 0],
            [6, 6, 0]]

shapeJ_2 = [[6, 0, 0],
            [6, 6, 6],
            [0, 0, 0]]

shapeJ_3 = [[6, 6, 0],
            [6, 0, 0],
            [6, 0, 0]]

shapeJ_4 = [[6, 6, 6],
            [6, 0, 0],
            [0, 0, 0]]

J = [
    shapeJ_1, shapeJ_2, shapeJ_3, shapeJ_4
]
shapeT_1 = [[7, 7, 7],
            [0, 1, 0],
            [0, 0, 0]]

shapeT_2 = [[0, 7, 0],
            [7, 7, 0],
            [0, 7, 0]]

shapeT_3 = [[0, 7, 0],
            [7, 7, 7],
            [0, 0, 0]]

shapeT_4 = [[7, 0, 0],
            [7, 7, 0],
            [7, 0, 0]]

T = [
    shapeT_1, shapeT_2, shapeT_3, shapeT_4
]

shapes = [O, I, S, Z, L, J, T]
shape_colors = [
(255, 250, 0),
(90, 210, 230),
(0, 255, 0),
(255, 0, 0),
(255, 150, 0),
(0, 0, 255),
(180, 0, 255)
]

class Piece(object):
    def __init__(self, x, y, shape):
        self.shape = shape
        self.rotation = 0
        self.color = shape_colors[shapes.index(shape)]
        self.x = x
        self.y = y

def create_grid(locked_positions={}):
    grid = [[0 for column in range(10)] for row in range(20)]
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return Piece(5, 0, random.choice(shapes))

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label,(
                 (top_left_x + play_width/2) - (label.get_width()/2),
                 (top_left_y + play_width/2) - (label.get_height()/2)))

def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 60, bold=True)
    label = font.render("Next Shape", 10, (255, 255, 255))

    surface.blit(label,
                 (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

def draw_window( surface, grid):
    surface.fill((0, 0, 0))
    font = pygame.font.SysFont("comicsans", 60, bold=True)
    label = font.render("TETRIS", 60, (255, 255, 255))

    surface.blit(label,
        (top_left_x + play_width/2 - (label.get_width()/2), 30))

    pygame.draw.rect(surface,
                     (255, 0, 0),
                     (top_left_x, top_left_y, play_width, play_height),
                     5)


def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_shape = get_shape()
    next_shape = get_shape()
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        draw_window(win, grid)
        draw_next_shape(next_shape, win)
        pygame.display.update()


def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle("Press any key to start", 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main(win)




window = pygame.display.set_mode((s_width, s_height))
main_menu(window)