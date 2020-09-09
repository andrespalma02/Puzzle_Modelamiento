from abc import ABC, abstractmethod
import pygame
from virus.listener import *
from virus.solapamiento import *
from virus.posicion import *
pygame.init()

class Cuadro(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class CuadroPared(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

class CuadroPaginaWeb(Cuadro):
    def __init__(self, imagen, imagenMala, posicion):
        super().__init__(posicion)
        self.imagenBuena = pygame.image.load(imagen)
        self.imagenMala = pygame.image.load(imagenMala)
        self.esMalo = False

    def dibujar(self, ventana):
        if not self.esMalo:
            ventana.blit(self.imagenBuena, self.posicion.getCoordenadas())
        else:
            ventana.blit(self.imagenMala, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def transformar(self):
        self.esMalo = not self.esMalo

    def obtenerEstado(self):
        return (self.posicion.getCoordenadas(), self.esMalo)



class CuadroObjetivo(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def getCoordenadas(self):
        return self.posicion.getCoordenadas()

class CuadroPersonaje(Cuadro):
    def __init__(self, imagen, posicion, solapamiento):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.solapamiento = solapamiento

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self, dr):
        listener = Listener()
        keys = listener.detectar()
        x, y = self.posicion.getCoordenadas()
        if keys[pygame.K_UP] and self.solapamiento.verificarSolapamiento((x,y),(x, y - dr)):
            self.posicion.y -= dr
            pygame.time.delay(150)
        if keys[pygame.K_DOWN] and self.solapamiento.verificarSolapamiento((x,y),(x, y + dr)):
            self.posicion.y += dr
            pygame.time.delay(150)
        if keys[pygame.K_LEFT] and self.solapamiento.verificarSolapamiento((x,y),(x - dr, y)):
            self.posicion.x -= dr
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and self.solapamiento.verificarSolapamiento((x,y),(x + dr, y)):
            self.posicion.x += dr
            pygame.time.delay(150)

class Mensaje(Cuadro):
    def __init__(self, imagen, nombre, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def dibujar(self, ventana):
        if self.aparecer:
            ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def esperar(self, juego):
        listener = Listener()
        if self.aparecer:
            keys = listener.detectar()
            if keys[pygame.K_SPACE] and self.nombre == 'instrucciones':
                self.aparecer = False
            elif keys[pygame.K_RETURN] and self.nombre == 'fallo':
                self.aparecer = False
                juego.reiniciarJuego()
            elif keys[pygame.K_RETURN] and self.nombre == 'victoria':
                self.aparecer = False
                juego.reiniciarJuego()
            elif keys[pygame.K_ESCAPE] and self.nombre == 'victoria':
                self.aparecer = False
                juego.salirJuego()

    def autorizarDibujo(self, booleano):
        self.aparecer = booleano

    def getAparecer(self):
        return self.aparecer

    def getNombre(self):
        return self.nombre

class Mapa(Cuadro):

    def __init__(self, imagen):
        super().__init__(Posicion(0,0))
        self.imagen = pygame.image.load(imagen)
        self.dictCuadros = dict()
        self.dictCuadros['cuadroObjetivo'] = None
        self.dictCuadros['cuadroPaginaWeb'] = list()
        self.dictCuadros['cuadroPared'] = list()
        self.dictCuadros['mensaje'] = list()
        self.dictCuadros['personaje'] = None

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def agregarCuadros(self, cuadro):
        if isinstance(cuadro, CuadroObjetivo):
            self.dictCuadros['cuadroObjetivo'] = cuadro
        elif isinstance(cuadro, CuadroPaginaWeb):
            self.dictCuadros['cuadroPaginaWeb'].append(cuadro)
        elif isinstance(cuadro, CuadroPared):
            self.dictCuadros['cuadroPared'].append(cuadro)
        elif isinstance(cuadro, CuadroPersonaje):
            self.dictCuadros['personaje'] = cuadro
        elif isinstance(cuadro, Mensaje):
            self.dictCuadros['mensaje'].append(cuadro)
