import pygame
from GameConstants import *

class Button:
    def __init__(self, color, hover_color, text, text_size, text_color, x, y, width, height):
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen, is_hover=False):
        if(is_hover):
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(TEXT_FONT, self.text_size)
        text = font.render(self.text, 1, self.text_color)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, mouse_pos):
        return mouse_pos[0] >= self.x and mouse_pos[0] <= self.x+self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y+self.height