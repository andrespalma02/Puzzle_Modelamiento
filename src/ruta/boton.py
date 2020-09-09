import pygame
from ruta.assets.settings import *
from ruta.assets.herramientas import *
from ruta.posicionMaya import *


class BotonRuta:
    def __init__(self, tipo, posicion):
        self.tipo = tipo
        
        if tipo == "OK":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botonOk.png', __file__))
        elif tipo == "JUGAR":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botonJugar.png', __file__))
        elif tipo == "ATRAS":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botonAtras.png', __file__))
        
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoBoton"])
        self._rect = pygame.Rect((0, 0), (100, 100))
        self.posicion = posicion

    def render(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def onClic(self, event):
        rect = pygame.Rect(self.posicion.getPosicion(), (self.imagen.get_rect().width, self.imagen.get_rect().height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect.collidepoint(event.pos):
                    return (self.tipo, True)
        return (self.tipo, False)
