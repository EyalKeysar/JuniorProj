import socket
from server.constants import *
import threading
from shared.ServerAPI.mtnp import *

class ServerNetworkHandler:
    def __init__(self, logger):
        self.logger = logger
        self.client_list = []

        self.waiting_for_clients = False

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', SERVER_PORT))



    def run(self):
        self.waiting_for_clients = True
        self.server_socket.listen(1)
        
        client, address = self.server_socket.accept()
        if((client, address) in self.client_list):
            self.client_list.remove((client, address))
            client.close()
            self.waiting_for_clients = False
            return None, None

        server_handshake(client, self.logger, address, self.client_list)
        
        
        self.logger.log(" * Client connected from %s:%d" % (address[0], address[1]))
        self.client_list.append((client, address))
        self.waiting_for_clients = False

        return client, address

                
    def kill(self):
        for thread in self.threads_queue:
            thread.join()
        for client in self.client_queue:
            client.close()

        self.server_socket.close()
        self.logger.log(" * Server stopped running")