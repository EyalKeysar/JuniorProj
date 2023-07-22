
import threading
from shared.ServerAPI.network_handler import NetworkHandler

class ServerAPI:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.network_handler = NetworkHandler(self.logger)
        self.is_authenticated = False

    # General
    def Build(self):
        self.network_handler.CreateSocketThreaded()

    def CheckConnection(self):
        if(self.network_handler.in_creation):
            return False
        
        respond, e = self.network_handler.CheckConnection()
        if(respond):
            self.logger.log(" * Connection is alive")
            self.network_handler.connection_status = True
            
        else:
            self.logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno))
            self.network_handler.connection_status = False
            self.network_handler.HandelConnectionError(e)

            return False

    
    def GetConnectionStatus(self):
        return self.network_handler.connection_status

    def Destroy(self):
        pass

    # Sign in
    def Login(self, username, password) -> bool:
        pass

    def Register(self, username, password, mail):
        pass

    def IsAuthenticated(self):
        respond = self.network_handler.IsAuthenticated()
        self.is_authenticated = respond
        return respond

    # Lobby
    def GetRooms(self):
        pass

    def JoinRoom(self):
        pass

    def CreateRoom(self):
        pass

    # Game
    def UpdateGame(self):
        pass
