import pygame
from GameConstants import *
import sys
from Button import Button


def draw_title(screen, x, y, color, text):

    text_font = pygame.font.Font(TEXT_FONT, TITLE_TXT_SIZE)
    text = text_font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text, text_rect)
    
    
def draw_connection_status(screen, is_connected):
    if(is_connected):
        color = (0, 255, 0)
        text = "Connected"
    else:
        color = (255, 0, 0)
        text = "Disconnected"
        
    connection_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 50)
    pygame.draw.rect(screen, color, connection_rect)
    text_font = pygame.font.Font(TEXT_FONT, 32)
    text = text_font.render(text, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = connection_rect.center
    screen.blit(text, text_rect)

def draw_opening_screen(screen, is_connected, start_button, is_over):
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the title text
    draw_title(screen, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/4, color=(255, 0, 0), text=GAME_NAME)
    # Draw the start button
    if(is_over):
        start_button.draw(screen, True)
    else:
        start_button.draw(screen, False)
    # Draw the connection status
    draw_connection_status(screen, is_connected)
    
    pygame.display.update()
    
def draw_active_players(screen, active_players_btn_lst):
    '''Draws a block with list of buttons, each button text is from the active_players list using Button class'''
    for btn in active_players_btn_lst:
        btn.draw(screen)
    


    

def draw_lobby_screen(screen, is_connected, active_players_btn_lst):
    screen.fill((0, 0, 0))
    draw_title(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/7, (255, 0, 0), LOBBY_TITLE)
    
    draw_active_players(screen, active_players_btn_lst)

    draw_connection_status(screen, is_connected)

    pygame.display.update()