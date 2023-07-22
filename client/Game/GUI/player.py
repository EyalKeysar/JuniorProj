import pygame

from client.Game.GUI.simplegui import draw_cell_by_grid
from client.Game.GUI.pygame_constants import *

class Player:
    def __init__(self):
        self.pos = [70, 70]
        self.sprite = PLAYER_SPRITE
        self.sprite_size = PLAYER_SPRITE_SIZE

    def draw(self, screen):
        start_x = self.pos[0]
        start_y = self.pos[1]

        for i in range(self.sprite_size[1]):
            for j in range(self.sprite_size[0]):
                if self.sprite[i*self.sprite_size[0] + j] == 1:
                    draw_cell_by_grid(screen, (start_x + j, start_y + i), (255, 0, 255))