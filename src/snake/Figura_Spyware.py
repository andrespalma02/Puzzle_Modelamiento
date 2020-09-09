from snake.Figura import Figura

import pygame
import os
import sys

spywareIMG = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/spyware.png"))
spywareIMG = pygame.transform.scale(spywareIMG, (64, 64))
class Figura_Spyware(Figura):

    def __init__(self, x, y):
        self.valor = 100
        self.posX = x
        self.posY = y
        self.imagen = spywareIMG

    def dibujar(self,ventana):
        ventana.blit(self.imagen, (self.posX,self.posY))

    def obtenerValor(self):
        return self.valor

    def obtenerPosicion(self):
        return self.posX,self.posY
