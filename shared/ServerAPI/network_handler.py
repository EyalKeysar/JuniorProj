import socket
# from shared import net_constants
import threading
from shared.ServerAPI.mtnp import *


class NetworkHandler():
    def __init__(self, logger):
        self.logger = logger
        self.client_socket = None
        self.connection_status = False
        self.in_creation = False
        self.data_from_server = ""
        

    def CreateSocketThreaded(self):
        self.in_creation = True
        threading.Thread(target=self.CreateSocket).start()
    
    def CreateSocket(self):
        self.client_socket = socket.socket()
        self.client_socket.settimeout(0.5)
        self.client_socket = client_handshake(self.logger, self.client_socket)
        self.in_creation = False

    def CheckConnection(self):
        self.logger.log(" * Checking connection...")
        if(self.in_creation):
            self.connection_status = False
            return False
            
        
        respond, e = client_mtn(self.logger, self.client_socket)

        if(respond):
            self.logger.log(" * Connection is alive")
            self.connection_status = True
            return True
        else:
            self.logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno))
            self.connection_status = False
            self.HandelConnectionError(e)

            return False
        
    
    def HandelConnectionError(self, e):
        """
            Handels a connection error.
            If the error is a server refresh, a new socket is created.
            Otherwise, the error is logged.
        """
        if(e.errno == 10054 or e.errno == 10056):
            self.client_socket = self.CreateSocketThreaded()
        else:
            self.logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno) + "\n" + str(e))