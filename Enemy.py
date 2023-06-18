from Player import Player
from GameConstants import *

class Enemy(Player):
    def __init__(self, game):
        super().__init__(game)
        self.rect.centerx = game.screen_width / 2
        self.rect.bottom = self.rect.height + HEIGHT_OFFSET
        
    def update(self):
        pass
    
    
     