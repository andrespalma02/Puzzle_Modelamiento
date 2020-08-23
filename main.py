import pygame
from abc import *
import random

import pygame


class Listener:
    @staticmethod
    def detectar() -> tuple:
        return pygame.key.get_pressed()


class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosicion(self):
        pos = (self.x, self.y)
        return pos

    def actualizar(self, x, y):
        self.x = x
        self.y = y


class Cuadro(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @property
    def posicion(self):
        return self.__posicion

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class CuadroVacio(Cuadro):

    def __init__(self, posicion, imagen):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, fondo):
        dimension = (140, 140)
        fondo.blit(pygame.transform.scale(self.imagen, dimension), self.posicion.getPosicion())

    def mover(self):
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_RIGHT]:
            self.posicion.x -= 10
            pygame.time.delay(150)
        if keys[pygame.K_DOWN]:
            self.posicion.x -= 10
            pygame.time.delay(150)


class FragmentoImagen(Cuadro):

    def __init__(self, posicion, imagen):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, fondo):
        dimension = (140, 140)
        fondo.blit(pygame.transform.scale(self.imagen, dimension), self.posicion.getPosicion())

    def mover(self):
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_RIGHT]:
            self.posicion.x -= 10
            pygame.time.delay(150)
        if keys[pygame.K_DOWN]:
            self.posicion.x -= 10
            pygame.time.delay(150)


class Imagen(Cuadro):
    def __init__(self, posicion, imagen):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)
        self.dimension = imagen.get_size()
        self.lista_cuadros = dict()
        self.lista_cuadros["CuadroVacio"] = None
        self.lista_cuadros["Fragmentos"] = list()

    def mover(self):
        pass

    def dibujar(self):
        pass

    def descomponer(self):
        pass

    def actualizarPosicion(self):
        pass


'''
for n in range (n*n)
pygame.init()
cuadroVacio = CuadroVacio(Posicion(320, 320), "CuadroVacio.png")
DIMENSION = 1000, 500
pantalla_juego = pygame.display.set_mode(DIMENSION)
titulo_juego = pygame.display.set_caption('I <3 PUZZLE')
clock = pygame.time.Clock()
while True:
    pantalla_juego.fill((255, 255, 255))
    cuadroVacio.dibujar(pantalla_juego)
    pygame.display.update()
'''
nivel = 1
n = 2 + nivel
listapos = list()
listarand = list()
for i in range(n):
    for j in range(n):
        listapos.append((int(40 + j * (420 / n)), int(40 + (i) * (420 / n))))
        listarand.append((int(40 + j * (420 / n)), int(40 + (i) * (420 / n))))
random.shuffle(listarand)
print(listapos)
print(listarand)
