import pygame
from laser import Laser
from config_class import *
class Nave(pygame.sprite.Sprite):
    def __init__(self,path_imagen,size,midBottom):
        super().__init__()

        self.image = pygame.image.load(path_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image,size)

        self.rect = self.image.get_rect()
        self.rect.midbottom = midBottom

        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


    def disparar(self,sonido,speed,sprites,lasers):
        laser = Laser(self.rect.midtop,speed)
        try:
            sound_disparo = pygame.mixer.Sound(sonido)
            sound_disparo.play()
        except pygame.error:
            pass
        sprites.add(laser)
        lasers.add(laser)