import pygame
from GameConstants import *
import sys


def draw_title(screen, color=TITLE_TXT_CLR):
    title_font = pygame.font.Font(TEXT_FONT, TITLE_TXT_SIZE)
    title_text = title_font.render(GAME_NAME, True, color)
    title_rect = title_text.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.centery = 100
    screen.blit(title_text, title_rect)
    
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

def draw_start_button(screen, color=STARTGAME_BTN_COLOR, text_color=STARTGAME_BTN_TXT_CLR):
    start_button = pygame.Rect(STARTGAME_BTN_LEFT, STARTGAME_BTN_TOP, STARTGAME_BTN_WIDTH, STARTGAME_BTN_HEIGHT)
    pygame.draw.rect(screen, color, start_button)
    text_font = pygame.font.Font(TEXT_FONT, STARTGAME_BTN_FONT_SIZE)
    text = text_font.render(STARTGAME_BTN_TXT, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = start_button.center
    screen.blit(text, text_rect)

def draw_opening_screen(screen, is_connected):
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the title text
    draw_title(screen, (255, 0, 0))
    # Draw the start button
    draw_start_button(screen)
    # Draw the connection status
    draw_connection_status(screen, is_connected)
    
    pygame.display.update()
    