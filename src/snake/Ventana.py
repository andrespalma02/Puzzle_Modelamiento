from snake.Mapa import Mapa
#from Marcador import Marcador
import pygame
import sys
import os.path
from pygame.locals import *

bg = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/BG.png"))

class Ventana(object):

    def __init__(self):
        self.mapa=Mapa()
        self.ancho = 768
        self.alto = 512
        self.imagen = bg

    def cargarPantalla(self):
        ventana = pygame.display.set_mode((768,512))
        pygame.display.set_caption('Snake')
        return ventana

    def obtenerMapa(self):
        return self.mapa

    def dibujarFondo(self,ventana):
        ventana.blit(self.imagen, (0,0))

    def obtenerLimites(self):
        return self.ancho,self.alto
