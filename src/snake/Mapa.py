import pygame
from snake.Colision import Colision
from snake.Fabrica_Troyano import Fabrica_Troyano
from snake.Fabrica_Spyware import Fabrica_Spyware
from snake.Fabrica_Bomba import Fabrica_Bomba
from random import randint
from snake.Cabeza import Cabeza
from snake.Cola import Cola



class Mapa(object):

    def __init__(self):
        self.cabeza = Cabeza(0,0,64,64)
        self.cola=Cola()

    def obtenerMalware(self):
        pos = (randint(0,11)*64, randint(0,7)*64)
        bandera = True
        while bandera:
            bandera=False
            for segmento in self.cola.obtenerCola():
                if segmento.obtenerPosicion() == pos or self.cabeza.obtenerPosicion() == pos:
                    pos = (randint(0,11)*64, randint(0,7)*64)
                    bandera=True

        aleatorio=randint(0,100)
        if aleatorio >=0 and aleatorio <=33:
            return Fabrica_Troyano().crearImagen(pos)

        elif aleatorio >33 and aleatorio <=66:
            return Fabrica_Spyware().crearImagen(pos)

        else:
            return Fabrica_Bomba().crearImagen(pos)


    def verificarColision(self,limVentana,posMalware):
        run=[False,False]
        posCabeza=self.cabeza.obtenerPosicion()
        cola=self.cola.obtenerCola()
        run[0]= Colision().colisionarCabezaMalware(posCabeza,posMalware )
        run[1]=Colision().colisionarCabezaVentana(posCabeza,limVentana[0],limVentana[1]) or Colision().colisionarCabezaSegmento(posCabeza,cola)
        return run

    def dibujarMapa(self, ventana):
        self.cola.dibujar(ventana)
        self.cabeza.dibujar(ventana)

    def obtenerComponentes(self):
        return (self.cabeza,self.cola)
