import pygame
from abc import *
import random
import ctypes
import pygame

NIVEL = 0
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

    def obtenerCoordenadas(self):
        return self.x, self.y

    def actualizarCoordenadas(self, x, y):
        self.x = x
        self.y = y


class Cuadro(ABC):
    def __init__(self, posicionRef, posicionAct):
        self.posicionReferencial = posicionRef
        self.posicionActual = posicionAct
        super().__init__()

    @property
    def posicionReferencial(self):
        return self.__posicionReferencial

    @property
    def posicionActual(self):
        return self.__posicionActual

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class CuadroVacio(Cuadro):

    def __init__(self, posicionR, imagen):
        self._Cuadro__posicionReferencial = posicionR
        self._Cuadro__posicionActual = None
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicionActual.getX(), self.posicionActual.getY()))

    def iniciarMovimiento(self, colision):
        keys = Listener.detectar()
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()

        if keys[pygame.K_LEFT]:
            colision.verificarColision((x + DIM, y))
        if keys[pygame.K_RIGHT]:
            colision.verificarColision((x - DIM, y))
        if keys[pygame.K_UP]:
            colision.verificarColision((x, y + DIM))
        if keys[pygame.K_DOWN]:
            colision.verificarColision((x, y - DIM))

    def mover(self, pos):
        self.posicionActual.setX(pos[0])
        self.posicionActual.setY(pos[1])

    def getPosicionActual(self):
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()
        return x, y

    def getPosicionRef(self):
        x = self.posicionReferencial.getX()
        y = self.posicionReferencial.getY()
        return x, y

    def setPosicionActual(self, posicion):
        self._Cuadro__posicionActual = Posicion(posicion[0], posicion[1])


class FragmentoImagen(Cuadro):

    def __init__(self, posicionR, imagen):
        self._Cuadro__posicionReferencial = posicionR
        self._Cuadro__posicionActual = None
        self.imagen = imagen
        self.estaOculto = False

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicionActual.getX(), self.posicionActual.getY()))

    def mover(self, pos):
        self.posicionActual.setX(pos[0])
        self.posicionActual.setY(pos[1])

    def getPosicionActual(self):
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()
        return x, y

    def getPosicionRef(self):
        x = self.posicionReferencial.getX()
        y = self.posicionReferencial.getY()
        return x, y

    def setPosicionActual(self, posicion):
        self._Cuadro__posicionActual = Posicion(posicion[0], posicion[1])

    def ocultar(self):
        self.estaOculto = True
        self.imagen = pygame.image.load("CuadroVacio.png")

    def verificarOcultamiento(self):
        return self.estaOculto


class Imagen(Cuadro):
    def __init__(self,contador,verificacion):
        self._Cuadro__posicion = None
        self.imagen = None
        self.dimension = DIM
        self.lista_cuadros = list()
        self.verificacion=verificacion
        self.contador=contador

    def mover(self, colision):
        self.lista_cuadros[-1].iniciarMovimiento(colision)

    def dibujar(self, posicion, imagen, pantalla):
        self.imagen = pygame.image.load(imagen)
        self._Cuadro__posicion = posicion

    def descomponer(self):
        listarand = list()
        for item in self.lista_cuadros:
            listarand.append(item.getPosicionRef())
        random.shuffle(listarand)
        i = int(0)
        for item in self.lista_cuadros:
            item.setPosicionActual(listarand[i])
            i += 1

    def actualizarImagen(self, ventana):
        for i in range(len(self.lista_cuadros)):
            self.lista_cuadros[i].dibujar(ventana)
        ventana.blit(self.imagen, (500, 40))

    def agregarCuadro(self, fragmentoimagen):
        self.lista_cuadros.append(fragmentoimagen)

    def intercambiar(self, posicion):

        listapos = list()
        for elemento in self.lista_cuadros:
            listapos.append((elemento.getPosicionActual(),elemento.getPosicionRef()))
            if (elemento.getPosicionActual() == posicion):
                self.contador.aumentar()
                elemento.mover(self.lista_cuadros[-1].getPosicionActual())
                self.contador.verificar(elemento)
        self.lista_cuadros[-1].mover(posicion)
        self.verificacion.verificarCondiciones(self.lista_cuadros)

class Contador:
    def __init__(self):
        self.numeroMovimientos = int(0)

    def aumentar(self):
        self.numeroMovimientos += 1
        print(self.numeroMovimientos)

    def verificar(self, fragmento):
        if (self.numeroMovimientos % 5 == 0) & (self.numeroMovimientos >= 5) & isinstance(fragmento,FragmentoImagen):
            fragmento.ocultar()

class Colision:
    def __init__(self, imagen):
        self.imagen = imagen

    def verificarColision(self, posicion):

        for pos in self.imagen.lista_cuadros:
            if pos.getPosicionActual() == posicion:
                self.imagen.intercambiar(posicion)
                break



class Verificacion:
    def __init__(self, puntaje):
        self.puntaje = puntaje

    def verificarCondiciones(self, listafragmentos):
        contG = 0
        contP=0
        for elemento in listafragmentos:
            if isinstance(elemento,FragmentoImagen):
                if elemento.verificarOcultamiento():
                    contP += 1
        if contP == len(listafragmentos)-1:
            self.puntaje.calcularPuntaje(False)

        for elemento in listafragmentos:
            if (elemento.getPosicionActual()==elemento.getPosicionRef()):
                contG += 1

        if contG == len(listafragmentos):
            self.puntaje.calcularPuntaje(True)


class Puntaje:

    def __init__(self,puzzle, contador):
        self.contador = contador
        self.puzzle=puzzle
        self.puntajeFinal = 0

    def calcularPuntaje(self,estado):
        if estado:
            self.puntajeFinal = int(100000 / self.contador.numeroMovimientos)
            print(self.puntajeFinal)
            return self.puntajeFinal
        else:
            print(self.puntajeFinal)
            return self.puntajeFinal
    def getpuntaje(self):
        return self.puntajeFinal

class Mensaje:
    pass

# ponle tipo juego en el constructor
class Puzzle():

    def iniciarJuego(self):

        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        titulo_juego = pygame.display.set_caption('I <3 PUZZLE')  # Se inserta un titulo a la ventana creada
        pygame.init()

        # Instancia de Contador
        contador = Contador()
        # Instancia de Puntaje
        puntaje = Puntaje(self, contador)
        # instancia de la imagen
        imagen = Imagen(contador, Verificacion(puntaje))
        # Instancia de Verificacion
        # Instancia de Colision
        colision = Colision(imagen)
        imagen.dibujar(Posicion(0, 0), "ImagenMonitor.png", pantalla_juego)

        # Instancias de los fragmentos
        listapos = list()
        listaimg = list()
        listaFragmentos = list()
        for i in range(N):
            for j in range(N):
                posx = int(40 + j * DIM)
                posy = int(40 + i * DIM)
                listapos.append((posx, posy))  # Se guardan las posiciones correctas de los fragmento
                imaux = pygame.Surface((DIM, DIM))  # Se crea una superficie
                imaux.blit(pygame.image.load("ImagenMonitor.png"), (0, 0), (posx - 40, posy - 40, DIM, DIM))
                listaimg.append(imaux)

        #Se agrega las listas de imagenes y las posiciones de referencia a la lista de Fragmentos
        for i in range(len(listapos)):
             listaFragmentos.append(FragmentoImagen(
                    Posicion(listapos[i][0], listapos[i][1]),
                    listaimg[i]))

        # Instancia del cuadro Vacio
        cuadro_vacio = CuadroVacio(Posicion(listapos[-1][0], listapos[-1][1]), "CuadroVacio.png")

        for i in range(len(listaFragmentos) - 1):
            imagen.agregarCuadro(listaFragmentos[i])

        imagen.agregarCuadro(cuadro_vacio)
        imagen.descomponer()
        clock = pygame.time.Clock()

        iniciado = True
        while iniciado:
            for event in pygame.event.get():
                pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                imagen.mover(colision)
                imagen.actualizarImagen(pantalla_juego)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    iniciado = False
                    pygame.quit()


    def finalizarJuego(self):
        pass

    def reiniciarJuego(self):
        pass


puzzle = Puzzle()
puzzle.iniciarJuego()