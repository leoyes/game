"""
Alien war

"""
import sys
import pygame
from settings import Settings
ai_settings=Settings()

def run_game():
    pygame.init()
    screen=pygame.display.set_mode(size=(ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion War')
    screen.fill(ai_settings.bg_color)
    pygame.display.flip()   
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 

    
run_game()
