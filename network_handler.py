import socket
from Network.constants import *
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
        data_from_server = ""
        self.client_socket = socket.socket()
        self.client_socket.settimeout(0.5)

        if(self.data_from_server != SYN_ACK):
            # Try to connect to the server and perform handshake.    
            try:
                self.client_socket.connect((SERVER_IP, SERVER_PORT))
                self.client_socket.send(SYN_REQ.encode())
        
                self.data_from_server = self.client_socket.recv(1024).decode()
                
            except Exception as e:
                self.logger.log(" * Failed To Create Socket \n" + str(e))
                self.client_socket = socket.socket()
                self.client_socket.settimeout(0.5)

    def CheckConnection(self):
        """
            Checks if the connection to the server is still alive.
            Sends a MTN request to the server and checks the response.
        """
        try:
            self.client_socket.send(MAINTAIN_CONNECTION.encode())
            MNTN_recv = self.client_socket.recv(1024).decode()
            self.connection_status = MNTN_recv == MAINTAIN_OK
        except Exception as e:
            self.HandelConnectionError(e)
            self.connection_status = False
    
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