import pygame

class Asteroide(pygame.sprite.Sprite):
    def __init__(self,path_imagen,size,center,speed):
        super().__init__()

        self.image = pygame.image.load(path_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image,size)

        self.rect = self.image.get_rect()
        self.rect.center = center

        self.velocidad_y = speed

    def update(self):
        self.rect.y += self.velocidad_y