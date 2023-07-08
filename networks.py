
from GameConstants import *
import socket
import pygame
from Network.constants import *
import sys

def CreateSocket(logger):
    """
        Creates a socket and connects to the server.
        Handshake is performed.
        
        :Returns: socket
    """
    data_from_server = ""
    client_socket = socket.socket()
    client_socket.settimeout(0.5)

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
    