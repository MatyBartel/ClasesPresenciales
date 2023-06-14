import pygame
import sys
import random

from config_class import *
from nave import *
from asteroide import *

class Game:
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error:
            pass

        self.clock = pygame.time.Clock()
        self.score = 0
        self.jugando = False
        self.finalizado = False
        
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Sprites")
        self.fondo = pygame.image.load("./images/fondo.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo,(WIDTH,HEIGHT))
        self.fuente = pygame.font.Font("freesansbold.ttf",40)
        self.sprites = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()

        self.nave = nave = Nave("./images/nave.png",SIZE_NAVE,(self.screen.get_width()//2, self.screen.get_height() - 20))

        self.agregar_sprite(nave)
    
    def agregar_sprite(self,sprite):
        self.sprites.add(sprite)
    def agregar_asteroide(self,asteroide):
        self.asteroides.add(asteroide)
    def agregar_laser(self,laser):
        self.lasers.add(laser)

    def iniciar_juego(self):
        self.jugando = True
        self.finalizado = False

        while self.jugando:
            self.clock.tick(FPS)
            
            self.manejar_eventos()
            
            self.actualizar_elementos()

            self.renderizar_pantalla()

    def manejar_eventos(self):

        for evento in pygame.event.get():
            match evento.type:
                case pygame.QUIT:
                        self.salir()
                case pygame.MOUSEBUTTONDOWN:
                        self.nave.rect.center = pygame.mouse.get_pos()

                case pygame.KEYDOWN:
                    match evento.key:
                        case pygame.K_LEFT:
                            self.nave.velocidad_x = -SPEED_NAVE
                        case pygame.K_RIGHT:
                            self.nave.velocidad_x = +SPEED_NAVE

                        case pygame.K_UP:
                            self.nave.velocidad_y = -SPEED_NAVE
                        case pygame.K_DOWN:
                            self.nave.velocidad_y = +SPEED_NAVE

                        case pygame.K_SPACE:
                            self.nave.disparar("./sounds/sonido_laser.mp3",SPEED_LASER,self.sprites,self.lasers)
                        case pygame.KEYUP:
                            self.nave.velocidad_x = 0
                            self.nave.velocidad_y = 0
                        case pygame.K_ESCAPE:
                            self.terminar_partida()


    def actualizar_elementos(self):
        self.generar_asteroides(MAX_ASTEROIDES)
        self.sprites.update()

        for asteroide in self.asteroides:
            if asteroide.rect.bottom >= HEIGHT:
                asteroide.kill()
            lista = pygame.sprite.spritecollide(self.nave,self.asteroides,True)
        
        if len(lista) > 0:
            self.perder()

        for laser in self.lasers:
            if laser.rect.top <= 0:
                laser.kill()
            lista = pygame.sprite.spritecollide(laser,self.asteroides,True)
        if len(lista):
            self.finalizado = True

    def renderizar_pantalla(self):
       self.screen.blit(self.fondo,ORIGIN)
       self.sprites.draw(self.screen)

    def cerrar_juego(self):
        pygame.quit()
        sys.exit()

    def terminar_partida(self):
        self.jugando = False

    def generar_asteroides(self,cantidad):
        if len(self.asteroides) == 0:
            for i in range(cantidad):
                posicion = (random.randrange(20,WIDTH-20),random.randrange(-500,HEIGHT // 2))
                asteroide = Asteroide("./images/asteroide.png",SIZE_ASTEROIDE,posicion,SPEED_ASTEROIDE)
                self.agregar_asteroide(asteroide)
                self.agregar_sprite(asteroide)

    def perder(self):
        self.finalizado = True
        self.mostrar_pantalla_fin()

    def mostrar_pantalla_fin(self):
        texto = self.fuente.render("GAME OVER",True,(255,255,255))
        rect_texto = texto.get_rect()
        rect_texto.center = (CENTER)
        self.screen.fill((0,0,0))

        self.screen.blit(texto)
        pygame.display.flip()
        pygame.time.wait(5000)

juego = Game()

juego.iniciar_juego()