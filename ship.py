import pygame
class Ship():
    def __init__(self,screen):
        self.screen=screen

        self.image=pygame.image.load('ship.jpg')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        
