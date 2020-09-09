from ruta.figuras import *
from ruta.audioPregunta import *

class VerificacionRuta:
    def __init__(self, audioPregunta, mapa):
        self.mapa = mapa
        self.respuestaPregunta = audioPregunta.obtenerLetraRespuesta()

    def verificarSeleccion(self, letraSeleccionada):
        opciones = self.mapa.obtenerOpciones()
        for opcion in opciones:
            if(self.respuestaPregunta == letraSeleccionada):
                self.mapa.actualizar(True)
            else:
                self.mapa.actualizar(False)