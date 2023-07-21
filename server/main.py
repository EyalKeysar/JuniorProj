import socket
import threading
import time
import sys
import os
import random

from server.server_network_handler import ServerNetworkHandler

from shared.logger import Logger
from shared.ServerAPI.mtnp_constants import *

class Server:
    def __init__(self, port=SERVER_PORT):
        self.client_list = []
        self.logger = Logger()
        self.network_handler = ServerNetworkHandler(self.logger, self.client_list)

    def run(self):
        self.network_handler.run()
    
    

Server().run()