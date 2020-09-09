import pygame
from abc import ABC, abstractmethod
from ruta.assets.herramientas import *
from ruta.assets.settings import *
from ruta.listener import *
from ruta.audioPregunta import *
from ruta.solapamiento import *

class Figura(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Fondo(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoVentana"])
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Camino(Figura):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoCamino"])
        self.estadoMovimiento = True
        
    def dibujar(self, ventana):
        posicion = self.posicion.getPosicion()
        ventana.blit(self.imagen, (posicion[0], settings["tamañoCamino"][1]))

    def mover(self, desplazamiento, ventana):
        if(self.estadoMovimiento):
            x, y = self.posicion.getPosicion()
            alturaImagen = self.imagen.get_rect().height
            relativoY = y % alturaImagen
            self.distancia = abs(y)
            if(self.distancia <= alturaImagen*3):
                ventana.blit(self.imagen, (x, relativoY - alturaImagen))
                if relativoY < settings['tamañoVentana'][1]:
                    ventana.blit(self.imagen, (x, relativoY))
                self.posicion.actualizarY(y-desplazamiento)
            else:
                ventana.blit(self.imagen, settings["coordenadaCamino"])
                self.estadoMovimiento = False
        else:
            ventana.blit(self.imagen, settings["coordenadaCamino"])

    def notificar(self):
        if(self.estadoMovimiento == False):
            return self.estadoMovimiento


class Personaje(Figura):

    def __init__(self, imagen, posicion, solapamiento):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoPersonaje"])
        self.solapamiento = solapamiento
        super().__init__(posicion)


    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        x, y = ListenerRuta.captarMouse()
        tamañoImagen = self.imagen.get_rect()
        distanciaVereda = (settings["tamañoVentana"][0] - settings["tamañoCamino"][0])/2
        condicionLimiteX = x >= distanciaVereda and x <= settings["tamañoVentana"][0] - distanciaVereda
        condicionLimiteY = y >= settings["tamañoVentana"][1] * 0.1 and y <= settings["tamañoVentana"][1]*0.9
        if(condicionLimiteX and condicionLimiteY):
            self.posicion.actualizarX(ListenerRuta.captarMouse()[0]-tamañoImagen.width/2)
            self.posicion.actualizarY(ListenerRuta.captarMouse()[1]-tamañoImagen.height/2)
        for solapamiento in self.solapamiento:
            solapamiento.verificar(self.posicion.getPosicion())    


class FiguraVida(Figura):
    def __init__(self, posicion):
        self.imagen = None
        self.posicion = posicion
        self.numeroVidas = 4

    def dibujar(self, ventana):
        if(self.numeroVidas == 4):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida4.png', __file__))
        else:
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida3.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoFigVida"])
        ventana.blit(self.imagen, self.posicion.getPosicion())
    
    def disminuirVidas(self):
        self.numeroVidas = self.numeroVidas - 1

    def mover(self):
        pass


class FiguraOpcion(Figura):
    def __init__(self, imagen, posicion, letraAsociada, solapamiento):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoOpcion"])
        self.posicion = posicion
        self.letraAsociada = letraAsociada
        self.solapamiento = solapamiento
        self.visibilidad = False

    def dibujar(self, ventana):
        if(self.visibilidad == True):
            ventana.blit(self.imagen, self.posicion.getPosicion())

    def setVisibilidad(self, esVisible):
        self.visibilidad = esVisible

    def mover(self):
        pass

    def notificar(self):
        if (self.visibilidad == True):
            self.solapamiento.actualizar(self.posicion.getPosicion(), self.getLetraAsociada())

    def getLetraAsociada(self):
        return self.letraAsociada

    def obtenerVisibilidad(self):
        return self.visibilidad



class Marcador(Figura):
    def __init__(self, imagen, posicion, puntaje):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoMarcador"])
        self.posicion = posicion
        self.puntaje = puntaje

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Mapa(Figura):
    def __init__(self):
        self.dictFiguras = dict()
        self.dictFiguras['fondo'] = None
        self.dictFiguras['camino'] = None
        self.dictFiguras['marcador'] = None
        self.dictFiguras['figuraVida'] = None
        self.dictFiguras['figuraOpcion'] = list()
        self.dictFiguras['personaje'] = None

    def agregarFigura(self, figura):
        if isinstance(figura, Camino):
            self.dictFiguras['camino'] = figura
        elif isinstance(figura, Marcador):
            self.dictFiguras['marcador'] = figura
        elif isinstance(figura, Fondo):
            self.dictFiguras['fondo'] = figura
        elif isinstance(figura, Personaje):
            self.dictFiguras['personaje'] = figura
        elif isinstance(figura, FiguraVida):
            self.dictFiguras['figuraVida'] = figura
        elif isinstance(figura, FiguraOpcion):
            self.dictFiguras['figuraOpcion'].append(figura)

    def quitarFigura(self):
        pass

    def dibujar(self, ventana):
        for key in self.dictFiguras:
            if key != 'figuraOpcion' and key != 'personaje':
                self.dictFiguras[key].dibujar(ventana)
        for opcion in self.dictFiguras['figuraOpcion']:
            opcion.dibujar(ventana)
            opcion.notificar()
        self.dictFiguras['personaje'].dibujar(ventana)

    def mover(self, ventana):
        self.dictFiguras['camino'].mover(settings["factorDesplazamiento"], ventana)
        self.dictFiguras['personaje'].mover()
        pygame.mouse.set_visible(False)

    def obtenerOpciones(self):
        return self.dictFiguras['figuraOpcion']
    
    def actualizar(self, comprobacion):
        if(comprobacion == True): 
            pass
        else:
            self.dictFiguras['figuraVida'].disminuirVidas()
            pass
            

