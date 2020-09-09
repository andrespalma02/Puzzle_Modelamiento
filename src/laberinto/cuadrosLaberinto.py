import pygame
import laberinto.settingsLaberinto as s
from pygame.locals import *
from abc import ABC, abstractmethod
from laberinto.posicionLaberinto import *
from laberinto.listenerLaberinto import *

class CuadroLaberinto(ABC):
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


class FondoLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = s.columnas * s.dim_Cuadro
        alto = s.filas * s.dim_Cuadro
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), (x, y))

    def mover(self):
        pass


class PersonajeLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagen = pygame.image.load(imagen)
        self.numeroVidas = s.maximo_de_vidas

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self, dr, sl):
        keys = ListenerLaberinto.detectar()
        (x, y) = (self.posicion.x, self.posicion.y)
        if keys[pygame.K_UP] and sl.verificar((x, y - dr)):
            self.posicion.actualizarY(y - dr)
            pygame.time.delay(150)
        if keys[pygame.K_DOWN] and sl.verificar((x, y + dr)):
            self.posicion.actualizarY(y + dr)
            pygame.time.delay(150)
        if keys[pygame.K_LEFT] and sl.verificar((x - dr, y)):
            self.posicion.actualizarX(x - dr)
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and sl.verificar((x + dr, y)):
            self.posicion.actualizarX(x + dr)
            pygame.time.delay(150)


class CaminoLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass


class VirusLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass


class MetaLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass

class MensajeLaberinto(CuadroLaberinto):
    def __init__(self, imagen, nombre):
        self._CuadroLaberinto__posicion = PosicionLaberinto(0, 0)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def permitirDibujo(self, bool):
        self.aparecer = bool

    def getNombre(self):
        return self.nombre

    def getAparecer(self):
        return self.aparecer

    def dibujar(self, ventana):
        if self.aparecer:
            (x, y) = (self.posicion.x, self.posicion.y)
            ventana.blit(pygame.transform.scale(self.imagen, (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)), (x, y))

    def mover(self):
        pass

class TableroLaberinto(CuadroLaberinto):
    def __init__(self):
        self._CuadroLaberinto__posicion = PosicionLaberinto(0,0)
        self.dictCuadros = dict()
        self.dictCuadros['camino'] = list()
        self.dictCuadros['virus'] = list()
        self.dictCuadros['personaje'] = None
        self.dictCuadros['fondo'] = None
        self.dictCuadros['meta'] = None
        self.dictCuadros['mensaje'] = list()
        self.dictCuadros['vidas'] = list()

    def agregarCuadros(self, cuadro):
        if isinstance(cuadro, CaminoLaberinto):
             self.dictCuadros['camino'].append(cuadro)
        elif isinstance(cuadro, VirusLaberinto):
             self.dictCuadros['virus'].append(cuadro)
        elif isinstance(cuadro, PersonajeLaberinto):
             self.dictCuadros['personaje'] = cuadro
        elif isinstance(cuadro, MetaLaberinto):
             self.dictCuadros['meta'] = cuadro
        elif isinstance(cuadro, FondoLaberinto):
             self.dictCuadros['fondo'] = cuadro
        elif isinstance(cuadro, MensajeLaberinto):
            self.dictCuadros['mensaje'].append(cuadro)
        elif isinstance(cuadro, VidaLaberinto):
            self.dictCuadros['vidas'].append(cuadro)

    def dibujar(self,ventana):
        pass

    def mover(self, solapamiento):
        pass


class VidaLaberinto(CuadroLaberinto):
    def __init__(self, imagen1, imagen2, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagenes = [pygame.image.load(imagen1), pygame.image.load(imagen2)]
        self.lleno = 1

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagenes[self.lleno], (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass
