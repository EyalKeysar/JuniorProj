import pygame
import time
import sys

from client.Game.GUI.gamegui import GameGUI
from client.Game.GUI.player import Player

from client.Game.GUI.pygame_constants import *
from shared.game_constants import *
from shared.ServerAPI.api_constants import *


class Game:
    def __init__(self, serverAPI):
        self.serverAPI = serverAPI

        self.players = []
        self.shoots = []

    def get_players(self, serverAPI):
        self.players = serverAPI.GetPlayers()


    def run(self):
        self.gui = GameGUI()

        while self.gui.is_running:
            
            self.serverAPI.GetUpdates()


            self.players = self.serverAPI.GetPlayers()
            self.shoots = self.serverAPI.GetShoots()


            # self.gui

            # calculate how long to draw the frame for

            self.gui.draw_grid()
            self.gui.draw_players(self.players)
            self.gui.draw_bullets(self.shoots)
  
            self.gui.update()
            for key in self.gui.events:

                if(key == pygame.K_LEFT):
                    self.serverAPI.MovePlayerLeft()
                if(key == pygame.K_RIGHT):
                    self.serverAPI.MovePlayerRight()

                if(key == pygame.K_UP):
                    self.serverAPI.Shoot()
                if(key == pygame.K_DOWN):
                    self.serverAPI.Sheild()
        sys.exit()
        
if __name__ == "__main__":
    game = Game(None)
    game.run()