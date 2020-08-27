import pygame
from abc import *
import random

import pygame

NIVEL = 1
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
        fondo.blit(pygame.transform.scale(self.imagen, dimension), (self.posicion.getX(), self.posicion.getY()))

    def mover(self,colision):
        keys = Listener.detectar()
        x = self.posicion.getX()
        y = self.posicion.getY()

        if keys[pygame.K_LEFT]:
            colision.verificarColision(x-DIM)
        if keys[pygame.K_RIGHT]:
            colision.verificarColision(x+DIM)
        if keys[pygame.K_UP]:
            colision.verificarColision(y-DIM)
        if keys[pygame.K_DOWN]:
            colision.verificarColision(y+DIM)



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
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_RIGHT]:
            self.posicion.x -= 10
            pygame.time.delay(150)
        if keys[pygame.K_DOWN]:
            self.posicion.x -= 10
            pygame.time.delay(150)
        if keys[pygame.K_UP]:
            self.posicion.x -= 10
            pygame.time.delay(150)
        if keys[pygame.K_LEFT]:
            self.posicion.x -= 10
            pygame.time.delay(150)

    def getPosicionActual(self):
        return self.posicionActual

    def setPosicionActual(self,posicion):
        self.posicionActual=posicion


class Imagen(Cuadro):
    def __init__(self, posicion, imagen):
        self._Cuadro__posicion = posicion
        self.imagen = self.dibujar(imagen)
        self.dimension = DIM
        self.lista_cuadros = list()
        self.cuadro_vacio = None

    def mover(self):
        self.cuadro_vacio.mover()

    def dibujar(self, imagen):
        return pygame.image.load(imagen)

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
            if listarand[i] == listapos[len(listapos)-1]:
                self.cuadro_vacio=\
                    CuadroVacio(Posicion(listarand[i][0],listarand[i][0]), "CuadroVacio.png")
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

    def intercambiar(self,posicion):
        for i in range(len(self.lista_cuadros)):
            if self.lista_cuadros[i].posicion.getX()==posicion[0] and self.lista_cuadros[i].posicion.getY()==posicion[1]:
                self.lista_cuadros[i].posicion.setX(self.cuadro_vacio.posicion.getX())
                self.lista_cuadros[i].posicion.setY(self.cuadro_vacio.posicion.getX())
        self.cuadro_vacio.posicion.setX(posicion[0])
        self.cuadro_vacio.posicion.setY(posicion[1])


class Contador:
    def __init__(self):
        self.numeroMovimientos = int(0)

    def aumentar(self):
        return self.numeroMovimientos + 1


class Colision:
    def __init__(self, contador, imagen):
        self.imagen=imagen
        self.contador = contador

    def verificarColision(self, posicion):
        for pos in self.imagen.lista_cuadros:
            if pos.getPosicionActual == posicion:
                self.contador.aumentar()
                self.imagen.intercambiar(posicion)


class Puntaje:
    def __init__(self, puntaje):
        self.puntaje = puntaje


class Puzzle:
    def __init__(self,imagen):
        self.imagen = imagen

    def iniciarJuego(self):
        pygame.init()
        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        titulo_juego = pygame.display.set_caption('I <3 PUZZLE')  # Se inserta un titulo a la ventana creada
        imagen.descomponer()
        clock = pygame.time.Clock()
        iniciado = True
        while iniciado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    iniciado = False
                pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                imagen.actualizarImagen(pantalla_juego)
                pygame.display.update()




imagen = Imagen(Posicion(0, 0), "plantilla.png")
contador=Contador()
puzzle = Puzzle(imagen)
colision = Colision(contador,imagen)
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
