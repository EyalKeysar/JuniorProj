import pygame
from client.Game.GUI.pygame_constants import *

def draw_cell_by_grid(screen, grid, color):
    x = grid[0] * (CELL_SIZE + LINE_WIDTH) + PAD_LEFT
    y = grid[1] * (CELL_SIZE + LINE_WIDTH) + PAD_TOP
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
