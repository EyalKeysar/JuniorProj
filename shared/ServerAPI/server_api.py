
import threading
from shared.ServerAPI.network_handler import NetworkHandler
from shared.ServerAPI.api_constants import *
import time

class ServerAPI:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.network_handler = NetworkHandler(self.logger)
        self.is_authenticated = False

        self.raw_data = ""
        self.raw_players = ""
        self.raw_shoots = ""

    # General
    def Build(self):
        while(self.network_handler.in_creation):
            time.sleep(0.1)
        self.logger.log(" * Building server API")
        self.network_handler.CreateSocketThreaded()

    def CheckConnection(self):
        if(self.network_handler.in_creation):
            time.sleep(0.1)
        
        respond, e = self.network_handler.CheckConnection()
        if(respond):
            self.network_handler.connection_status = True
        else:
            print("therespond = " + str(respond))
            self.logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno))
            self.network_handler.connection_status = False
            self.network_handler.HandelConnectionError(e)

            return False
        

    def GetUpdates(self):
        if(self.network_handler.in_creation):
            time.sleep(0.1)
        
        respond = self.network_handler.GetUpdates()
        if(not respond):
            self.raw_data = ""
            return
        self.raw_data = respond
        
        try:
            self.raw_players = self.raw_data.split("\n")[0]
            if(self.raw_data.split("\n")[1] == "False"):
                self.raw_shoots = ""
            else:
                self.raw_shoots = self.raw_data.split("\n")[1]
        except Exception as e:
            print(e)
            self.raw_players = ""
            self.raw_shoots = ""    
    
    def GetPlayers(self):

        if(self.raw_players == ""):
            return []

        try:
            self.raw_players_split = self.raw_players.split(";")
            players = []
            for player in self.raw_players_split:
                player = player.split(",")
                player[0] = int(player[0])
                player[1] = int(player[1])

                if(player[2] == "0"):
                    player[2] = False
                else:
                    player[2] = True

                
                players.append(player)
        except Exception as e:
            print("PLAYERS" + str(e))
            players = []

        return players

    def GetShoots(self):

        if(self.raw_shoots == ""):
            return []


        try:
            self.raw_shoots_split = self.raw_shoots.split(";")
            shoots = []
            for shoot in self.raw_shoots_split:
                shoot = shoot.split(",")
                shoot[0] = int(shoot[0])
                shoot[1] = int(shoot[1])

                
                shoots.append(shoot)
        except Exception as e:
            print("BULLETS" + str(e))
            shoots = []


        return shoots

    
    def GetConnectionStatus(self):
        return self.network_handler.connection_status

    def Destroy(self):
        pass

    # Sign in
    def Login(self, username, password) -> bool:
        while(self.network_handler.in_creation):
            time.sleep(0.1)
        
        respond = self.network_handler.Login(username, password)
        if(respond):
            self.is_authenticated = True
        else:
            self.is_authenticated = False
        return respond

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
    def MovePlayerLeft(self):
        respond =  self.network_handler.MovePlayerLeft()
        
    def MovePlayerRight(self):
        respond = self.network_handler.MovePlayerRight()

    def Shoot(self):
        respond = self.network_handler.shoot()

            



    def Sheild(self):
        pass

