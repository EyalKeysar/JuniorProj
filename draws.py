import pygame
from GameConstants import *
import sys


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

def draw_button(screen, x, y, width, height, color, text, text_color):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    text_font = pygame.font.Font(TEXT_FONT, 32)
    text = text_font.render(text, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = button.center
    screen.blit(text, text_rect)

def draw_start_button(screen, color=STARTGAME_BTN_COLOR, text_color=STARTGAME_BTN_TXT_CLR):
    draw_button(screen, STARTGAME_BTN_LEFT, STARTGAME_BTN_TOP, STARTGAME_BTN_WIDTH, STARTGAME_BTN_HEIGHT, color, STARTGAME_BTN_TXT, text_color)

def draw_opening_screen(screen, is_connected, hover_start_button):
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the title text
    draw_title(screen, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/4, color=(255, 0, 0), text=GAME_NAME)
    # Draw the start button
    if(hover_start_button):
        draw_start_button(screen, color=STARTGAME_BTN_COLOR_HOVER)
    else:
        draw_start_button(screen)
    # Draw the connection status
    draw_connection_status(screen, is_connected)
    
    pygame.display.update()
    

def draw_lobby_screen(screen, is_connected):
    screen.fill((0, 0, 0))

    draw_title(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/7, (255, 0, 0), LOBBY_TITLE)
    
    draw_connection_status(screen, is_connected)

    pygame.display.update()