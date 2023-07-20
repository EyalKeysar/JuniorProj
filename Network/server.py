import socket
import threading
import time
import sys
import os
import random
from constants import *
sys.path.append('../')
from networks import *
from logger import Logger
from server_network_handler import ServerNetworkHandler


class Server:
    def __init__(self, port=SERVER_PORT):
        self.client_list = []
        self.logger = Logger()
        self.network_handler = ServerNetworkHandler(self.logger, self.client_list)

    def run(self):
        self.network_handler.run()

    # def run(self):
    #     self.is_running = True
    #     self.logger.log(" * Server started running")
    #     self.server_socket.listen(1)
        
    #     while self.is_running:
    #         # Wait for a connection
    #         client, address = self.server_socket.accept()
    #         self.logger.log(" * Client connected from %s:%d" % (address[0], address[1]))
    #         self.client_queue.append(client)
    #         self.active_players.append(address[0])
            
    #         # Handle the connection.
    #         client_thread = threading.Thread(target=self.handle_connection, args=(client, address))
            
    #         try:
    #             client_thread.start()
    #             self.threads_queue.append(client_thread)
    #         except Exception as e:
    #             self.logger.log(" * Failed to run thread \n" + str(e))
        
    
        
        
    #     # Handshake successful, start game.
                
    #     while True:
    #         try:
    #             data = client.recv(1024)
    #             if not data:
    #                 self.logger.log(" * Client disconnected from %s:%d" % (address[0], address[1]))
    #                 # self.client_queue.remove(client)
    #                 self.active_players.remove(address[0])
    #                 self.threads_queue.remove(threading.current_thread())
    #                 return
    #             if(data.decode() == MAINTAIN_CONNECTION):
    #                 self.logger.log(" * Client requested MTN")
    #                 client.send(MAINTAIN_OK.encode())
    #             elif(data.decode() == GET_ACTIVE_PLAYERS):
    #                 send_active_players(client, self.active_players, self.logger)

    #         except Exception as e:
    #             self.logger.log(" * Client disconnected from %s:%d\n Internal exception raised: %s" % (address[0], address[1], e))
    #             # self.client_queue.remove(client)
    #             self.active_players.remove(address[0])
    #             self.threads_queue.remove(threading.current_thread())
    #             return
            
    
    

Server().run()