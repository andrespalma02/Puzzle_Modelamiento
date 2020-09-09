
import pygame
import os.path
from snake.Control_Movimiento import Control_Movimiento

pygame.init()

mov_izquierda = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/L1.png"))
mov_derecha = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/R1.png"))
mov_arriba = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/U1.png"))
mov_abajo = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/D1.png"))

class Cabeza(object):
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.vel = 64
        self.izquierda = False
        self.derecha = False
        self.arriba = False
        self.abajo = False

    def dibujar(self, ventana):
    #Cambio de imagen dependiendo de la posicion senialada por teclado
        if self.izquierda:
            ventana.blit(mov_izquierda, (self.x,self.y))
        elif self.derecha:
            ventana.blit(mov_derecha, (self.x,self.y))
        elif self.arriba:
            ventana.blit(mov_arriba, (self.x,self.y))
        else:
            ventana.blit(mov_abajo, (self.x,self.y))

    def mover(self,limiteVentanaX,limiteVentanaY):

        keys = Control_Movimiento.detectarMovimiento()

        if keys[pygame.K_a] and self.x >= 0 and not self.derecha:

            self.x -= self.vel
            self.izquierda = True
            self.derecha = False
            self.arriba = False
            self.abajo = False

        elif keys[pygame.K_d] and self.x <= limiteVentanaX-self.ancho  and not self.izquierda:

            self.x += self.vel
            self.izquierda = False
            self.derecha = True
            self.arriba = False
            self.abajo = False

        elif keys[pygame.K_w] and self.y >= 0  and not self.abajo:

            self.y -= self.vel
            self.izquierda = False
            self.derecha = False
            self.arriba = True
            self.abajo = False

        elif keys[pygame.K_s] and self.y <= limiteVentanaY-self.alto  and not self.arriba:

            self.y += self.vel
            self.izquierda = False
            self.derecha = False
            self.arriba = False
            self.abajo = True

        else:
            if self.izquierda and self.x >= 0:
                self.x -= self.vel

            elif self.derecha and self.x <= limiteVentanaX-self.ancho :
                self.x += self.vel

            elif self.arriba and self.y >= 0:
                self.y -= self.vel

            elif self.abajo and self.y <= limiteVentanaY-self.alto :
                self.y += self.vel

    def obtenerPosicion(self):
        return self.x,self.y

    def cambiarPosicion(self,x,y):
        self.x=x
        self.y=y
        self.izquierda = False
        self.derecha = False
        self.arriba = False
        self.abajo = True

    def retornarPosicion(self,limiteVentanaX,limiteVentanaY):
        if self.x<0:
            self.x=0
        elif self.x>=limiteVentanaX:
            self.x-=64
        if self.y<0:
            self.y=0
        elif self.y>=limiteVentanaY:
            self.y-=64
