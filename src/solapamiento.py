from herramientas import *

class Solapamiento:

    def __init__(self, mapaMuseo):
        self.mapa = mapaMuseo

    def verificar(self, posiblePos):
        return self.verificarCamino(posiblePos) or self.verificarEstacion(posiblePos)

    def verificarCamino(self, posiblePos):
        dict = self.mapa.accederLista()
        for piso in dict['camino']:
            if piso.obtenerPosicion() == posiblePos:
                return True
        return False

    def verificarEstacion(self, posiblePos):
        dict = self.mapa.accederLista()
        for estacion in dict['estaciones']:
            if estacion.obtenerPosicion() == posiblePos:
                for mensaje in dict['mensaje']:
                    if mensaje.getNombre() == estacion.getNombre():
                        mensaje.permitirDibujo(True)
                        try:
                            ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"r")
                            puntuacion = ppNiña.readline().split(",")[2]
                            ppNiña.close()
                            ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"w")
                            ppNiña.write(str(posiblePos[0]) + "," + str(posiblePos[1]) + "," + str(puntuacion))
                            ppNiña.close()
                        except IOError:
                            print("Error al manejar el archivo")
                return True
        return False
