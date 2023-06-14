import pygame
import sys
import random
from config_class import *
from nave import *
from asteroide import *

def generar_asteroides(grupo_asteroides,grupo_sprites,cantidad):
    if len(grupo_asteroides) == 0:
        for i in range(cantidad):
            posicion = (random.randrange(20,WIDTH-20),random.randrange(-500,HEIGHT // 2))
            asteroide = Asteroide("./images/asteroide.png",SIZE_ASTEROIDE,posicion,SPEED_ASTEROIDE)
            grupo_asteroides.add(asteroide)
            grupo_sprites.add(asteroide)



pygame.init()
try:
    pygame.mixer.init()
except pygame.error:
    pass

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sprites")
fondo = pygame.image.load("./images/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo,(WIDTH,HEIGHT))

sprites = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
lasers = pygame.sprite.Group()

nave = Nave("./images/nave.png",SIZE_NAVE,(screen.get_width()//2, screen.get_height() - 20))
sprites.add(nave)


while True:
    clock.tick(FPS)

    for evento in pygame.event.get():
        match evento.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()

            case pygame.MOUSEBUTTONDOWN:
                    nave.rect.center = pygame.mouse.get_pos()

            case pygame.KEYDOWN:
                match evento.key:
                    case pygame.K_LEFT:
                        nave.velocidad_x = -SPEED_NAVE
                    case pygame.K_RIGHT:
                        nave.velocidad_x = +SPEED_NAVE

                    case pygame.K_UP:
                        nave.velocidad_y = -SPEED_NAVE
                    case pygame.K_DOWN:
                        nave.velocidad_y = +SPEED_NAVE

                    case pygame.K_SPACE:
                        nave.disparar("./sounds/sonido_laser.mp3",SPEED_LASER,sprites,lasers)
            case pygame.KEYUP:
                    nave.velocidad_x = 0
                    nave.velocidad_y = 0


    for asteroide in asteroides:
        if asteroide.rect.bottom >= HEIGHT:
            asteroide.kill()

    pygame.sprite.spritecollide(nave,asteroides,True)
    generar_asteroides(asteroides,sprites,MAX_ASTEROIDES)

    sprites.update()
    screen.blit(fondo,ORIGIN)
    sprites.draw(screen)
    pygame.display.flip()