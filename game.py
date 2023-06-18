import pygame
from GameConstants import *
from GamePlayer import GamePlayer
from Enemy import Enemy
from Player import Player
import sys

class Game:
    def __init__(self):
        
        # self.username = username
        
        pygame.init()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(SCREEN_TITLE)  # "Space Invaders"
        self.clock = pygame.time.Clock()
        
        self.player = GamePlayer(self)
        self.enemy = Enemy(self)
        
        
    def run(self):
        while True:
            # Get the current framerate
            fps = self.clock.tick(60)

            # Update the player ship
            self.player.update()
            self.enemy.update()


            # Draw the screen
            self.screen.fill((0, 0, 0))
            self.player.draw()
            self.enemy.draw()

            # Update the display
            pygame.display.update()

            # Check for the user closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return
                    
    
    
# Game().run()