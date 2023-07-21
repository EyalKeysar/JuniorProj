from shared.ServerAPI.network_handler import NetworkHandler

class ServerAPI:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.network_handler = NetworkHandler(self.logger)

    # General
    def Build(self):
        self.network_handler.CreateSocketThreaded()

    def CheckConnection(self):
        self.network_handler.CheckConnection()
    
    def GetConnectionStatus(self):
        return self.network_handler.connection_status

    def Destroy(self):
        pass

    # Sign in
    def Login(self, username, password):
        pass

    def Register(self, username, password, mail):
        pass

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
