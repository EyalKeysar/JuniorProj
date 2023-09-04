import socket
import time
# from shared import net_constants
import threading
from shared.ServerAPI.api_constants import *


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

        # handshake
        try:
            self.client_socket.connect((SERVER_IP, SERVER_PORT))
            self.connection_status = True
            self.logger.log(" * Connected to server")
            

        self.in_creation = False

    def CheckConnection(self):
        if(self.in_creation):
            print("currently in creation canot check connection")
            self.connection_status = False
            return False, None
            
        respond, e = client_mtn(self.logger, self.client_socket)

        return respond, e
    

    def Login(self, username, password):
        if(self.in_creation):
            return False
        
        self.in_creation = True
        try:
            login_request = LOGIN_REQUEST + "\n" + username + ";" + password
            self.client_socket.send(login_request.encode())
            respond = self.client_socket.recv(1024).decode()
            self.in_creation = False
            return respond == LOGIN_TRUE
        except Exception as e:
            self.HandelConnectionError(e)
            self.in_creation = False
            return False

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
        
        self.in_creation = True
        try:
            self.client_socket.send(MOVE_LEFT.encode())
            print(end='')
            self.in_creation = False
            return
        
        except Exception as e:
            self.HandelConnectionError(e)
            self.in_creation = False
            return False
    
    def MovePlayerRight(self):

        if(self.in_creation):
            return False

        try:
            self.client_socket.send(MOVE_RIGHT.encode())
            print(end='')
            return
        
        except Exception as e:
            print("Error from MovePlayerRight")
            self.HandelConnectionError(e)
            return False
    

    def GetUpdates(self):
        try:
            self.client_socket.send(GET_UPDATES.encode())
            self.client_socket.settimeout(None)
            respond = self.client_socket.recv(1024).decode()
            self.client_socket.settimeout(0.5)
            return respond
        
        except Exception as e:
            print("Error from GetUpdates")
            self.HandelConnectionError(e)
            return False
        
    def shoot(self):
        if(self.in_creation):
            return False
        try:
            self.client_socket.send(SHOOT.encode())
            return True
        
        except Exception as e:
            print("Error from shoot")
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
            self.logger.log(" * Error Handeling\nerrno:" + str(e.errno) + "\n" + str(e))