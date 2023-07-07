import pygame
import sys
import os
import time
import socket
from GameConstants import *
from Network.constants import *
from game import Game
from draws import *
from networks import *
from logger import Logger
from lobby_handler import LobbyHandler


def main():
    logger =  Logger() 
    logger.log(" * Starting game")
    
    # Initializition
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()

    draw_opening_screen(screen, False, False)
    
    client_socket = CreateSocket(logger)
            
    logger.log("Connected to server")

    is_connected = True
    
    while True:
        logger.log(" * Waiting in maintenance mode")
        try:
            is_connected = CheckConnection(client_socket)
        except Exception as e:
            logger.log(" * Connection to server lost")
            is_connected = False
            draw_opening_screen(screen, is_connected)
            client_socket = HandelConnectionError(e, logger, client_socket)
            continue
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_over_start_button = mouse_pos[0] >= STARTGAME_BTN_LEFT and mouse_pos[0] <= STARTGAME_BTN_LEFT+STARTGAME_BTN_WIDTH and mouse_pos[1] >= STARTGAME_BTN_TOP and mouse_pos[1] <= STARTGAME_BTN_TOP+STARTGAME_BTN_HEIGHT
        if(mouse_over_start_button):
            draw_opening_screen(screen, is_connected, True)
        else:
            draw_opening_screen(screen, is_connected, False)
        
        
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
                        logger.log(" * Starting game -----------------------------------")
                        LobbyHandler(screen, client_socket, logger).run()
                        main()
                        return
                        
    
    
if __name__ == "__main__":
    main()