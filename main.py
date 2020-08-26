import pygame
from abc import *
import random

import pygame

NIVEL = 5
N = NIVEL + 2
DIM = int(420 / N)
DIMENSION = 1000, 500  # Se define las dimensiones de la ventana del juego

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
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension), self.posicion.getPosicion())

    def mover(self, rd):
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_LEFT]:
            self.posicion.x -= rd
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT]:
            self.posicion.x += rd
            pygame.time.delay(150)
        if keys[pygame.K_UP]:
            self.posicion.y -= rd
            pygame.time.delay(150)
        if keys[pygame.K_DOWN]:
            self.posicion.y += rd
            pygame.time.delay(150)


class FragmentoImagen(Cuadro):

    def __init__(self, posicion, imagen):
        self._Cuadro__posicion = posicion
        self.imagen = imagen

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
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
        self.dimension = DIM
        self.lista_cuadros = list()

    def mover(self):
        pass

    def dibujar(self):
        listaimg=list()
        listapos=list()
        listarand=list()
        for i in range(N):
            for j in range(N):
                posx = int(40 + j * DIM)
                posy = int(40 + i * DIM)
                listapos.append((posx, posy))  # Se guardan las posiciones correctas de los fragmentos
                listarand.append((posx, posy))  # Se guardan posiciones randomicas para los fragmentos
                imaux = pygame.Surface((DIM, DIM))  # Se crea una superficie
                imaux.blit(self.imagen, (0, 0), (posx - 40, posy - 40, DIM, DIM))
                listaimg.append(imaux)
        return listaimg
    def descomponer(self):
        listarand=list()


    def actualizarPosicion(self):
        pass

    def agregarCuadro(self, cuadro):
        listaimg=list()
        for i in range(len(listaimg) - 1):
            self.lista_cuadros.append(listaimg[i])
        self.lista_cuadros = \
            CuadroVacio(Posicion(40 + (N - 1) * DIM, 40 + (N - 1) * DIM), "CuadroVacio.png")





class Contador:
    def __init__(self):
        self.numeroMovimientos = int(0)

    def aumentar(self):
        return self.numeroMovimientos + 1


class Colision:
    def __init__(self, contador, listafragmentos):
        self.listafragmentos = listafragmentos
        self.contador = contador

    def verificarColision(self, posicion):
        for pos in self.listafragmentos.accederLista():
            if pos == posicion:
                return True
                self.contador.aumentar()
        return False


class Puntaje:
    def __init__(self, puntaje):
        self.puntaje = puntaje


class Puzzle:
    def iniciarJuego(self):
        pygame.init()
        cuadroVacio=CuadroVacio(Posicion(40 + (N - 1) * DIM, 40 + (N - 1) * DIM), "CuadroVacio.png")
        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        titulo_juego = pygame.display.set_caption('I <3 PUZZLE')  # Se inserta un titulo a la ventana creada
        clock = pygame.time.Clock()
        print("hola")
        imagen = Imagen(Posicion(0, 0), "plantilla.png")
        imagen.dibujar()
        imagen.descomponer()
        iniciado = True
        listaimg=list()
        listarand=list()
        while iniciado:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    iniciado = False
                pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                cuadroVacio.dibujar(pantalla_juego)
                for elemento in range(len(listaimg) - 1):  # se muestran en pantalla todos los fragmentos de la imagen
                    pantalla_juego.blit(listaimg[elemento], listarand[
                        elemento])  # Se pasa la lista de imagenes y la lista de las posiciones para que se muestren en pantalla

                cuadroVacio.posicion.getPosicion()
                print(cuadroVacio.posicion.getPosicion())
                cuadroVacio.mover(DIM)
                pygame.display.update()


puzzle=Puzzle()
puzzle.iniciarJuego()
'''
 # Comparar las colisiones
        for cuadrofragmento in listapos:
            if cuadroVacio.posicion.getPosicion() == cuadrofragmento:
                print("COLISION")
                auxiliar = cuadroVacio.posicion.getPosicion()
                cuadroVacio.posicion.actualizar(cuadrofragmento[0], cuadrofragmento[1])
                cuadrofragmento = auxiliar

            else:
                pass

'''

