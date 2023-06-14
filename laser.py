import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,midBottom,speed):
        super().__init__()

        self.image = pygame.Surface((5,30))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.midbottom = midBottom

        self.velocidad_y = speed

    def update(self):
        self.rect.y -= self.velocidad_y