import socket
from Network.constants import *
from Network.mtnp import *
class NetworkHandler():
    def __init__(self, logger):
        self.logger = logger
        self.client_socket = None
        self.connection_status = False
        self.data_from_server = ""
        
    def CreateSocket(self):
        """
            Creates a socket and connects to the server.
            Handshake is performed.
            
            :Returns: socket
        """
        self.client_socket = socket.socket()
        self.client_socket.settimeout(0.5)

        self.client_socket = client_handshake(self.logger, self.client_socket)

    def CheckConnection(self):
        respond, e = client_mtn(self.logger, self.client_socket)

        if(respond):
            self.connection_status = True
            return True
        else:
            self.HandelConnectionError(e)
            self.connection_status = False
            return False
        
    
    def HandelConnectionError(self, e):
        """
            Handels a connection error.
            If the error is a server refresh, a new socket is created.
            Otherwise, the error is logged.
        """
        if(e.errno == 10054 or e.errno == 10056):
            self.logger.log(" * Server Refresh, Creating another socket")
            self.client_socket = self.CreateSocket()
        else:

            self.logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno) + "\n" + str(e))