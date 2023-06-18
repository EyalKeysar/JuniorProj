import pygame
import sys
import os
import time
import socket
from GameConstants import *
from Network.logger import Logger
from Network.constants import *
from game import Game

def main():
    logger =  Logger() 
    logger.log(" * Starting game")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    
    screen.fill((0, 0, 0))
    draw_opening_screen(screen)
    
    
    # set up socket client sent to 127.0.0.1:1337
    data = ""
    client_socket = socket.socket()
    client_socket.settimeout(2)
    while data != "ACK":
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        try:
            client_socket.connect(("127.0.0.2", SERVER_PORT))
            client_socket.send("SYN".encode())
    
            data = client_socket.recv(1024).decode()
            logger.log(" Server replied: " + data)
            
        except Exception as e:
            logger.log(" * Failed To Connect \n" + str(e))
            time.sleep(1)
            continue
            
    logger.log("Connected to server")
    is_connected = True
    
    while True:
        
        logger.log(" * Waiting in maintenance mode")
        client_socket.send("MTN".encode())
        MNTN_recv = client_socket.recv(1024).decode()
        is_connected = MNTN_recv == "MTNOK"
        
        
        # Add visual element that displays connection status !!!!!!!!!
        
        
        screen.fill((0, 0, 0))
        draw_opening_screen(screen)
        
        #update the display
        pygame.display.update()
        
        # Check for the user closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pressed()[0] == True):
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_over_start_button = mouse_pos[0] >= STARTGAME_BTN_LEFT and mouse_pos[0] <= STARTGAME_BTN_LEFT+STARTGAME_BTN_WIDTH and mouse_pos[1] >= STARTGAME_BTN_TOP and mouse_pos[1] <= STARTGAME_BTN_TOP+STARTGAME_BTN_HEIGHT
                    if(mouse_over_start_button):
                        print("Start Game")
                        Game().run()
                        print("Game Over")
                        main()
                        
                

def draw_title(screen, color=TITLE_TXT_CLR):
    title_font = pygame.font.Font(TEXT_FONT, TITLE_TXT_SIZE)
    title_text = title_font.render(GAME_NAME, True, color)
    title_rect = title_text.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.centery = 100
    screen.blit(title_text, title_rect)

def draw_start_button(screen, color=STARTGAME_BTN_COLOR, text_color=STARTGAME_BTN_TXT_CLR):
    start_button = pygame.Rect(STARTGAME_BTN_LEFT, STARTGAME_BTN_TOP, STARTGAME_BTN_WIDTH, STARTGAME_BTN_HEIGHT)
    pygame.draw.rect(screen, color, start_button)
    text_font = pygame.font.Font(TEXT_FONT, STARTGAME_BTN_FONT_SIZE)
    text = text_font.render(STARTGAME_BTN_TXT, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = start_button.center
    screen.blit(text, text_rect)

def draw_opening_screen(screen):
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the title text
    draw_title(screen, (255, 0, 0))
    # Draw the start button
    draw_start_button(screen)
    
    
    
    
if __name__ == "__main__":
    main()