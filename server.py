import socket
import threading
import time
import sys
import os
import random
from constants import *
from logger import Logger

class Server:
    def __init__(self, port=SERVER_PORT):
        #set up socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', SERVER_PORT))
        self.logger = Logger()
        
    
    def run(self):
        self.logger.log(" * Server started running")
        self.server_socket.listen(5)
        while True:
            # Wait for a connection
            client, address = self.server_socket.accept()
            self.logger.log(" * Client connected from %s:%d" % (address[0], address[1]))
            # Handle the connection.
            # thread = threading.Thread(target=self.handle_connection, args=(client, address))
            # thread.start()
        
    def kill(self):
        pass
    

Server().run()