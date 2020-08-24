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

    def mover(self,rd):
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



nivel = 1       #Se selecciona el nivel
n = 2 + nivel   #se ingresa las dimensiones de los fragmentos del rompecabezas
dim = int(420 / n)  #Se asigna la dimension de los fragmentos en base al nivel actual
listapos = list()   #Se crea una lista con las posiciones correctas de los fragmentos
listarand = list()  #Se crea una lista con las posiciones desordenadas de los fragmentos

pygame.init()
cuadroVacio = CuadroVacio(Posicion(40 + (n - 1) * dim, 40 + (n - 1) * dim), "CuadroVacio.png") #Creacion del objeto cuadro vacio
listaimg = list() #Se crea una lista con los fragmentos de la imagen
imagen = pygame.image.load("plantilla.png") #Se carga la imagen completa para despues hacerla fragmentos

DIMENSION = 1000, 500 #Se define las dimensiones de la ventana del juego
pantalla_juego = pygame.display.set_mode(DIMENSION) #Se crea la ventana con las dimensiones especificas
titulo_juego = pygame.display.set_caption('I <3 PUZZLE')    #Se inserta un titulo a la ventana creada
clock = pygame.time.Clock()

for i in range(n):
    for j in range(n):
        posx = int(40 + j * dim)
        posy = int(40 + i * dim)
        listapos.append((posx, posy)) #Se guardan las posiciones correctas de los fragmentos
        listarand.append((posx, posy)) #Se guardan posiciones randomicas para los fragmentos
        imaux = pygame.Surface((dim, dim)) #Se crea una superficie
        imaux.blit(imagen, (0, 0), (posx -40, posy-40 , dim, dim))
        listaimg.append(imaux)

random.shuffle(listarand) #se generan posiciones randomicas de los fragmentos




iniciado = True
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
        cuadroVacio.mover(140)

        #Comparar las colisiones
        for cuadrofragmento in listapos:
            if cuadroVacio.posicion.getPosicion()==cuadrofragmento:
                print("COLISION")
                auxiliar = cuadroVacio.posicion.getPosicion()
                cuadroVacio.posicion.actualizar(cuadrofragmento[0],cuadrofragmento[1])
                cuadrofragmento =auxiliar

            else:
                pass






        pygame.display.flip()
        clock.tick(60)





    pygame.display.update()
