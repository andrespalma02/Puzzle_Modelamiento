import sys
sys.path.append('../juego.py')
from herramientas import *
from virus.cuadro import *
from virus.solapamiento import *
class Solapamiento:

    def __init__(self, Mapa, juego):
        self.mapa = Mapa
        self.juego = juego
        self.tipoCuadroSolapado = 'paginaNormal'
        self.pagina = None

    def verificarSolapamiento(self, coordenadaActual, nuevasCoordenadas):
        return self.verificarSolapamientoPaginaWeb(coordenadaActual, nuevasCoordenadas) or self.verificarSolapamientoCuadroObjetivo(coordenadaActual, nuevasCoordenadas)

    def verificarSolapamientoPaginaWeb(self, coordenadaActual, nuevasCoordenadas):
        for pagina in self.mapa.dictCuadros['cuadroPaginaWeb']:
            self.pagina = pagina
            posicion, esMalo = self.pagina.obtenerEstado() #obtener informacion de posicion y estado de un cuadro pagina web
            if posicion == nuevasCoordenadas and esMalo == False:
                #verifica que la pagina web a la que se va a mover no es un virus
                for pagina in self.mapa.dictCuadros['cuadroPaginaWeb']:
                    self.pagina = pagina
                    posicion, esMalo = self.pagina.obtenerEstado()
                    if posicion == coordenadaActual and esMalo == False: #busca el cuadro sobre el que se encuentra el personaje y lo transforma a un virus
                        paginaAcual = self.pagina
                self.tipoCuadroSolapado = 'paginaNormal'
                paginaAcual.transformar()
                self.notify()
                return True
            elif posicion == nuevasCoordenadas and esMalo == True:#verifica si el personaje se esta moviendo a un virus
            #notificar perdida del juego
                self.tipoCuadroSolapado = 'virus'
                self.notify()
                return True

        return False

    def verificarSolapamientoCuadroObjetivo(self, coordenadaActual, nuevasCoordenadas):
        for pagina in self.mapa.dictCuadros['cuadroPaginaWeb']:
            self.pagina = pagina
            posicion, esMalo = self.pagina.obtenerEstado() #obtener informacion de posicion y estado de un cuadro pagina web
            if posicion == coordenadaActual and esMalo == False: #busca el cuadro sobre el que se encuentra el personaje y lo transforma a un virus
                paginaAcual = self.pagina
        if self.mapa.dictCuadros['cuadroObjetivo'].getCoordenadas() == nuevasCoordenadas:
            paginaAcual.transformar()
            self.tipoCuadroSolapado = 'objetivo'
            self.notify()
            return True
        return False

    def notify(self):
        self.juego.update(self.tipoCuadroSolapado)
