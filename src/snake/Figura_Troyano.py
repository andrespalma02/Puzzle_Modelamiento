from snake.Figura import Figura

import pygame
import os
import sys

troyanoIMG = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/troyano.png"))
troyanoIMG = pygame.transform.scale(troyanoIMG, (64, 64))
class Figura_Troyano(Figura):

    def __init__(self, x, y):
        self.valor = 150
        self.posX = x
        self.posY = y
        self.imagen = troyanoIMG

    def dibujar(self,ventana):
        ventana.blit(self.imagen, (self.posX,self.posY))

    def obtenerValor(self):
        return self.valor

    def obtenerPosicion(self):
        return self.posX,self.posY
