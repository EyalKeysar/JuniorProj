import pygame
import sys
import os
import time
import socket
from GameConstants import *
from logger import Logger
from Network.constants import *
from game import Game
from draws import *
from networks import *




def main():
    logger =  Logger() 
    logger.log(" * Starting game")
    
    # Initializition
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()

    draw_opening_screen(screen, False)
    
    client_socket = CreateSocket(logger)
            
    logger.log("Connected to server")

    is_connected = True
    
    while True:
        logger.log(" * Waiting in maintenance mode")
        try:
            client_socket.send("MTN".encode())
            MNTN_recv = client_socket.recv(1024).decode()
            is_connected = MNTN_recv == "MTNOK"
        except Exception as e:
            is_connected = False
            draw_opening_screen(screen, is_connected)
            
            if(e.errno == 10054 or e.errno == 10056):
                logger.log(" * Server Refresh, Creating another socket")
                client_socket = CreateSocket(logger)
            else:
                logger.log(" * Failed to send MTN request\nerrno:" + str(e.errno) + "\n" + str(e))
            continue
        
        draw_opening_screen(screen, is_connected)
        
        
        # Check for the user closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pressed()[0] == True):
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the user clicked on the start button, and initiate the game.
                    mouse_over_start_button = mouse_pos[0] >= STARTGAME_BTN_LEFT and mouse_pos[0] <= STARTGAME_BTN_LEFT+STARTGAME_BTN_WIDTH and mouse_pos[1] >= STARTGAME_BTN_TOP and mouse_pos[1] <= STARTGAME_BTN_TOP+STARTGAME_BTN_HEIGHT
                    if(mouse_over_start_button):
                        Game(client_socket).run()
                        main()
                        return
                        
    
    
if __name__ == "__main__":
    main()