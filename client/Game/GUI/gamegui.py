import pygame

from client.Game.GUI.pygame_constants import *
from shared.game_constants import *
from client.Game.GUI.simplegui import draw_cell_by_grid

class GameGUI:
    def __init__(self):
        pygame.init()
        self.pygame = pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.events =[]
    
    def draw_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                draw_cell_by_grid(self.screen, (i, j), CELL_COLOR)

    def update(self):
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if(event.type == pygame.KEYDOWN):
                self.events.append(event.key)
            if(event.type == pygame.KEYUP):
                if(event.key in self.events):
                    self.events.remove(event.key)

        

    def getEvents(self):
        return pygame.event.get()