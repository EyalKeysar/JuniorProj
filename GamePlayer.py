
import pygame
from Player import Player
from GameConstants import *
import os

class GamePlayer(Player):
    def __init__(self, game):
        super().__init__(game)
        self.rect.centerx = game.screen_width / 2
        self.rect.bottom = game.screen_height - HEIGHT_OFFSET
        
    def update(self):
        # Get the current key presses
        keys = pygame.key.get_pressed()

        # Move the player left if the left arrow key is pressed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        # Move the player right if the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        super().update()
            
        