
from shared.game_constants import *
from server.Game.player import Player
from server.Game.bullet import Bullet
from server.Game.normal_bullet import CommonBullet

class GameLogic():
    def __init__(self):
        self.players = []
        self.bullets = []

        self.players.append(Player([0, GRID_SIZE - PLAYER_SPRITE_SIZE[1]], 1))
        self.players.append(Player([GRID_SIZE - PLAYER_SPRITE_SIZE[0], 0], 2))

        self.bullets.append(CommonBullet([0, 0], 1))

    def update(self):
        for bullet in self.bullets:
            if(bullet.pos[1] >= GRID_SIZE - BULLET_SPRITE_SIZE[1] or bullet.pos[1] <= 0):
                self.bullets.remove(bullet)
                continue

            bullet.update()

    def move_player_left(self, player):
        if(player.pos[0] - 1 >= 0):
            player.pos = [player.pos[0] - 1, player.pos[1]]
            return True 
        return False
    
    def move_player_right(self, player):
        if(player.pos[0] + 1 <= GRID_SIZE - PLAYER_SPRITE_SIZE[0]):
            player.pos = [player.pos[0] + 1, player.pos[1]]
            return True 
        return False
    
    def shoot(self, player):
        self.bullets.append(CommonBullet([player.pos[0], player.pos[1]], -1))
    