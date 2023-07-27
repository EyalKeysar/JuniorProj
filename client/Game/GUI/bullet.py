
from client.Game.GUI.simplegui import draw_cell_by_grid
from client.Game.GUI.pygame_constants import *
from shared.game_constants import *

class Bullet():
    def __init__(self, x, y):
        self.pos = [x, y]
        self.sprite = BULLET_SPRITE
        self.sprite_size = BULLET_SPRITE_SIZE

    def draw(self, screen):
        start_x = self.pos[0]
        start_y = self.pos[1]

        for i in range(self.sprite_size[1]):
            for j in range(self.sprite_size[0]):
                if self.sprite[i*self.sprite_size[0] + j] == 1:
                    draw_cell_by_grid(screen, (start_x + j, start_y + i), BULLET_COLOR)
    
    def draw_
