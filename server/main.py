import socket
import threading
import time
import sys
import os
import random

from server.server_network_handler import ServerNetworkHandler

from shared.logger import Logger
from shared.ServerAPI.api_constants import *
from shared.ServerAPI.mtnp import *

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
            # print("c l = " + str(self.network_handler.client_list))
    
    def handle_clients(self):

        for (client, address) in self.network_handler.client_list:
            try:
                data = client.recv(1024)
            except Exception as e:
                if(e.errno == 10038):
                    data = None
                elif(e.errno == 10054 or e.errno == 10056):
                    if((client, address) in self.network_handler.client_list):
                        self.network_handler.client_list.remove((client, address))
                    client.close()
                    return
                else:
                    raise e
                
            if not data:
                self.logger.log(" * Client didnt send thing? from %s:%d" % (address[0], address[1]))
                if((client, address) in self.network_handler.client_list):
                    self.network_handler.client_list.remove((client, address))  
                client.close()
                return
            
            else:
                data = data.decode()
                server_mtn(data, client, self.logger)
                
                if(data == AUTH_REQUEST):
                    return self.is_authenticated(client)
                
    def is_authenticated(self, client):
        client.send(AUTH_TRUE.encode())
        return True
    

Server().run()