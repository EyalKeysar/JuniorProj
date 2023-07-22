import pygame
from client.Game.GUI.pygame_constants import *

class GameGui():
    def __init__(self):
        # pygame init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def update(self, grid):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        self.draw_grid(grid)
        pygame.display.update()


    def draw_grid(self, grid):
        self.screen.fill(BG_COLOR)
        # Clear the surface
        
        # Iterate over the grid and draw cubes
        for y in range(len(grid)):
            for x in range(len(grid)):
                # Get the color of the current cell=
                # Draw the cube
                self.draw_cell_by_grid(x, y, CELL_COLOR, self.screen)

        # Update the display
        pygame.display.flip()

    def draw_cell_by_grid(self, x, y, color, surface):
        pygame.draw.rect(surface, color, (x * (CELL_SIZE + LINE_WIDTH) + PAD_LEFT, y * (CELL_SIZE + LINE_WIDTH) + PAD_TOP, CELL_SIZE, CELL_SIZE))




if __name__ == "__main__":
    g = GameGui()
    grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    while True:
        g.update(grid)