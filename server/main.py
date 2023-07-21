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
    
    

Server().run()