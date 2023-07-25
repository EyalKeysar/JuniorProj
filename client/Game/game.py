import pygame
import sys

from client.Game.GUI.gamegui import GameGUI
from client.Game.GUI.player import Player

from client.Game.GUI.pygame_constants import *
from shared.game_constants import *
from shared.ServerAPI.api_constants import *


class Game:
    def __init__(self, serverAPI):
        self.serverAPI = serverAPI
        self.gui = GameGUI()

        self.players = []
        self.players.append(Player(PLAYER_START_POS))
        self.players.append(Player(PLAYER_START_POS))

    def get_players(self, serverAPI):
        self.players = serverAPI.GetPlayers()


    def run(self):
        while self.gui.is_running:

            self.gui.draw_grid()

            for player in self.players:
                player.draw(self.gui.screen)
  
            self.gui.update()
            for key in self.gui.events:
                if(key == pygame.K_LEFT):
                    respond = self.serverAPI.MovePlayerLeft()
                    if(respond != False):
                        self.players[0].pos = respond
                if(key == pygame.K_RIGHT):
                    respond = self.serverAPI.MovePlayerRight()
                    if(respond != False):
                        self.players[0].pos = respond
                if(key == pygame.K_UP):
                    self.serverAPI.Shoot()
                if(key == pygame.K_DOWN):
                    self.serverAPI.Sheild()
        sys.exit()
        
if __name__ == "__main__":
    game = Game(None)
    game.run()