import socket
import threading
import time
import sys
import os
import random

from server.server_network_handler import ServerNetworkHandler

from shared.logger import Logger
from shared.ServerAPI.api_constants import *
# from shared.ServerAPI.mtnp import *


class Server:
    def __init__(self, port=SERVER_PORT):
        self.logger = Logger()
        self.network_handler = ServerNetworkHandler(self.logger)

    def run(self):
        while True:
            if(not self.network_handler.waiting_for_clients):
                accept_thread = threading.Thread(target=self.network_handler.run)
                accept_thread.start()
            self.handle_clients()
    
    def handle_clients(self):
        for (client, address) in self.network_handler.client_list:
            try:
                data = client.recv(1024)
            except Exception as e:
                self.handle_error(e, client, address)
                if((client, address) in self.network_handler.client_list):
                    self.network_handler.client_list.remove((client, address))  
                client.close()
                continue
            
            data = data.decode()

            print(data)

            if(data == MAINTAIN_CONNECTION):
                client.send(MAINTAIN_OK.encode())
            if(data == AUTH_REQUEST):
                pass
                
    def is_authenticated(self, client):
        client.send(AUTH_TRUE.encode())
        return True
    
    def handle_error(self, e, client, address):
        print("in error")
        if(e.errno == 10038):
            data = None
        elif(e.errno == 10054 or e.errno == 10056):
            if((client, address) in self.network_handler.client_list):
                self.network_handler.client_list.remove((client, address))
            client.close()
            return
        else:
            raise e

Server().run()