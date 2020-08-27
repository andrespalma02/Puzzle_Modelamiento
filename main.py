import pygame
from abc import *
import random

import pygame

NIVEL = 0
N = NIVEL + 2
DIM = int(420 / N)
DIMENSION = 500, 500  # Se define las dimensiones de la ventana del juego


class Listener:
    @staticmethod
    def detectar() -> tuple:
        return pygame.key.get_pressed()


class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
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
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicion.getX(), self.posicion.getY()))

    def mover(self, colision):
        keys = Listener.detectar()
        x = self.posicion.getX()
        y = self.posicion.getY()

        if keys[pygame.K_LEFT]:
            colision.verificarColision((x + DIM, y))
        if keys[pygame.K_RIGHT]:
            colision.verificarColision((x - DIM, y))
        if keys[pygame.K_UP]:
            colision.verificarColision((x, y + DIM))
        if keys[pygame.K_DOWN]:
            colision.verificarColision((x, y - DIM))


class FragmentoImagen(Cuadro):

    def __init__(self, posicion, imagen, posicionact):
        self._Cuadro__posicion = posicion
        self.imagen = imagen
        self.posicionActual = posicionact

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicionActual.getX(), self.posicionActual.getY()))

    def mover(self):
        pass

    def getPosicionActual(self):
        (x, y) = self.posicionActual.getX(), self.posicionActual.getY()
        return (x, y)

    def setPosicionActual(self, posicion):
        self.posicionActual = posicion


class Imagen(Cuadro):
    def __init__(self):
        self._Cuadro__posicion = None
        self.imagen = None
        self.dimension = DIM
        self.lista_cuadros = list()
        self.cuadro_vacio = None

    def mover(self):
        self.cuadro_vacio.mover(colision)

    def dibujar(self, posicion, imagen):
        self.imagen = pygame.image.load(imagen)
        self._Cuadro__posicion = posicion

    def descomponer(self):
        listaimg = list()
        listapos = list()
        listarand = list()

        for i in range(N):
            for j in range(N):
                posx = int(40 + j * DIM)
                posy = int(40 + i * DIM)
                listapos.append((posx, posy))  # Se guardan las posiciones correctas de los fragmento
                listarand.append((posx, posy))
                imaux = pygame.Surface((DIM, DIM))  # Se crea una superficie
                imaux.blit(self.imagen, (0, 0), (posx - 40, posy - 40, DIM, DIM))
                listaimg.append(imaux)
        random.shuffle(listarand)
        for i in range(len(listapos)):
            if listarand[i] == listapos[len(listapos) - 1]:
                self.cuadro_vacio = \
                    CuadroVacio(Posicion(listarand[i][0], listarand[i][0]), "CuadroVacio.png")
            else:
                self.agregarCuadro(FragmentoImagen(
                    Posicion(listapos[i][0], listapos[i][1]),
                    listaimg[i],
                    Posicion(listarand[i][0], listarand[i][1])))

    def actualizarImagen(self, ventana):
        for i in range(len(self.lista_cuadros)):
            self.lista_cuadros[i].dibujar(ventana)
        self.cuadro_vacio.dibujar(ventana)

    def agregarCuadro(self, fragmentoimagen):
        self.lista_cuadros.append(fragmentoimagen)

    def intercambiar(self, posicion):
        for i in range(len(self.lista_cuadros)):
            if (self.lista_cuadros[i].getPosicionActual() == posicion):
                self.lista_cuadros[i].setPosicionActual(Posicion(self.cuadro_vacio.posicion.getX(),
                                                                 self.cuadro_vacio.posicion.getY()))
        self.cuadro_vacio.posicion.setX(posicion[0])
        self.cuadro_vacio.posicion.setY(posicion[1])

    def getLista(self):
        return self.lista_cuadros


class Contador:
    def __init__(self, puntaje):
        self.numeroMovimientos = int(0)
        self.verificacion = verificacion

    def aumentar(self):
        self.numeroMovimientos += 1
        verificacion.verificarCondiciones(self.numeroMovimientos)


class Colision:
    def __init__(self, contador, imagen):
        self.imagen = imagen
        self.contador = contador

    def verificarColision(self, posicion):

        for pos in self.imagen.getLista():
            if pos.getPosicionActual() == posicion:
                self.imagen.intercambiar(posicion)
                self.contador.aumentar()


class Verificacion:
    def __init__(self, imagen, puntaje):
        self.imagen = imagen
        self.puntaje = puntaje

    def verificarCondiciones(self, numeroMovimientos):
        cont = 0

        for elemento in imagen.getLista():
            if ((elemento.posicion.getX(), elemento.posicion.getY())
                    == elemento.getPosicionActual()):
                cont += 1
        if cont == len(imagen.getLista()):
            self.puntaje.calcularPuntaje(numeroMovimientos)


class Puntaje:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.puntajeFinal = 0

    def calcularPuntaje(self, numeroMovimientos):
        self.puntajeFinal = int(100000 / numeroMovimientos)


class Puzzle:

    def iniciarJuego(self, imagen):
        pygame.init()
        clock = pygame.time.Clock()
        imagen.dibujar(Posicion(0, 0), "Imagen.png")
        imagen.descomponer()

    def finalizarJuego(self, ventana):
        ventana.blit(pygame.image.load("Imagen.png"),(0,0))

puzzle = Puzzle()
imagen = Imagen()
puntaje = Puntaje(puzzle)
verificacion = Verificacion(imagen,puntaje)
contador = Contador(verificacion)
colision = Colision(contador, imagen)
puzzle.iniciarJuego(imagen)

pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
titulo_juego = pygame.display.set_caption('I <3 PUZZLE')  # Se inserta un titulo a la ventana creada

iniciado = True
while iniciado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT and puntaje.puntajeFinal !=0:
            puzzle.finalizarJuego(pantalla_juego)
            iniciado = False
        pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
        imagen.mover()
        imagen.actualizarImagen(pantalla_juego)
        pygame.display.update()
