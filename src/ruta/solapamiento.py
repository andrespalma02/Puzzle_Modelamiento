from ruta.figuras import *
from ruta.verificacion import *
import math

class SolapamientoRuta:
    def __init__(self, umbral, verificacion):
        self.umbral = umbral
        self.posicionOpcion = None
        self.letraSeleccionada = None
        self.verificacion = verificacion
        
    def verificar(self, posicionJugador):
        if self.posicionOpcion != None:
            (x1, y1) = posicionJugador
            (x2, y2) = self.posicionOpcion
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
            if distancia <= self.umbral:
                self.verificacion.verificarSeleccion(self.letraSeleccionada)
    
    def actualizar(self, posicionOpcion, letra):
        self.letraSeleccionada = letra
        self.posicionOpcion = posicionOpcion