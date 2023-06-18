
import pygame
import os
from GameConstants import *

class Player:
    def __init__(self, game):
        self.game = game
        
        self.sprite = pygame.image.load(os.path.join("Assets", "player.png"))
        self.sprite = pygame.transform.scale(self.sprite, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.sprite.get_rect()
        self.rect.width = PLAYER_SIZE
        self.rect.height = PLAYER_SIZE
        
        self.speed = 10
        
    def update(self):
        if(self.rect.x < 0):
            self.rect.x = 0
        elif(self.rect.x > self.game.screen_width - self.rect.width):
            self.rect.x = self.game.screen_width - self.rect.width
        
        #self.rect.x 

    def draw(self):
        # Draw the player image on the screen
        self.game.screen.blit(self.sprite, self.rect)