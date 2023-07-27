import socket
import threading
import time
import sys
import os
import random

from server.server_network_handler import ServerNetworkHandler
from server.Game.player import Player
from server.Game.game_logic import GameLogic
from server.client import Client

from shared.logger import Logger
from shared.ServerAPI.api_constants import *
from shared.game_constants import *
# from shared.ServerAPI.mtnp import *


class Server:
    def __init__(self, port=SERVER_PORT):
        self.network_handler = ServerNetworkHandler()

        self.client_list = []

        self.game_logic = GameLogic()


    def run(self):
        while True:

            if(len(self.client_list) != 0):
                # print(self.client_list)
                pass
            if(not self.network_handler.waiting_for_clients):
                accept_thread = threading.Thread(target=self.network_handler.run, args=(self.client_list,))
                
                accept_thread.start()

            self.game_logic.update()
            self.handle_clients()
        
    
    def handle_clients(self):
        for client in self.client_list:
            try:
                data = client.GetSocket().recv(1024)
            except Exception as e:
                self.handle_error(e, client)
                for current_client in self.client_list:
                    if(current_client.GetAddress()[0] == client.GetAddress()[0]):
                        self.client_list.remove(current_client)
                client.GetSocket().close()
                continue 
            
            data = data.decode()

            # network
            if(data == MAINTAIN_CONNECTION):
                print("maintain connection $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")
                client.send(MAINTAIN_OK.encode())
            if(data == AUTH_REQUEST):
                pass


            # game
            if(data == MOVE_LEFT):
                respond = self.game_logic.move_player_left(self.game_logic.players[0])
            if(data == MOVE_RIGHT):
                respond = self.game_logic.move_player_right(self.game_logic.players[0])
            if(data == SHOOT):
                self.game_logic.shoot(self.game_logic.players[0])


            if(data == GET_UPDATES):
                respond = str(self.game_logic.players[0].pos[0]) + ',' + str(self.game_logic.players[0].pos[1]) + ',' + str(1) + ';'
                respond += str(self.game_logic.players[1].pos[0]) + ',' + str(self.game_logic.players[1].pos[1]) + ',' + str(0)
                respond += '\n'
                for bullet in self.game_logic.bullets:
                    respond += str(bullet.pos[0]) + ',' + str(bullet.pos[1]) + ',' + str(bullet.speed) + ';'
                if(len(self.game_logic.bullets) == 0):
                    respond += 'False;'


                client.GetSocket().send(respond[:-1].encode())
                
    def is_authenticated(self, client):
        client.GetSocket().send(AUTH_TRUE.encode())
        return True
    
    def handle_error(self, e, client):
        print("in error " + str(e))
        if(e.errno == 10038):
            data = None
        elif(e.errno == 10054 or e.errno == 10056):
            for current_client in self.client_list:
                if(current_client.GetAddress()[0] == client.GetAddress()[0]):
                    self.client_list.remove(current_client)
            client.close()

            return
        else:
            raise e
Server().run()