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
        self.logger = Logger()
        self.network_handler = ServerNetworkHandler()


        self.player = Player(PLAYER_START_POS)

        self.client_list = []

        self.game_logic = GameLogic()


    def run(self):
        while True:
            if(len(self.client_list) != 0):
                print(self.client_list)
            if(not self.network_handler.waiting_for_clients):
                accept_thread = threading.Thread(target=self.network_handler.run, args=(self.client_list,))
                
                accept_thread.start()
            
            self.handle_clients()
        
    
    def handle_clients(self):
        for client in self.client_list:
            try:
                data = client.GetSocket().recv(1024)
            except Exception as e:
                self.handle_error(e, client)
                for current_client in self.client_list:
                    if(current_client.GetAddress[0] == client.GetAddress[0]):
                        self.client_list.remove(current_client)
                client.GetSocket().close()
                continue
            
            data = data.decode()

            print(data)

            # network
            if(data == MAINTAIN_CONNECTION):
                print("maintain connection $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")
                client.send(MAINTAIN_OK.encode())
            if(data == AUTH_REQUEST):
                pass


            # game
            if(data == MOVE_LEFT):
                respond = self.game_logic.move_player_left(self.player)
                if(respond):
                    client.GetSocket().send((str(self.player.pos[0]) + ',' + str(self.player.pos[1])).encode())
            if(data == MOVE_RIGHT):
                respond = self.game_logic.move_player_right(self.player)
                if(respond):
                    client.GetSocket().send((str(self.player.pos[0]) + ',' + str(self.player.pos[1])).encode())
                
                
    def is_authenticated(self, client):
        client.GetSocket().send(AUTH_TRUE.encode())
        return True
    
    def handle_error(self, e, client):
        print("in error " + str(e))
        if(e.errno == 10038):
            data = None
        elif(e.errno == 10054 or e.errno == 10056):
            for current_client in self.client_list:
                if(current_client.GetAddress[0] == client.GetAddress[0]):
                    self.client_list.remove(current_client)
            client.close()

            return
        else:
            raise e
Server().run()