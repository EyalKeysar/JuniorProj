
from shared.game_constants import *


class GameLogic():
    def __init__(self):
        pass

    def move_player_left(self, player):
        if(player.pos[0] - 1 > 0):
            player.pos = [player.pos[0] - 1, player.pos[1]]
            return True 
        return False
    
    def move_player_right(self, player):
        if(player.pos[0] + 1 < GRID_SIZE):
            player.pos = [player.pos[0] + 1, player.pos[1]]
            return True 
        return False
    