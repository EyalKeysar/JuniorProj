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
        if(self.in_creation):
            self.connection_status = False
            return False, None
            
        respond, e = client_mtn(self.logger, self.client_socket)

        return respond, e
    
    def IsAuthenticated(self):
        if(self.in_creation):
            return False
        try:
            self.client_socket.send(AUTH_REQUEST.encode())
            respond = self.client_socket.recv(1024).decode()
            return respond == AUTH_TRUE
        
        except Exception as e:
            self.HandelConnectionError(e)
            return False
    
    def MovePlayerLeft(self):
        if(self.in_creation):
            return False
        try:
            self.client_socket.send(MOVE_LEFT.encode())
            respond = self.client_socket.recv(1024).decode()
            return respond
        
        except Exception as e:
            self.HandelConnectionError(e)
            return False
    
    def MovePlayerRight(self):
        if(self.in_creation):
            return False
        try:
            self.client_socket.send(MOVE_RIGHT.encode())
            respond = self.client_socket.recv(1024).decode()
            return respond
        
        except Exception as e:
            self.HandelConnectionError(e)
            return False
    

    def GetUpdates(self):
        if(self.in_creation):
            return False
        try:
            self.client_socket.send(GET_UPDATES.encode())
            respond = self.client_socket.recv(1024).decode()
            return respond
        
        except Exception as e:
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