from snake.Figura import Figura

import pygame
import os
import sys

bombaIMG = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/bomba.png"))
bombaIMG = pygame.transform.scale(bombaIMG, (64, 64))
class Figura_Bomba(Figura):

    def __init__(self, x, y):
        self.valor = 50
        self.posX = x
        self.posY = y
        self.imagen = bombaIMG

    def dibujar(self,ventana):
        ventana.blit(self.imagen, (self.posX,self.posY))

    def obtenerValor(self):
        return self.valor

    def obtenerPosicion(self):
        return self.posX,self.posY
