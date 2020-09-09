from virus.virus import *
from laberinto.laberinto import *
from ruta.ruta import *
from snake.snake import *
from puzzle.puzzleJ import *
import pygame
import os
import settings as s
from abc import ABC, abstractmethod
from posicion import *
from listener import *

pygame.init()


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


class Fondo(Cuadro):
    def __init__(self, imagen, posicion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = s.columnas * s.dim_Cuadro
        alto = s.filas * s.dim_Cuadro
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), self.posicion.getPosicion())

    def mover(self):
        pass


class Personaje(Cuadro):
    def __init__(self, imagen, posicion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), self.posicion.getPosicion())

    def mover(self, dr, sl):
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_UP] and sl.verificar((x, y - dr)):
            self.posicion.y -= dr
            pygame.time.delay(150)
        if keys[pygame.K_DOWN] and sl.verificar((x, y + dr)):
            self.posicion.y += dr
            pygame.time.delay(150)
        if keys[pygame.K_LEFT] and sl.verificar((x - dr, y)):
            self.posicion.x -= dr
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and sl.verificar((x + dr, y)):
            self.posicion.x += dr
            pygame.time.delay(150)



class MapaMuseo(Cuadro):
    def __init__(self):
        self._Cuadro__posicion = Posicion(0,0)
        self.dictCuadros = dict()
        self.dictCuadros['camino'] = list()
        self.dictCuadros['estaciones'] = list()
        self.dictCuadros['personaje'] = None
        self.dictCuadros['fondo'] = None
        self.dictCuadros['mensaje'] = list()
        self.dictCuadros['marcador'] = None


    def agregarCuadros(self, cuadro):
        if isinstance(cuadro, Camino):
             self.dictCuadros['camino'].append(cuadro)
        elif isinstance(cuadro, Estacion):
             self.dictCuadros['estaciones'].append(cuadro)
        elif isinstance(cuadro, Personaje):
             self.dictCuadros['personaje'] = cuadro
        elif isinstance(cuadro, Fondo):
             self.dictCuadros['fondo'] = cuadro
        elif isinstance(cuadro, Mensaje):
            self.dictCuadros['mensaje'].append(cuadro)
        elif isinstance(cuadro, Marcador):
            self.dictCuadros['marcador'] = cuadro

    def accederLista(self):
        return self.dictCuadros

    def dibujar(self,ventana):
        self.dictCuadros['fondo'].dibujar(ventana)
        for camino in self.dictCuadros['camino']:
            camino.dibujar(ventana)
        for estacion in self.dictCuadros['estaciones']:
            estacion.dibujar(ventana)
        self.dictCuadros['personaje'].dibujar(ventana)
        self.dictCuadros['marcador'].dibujar(ventana)
        for mensaje in self.dictCuadros['mensaje']:
            mensaje.dibujar(ventana)
        pygame.display.update()

    def mover(self, solapamiento):
        self.dictCuadros['fondo'].mover()
        for camino in self.dictCuadros['camino']:
            camino.mover()
        for estacion in self.dictCuadros['estaciones']:
            estacion.mover()
        self.dictCuadros['personaje'].mover(s.dim_Cuadro, solapamiento)

class Estacion(Cuadro):
    def __init__(self, imagen, posicion, nombreEstacion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombreEstacion

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()

class Camino(Cuadro):
    def __init__(self, imagen, posicion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), self.posicion.getPosicion())

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()

class Mensaje(Cuadro):
    def __init__(self, imagen, nombre):
        self._Cuadro__posicion = Posicion(175,120)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def dibujar(self, ventana):
        if self.aparecer:
            ventana.blit(self.imagen, self.posicion.getPosicion())

    def permitirDibujo(self, booleano):
        self.aparecer = booleano

    def getAparecer(self):
        return self.aparecer

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def esperar(self):
        if self.aparecer:
            keys = Listener.detectar()
            juego = None
            if keys[pygame.K_RETURN] and self.nombre != 'inicio':
                pygame.quit()
                if self.nombre == 'laberinto':
                    juego = Laberinto()
                if self.nombre == 'puzzle':
                    juego = Puzzle()
                if self.nombre == 'ruta':
                    juego = Ruta()
                if self.nombre == 'snake':
                    juego = Snake()
                if self.nombre == 'virus':
                    juego = EvitandoVirus()
                juego.iniciarJuego()
            elif keys[pygame.K_ESCAPE]:
                self.aparecer = False

class Marcador(Cuadro):

    def __init__(self, imagen, posicion, puntaje):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)
        self.puntaje = puntaje

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())
        fuente = pygame.font.SysFont('Arial', 25)
        texto_puntaje = fuente.render(f'Puntaje: {self.puntaje.getAcumulador()}', 0, (255, 255, 255))
        ventana.blit(texto_puntaje, (self.posicion.getPosicion()[0] + 65, self.posicion.getPosicion()[1] + 10))

    def mover(self):
        pass
