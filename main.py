import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.2.1') 


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

    client_socket = CreateSocket(logger)
    logger.log("Connected to server")

    is_connected = True

    main_loop(logger, screen, client_socket, is_connected)
    
    
                        
    
def main_loop(logger, screen, client_socket, is_connected):
    while True:
            logger.log(" * Waiting in maintenance mode")
            try:
                is_connected = CheckConnection(client_socket)
            except Exception as e:
                logger.log(" * Connection to server lost")
                is_connected = False
                draw_opening_screen(screen, is_connected, start_game_button, False)
                client_socket = HandelConnectionError(e, logger, client_socket)
                continue
            
            mouse_pos = pygame.mouse.get_pos()
            draw_opening_screen(screen, is_connected, start_game_button, start_game_button.is_over(mouse_pos))


            # Check for the user closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(pygame.mouse.get_pressed()[0] == True):
                        mouse_pos = pygame.mouse.get_pos()
                        # Check if the user clicked on the start button, and initiate the game.
                        mouse_over_start_button = mouse_pos[0] >= STARTGAME_BTN_X and mouse_pos[0] <= STARTGAME_BTN_X+STARTGAME_BTN_WIDTH and mouse_pos[1] >= STARTGAME_BTN_Y and mouse_pos[1] <= STARTGAME_BTN_Y+STARTGAME_BTN_HEIGHT
                        
                        if(start_game_button.is_over(mouse_pos)):
                            logger.log(" * Join Lobby -----------------------------------")
                            client_socket = LobbyHandler(screen, client_socket, logger).run()
                            continue


if __name__ == "__main__":
    main()