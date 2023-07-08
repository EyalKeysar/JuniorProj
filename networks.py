
import  sys
from Network.constants import *
sys.path.append("..\\")
from GameConstants import *
import socket
import pygame

def CreateSocket(logger):
    """
        Creates a socket and connects to the server.
        Handshake is performed.
        
        :Returns: socket
    """
    data_from_server = ""
    client_socket = socket.socket()
    client_socket.settimeout(2)

    while data_from_server != SYN_ACK:
        # Pygame maintenance
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        # Try to connect to the server and perform handshake.    
        try:
            client_socket.connect(("127.0.0.2", SERVER_PORT))
            client_socket.send(SYN_REQ.encode())
    
            data_from_server = client_socket.recv(1024).decode()
            
        except Exception as e:
            logger.log(" * Failed To Create Socket \n" + str(e))
            client_socket = socket.socket()
            client_socket.settimeout(0.5)
            continue
    
    logger.log(" * Connection Established")    
    return client_socket

def CheckConnection(client_socket):
    """
        Checks if the connection to the server is still alive.
        Sends a MTN request to the server and checks the response.
    """
    client_socket.send(MAINTAIN_CONNECTION.encode())
    MNTN_recv = client_socket.recv(1024).decode()
    return MNTN_recv == MAINTAIN_OK


def HandelConnectionError(e, logger, client_socket):
    """
        Handels a connection error.
        If the error is a server refresh, a new socket is created.
        Otherwise, the error is logged.
    """
    if(e.errno == 10054 or e.errno == 10056):
        logger.log(" * Server Refresh, Creating another socket")
        client_socket = CreateSocket(logger)
    else:
        logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno) + "\n" + str(e))
    return client_socket
    

def send_active_players(client_socket, active_players, logger):
    """
        Sends the active players to the server.
    """
    try:
        client_socket.send((str(len(active_players)) + str('=')).encode())
        active_players_str = ""
        
        for player in active_players:
            active_players_str += str(player) + str(";")
        logger.log(" * Sending active players: " + active_players_str)
        client_socket.send(active_players_str.encode())

    except Exception as e:
        logger.log(" * Failed to send active players\n" + str(e))
    return client_socket

def get_active_players(client_socket, logger):
    """
        Gets the active players from the server.

    """
    logger.log(" * Getting active players")

    client_socket.send(GET_ACTIVE_PLAYERS.encode())
    players = []
    num_of_players = ""
    cur_char = client_socket.recv(1).decode()

    while cur_char != '=':
        num_of_players += cur_char
        cur_char = client_socket.recv(1).decode()

    num_of_players = int(num_of_players)

    for i in range(num_of_players):
        cur_player = ""
        cur_char = client_socket.recv(1).decode()
        while cur_char != ';':
            cur_player += cur_char
            cur_char = client_socket.recv(1).decode()
        players.append(cur_player)