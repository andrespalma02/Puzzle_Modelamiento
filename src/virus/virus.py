import pygame
import os
import sys
sys.path.append('../juego.py')
from juego import *
from virus.cuadro import *
from virus.posicion import *


# NOTE: dado que las dimensiones de este juego son 600 x 550, se consideraran 24 columnas y 22 filas
# NOTE: las dimensiones de cada imagen que interactuara con el juego son de 25px por 25px
class EvitandoVirus(Juego):

    def __init__(self):
        pygame.init()
        self.dimensiones = (600,550)
        self.titulo = 'Esquivando Virus'
        self.ventana = None
        self.clock = pygame.time.Clock()
        self.mapa = None

    def iniciarJuego(self):
        INSTRUCCIONES = True
        FONTO_PATH = 'virus/img/Fondo.png'
        OBJETIVO_PATH = 'virus/img/cuadroObjetivo.png'
        WEB_PATH = 'virus/img/cuadroPagWeb.png'
        INST_PATH = 'virus/img/inicioVirus.png'
        PARED_PATH = 'virus/img/Pared.png'
        CAMINO_PATH = 'virus/assets/matrizCamino.dat'
        PAREDES = 'virus/assets/matrizPared.dat'
        PERSONAJE_PATH = 'virus/img/personaje.png'
        VIRUS_PATH = 'virus/img/cuadroVirus.png'
        MENSAJES_PATH = 'virus/assets/mensajes.dat'
        self.ventana = pygame.display.set_mode(self.dimensiones)
        self.mapa = Mapa(FONTO_PATH)
        pygame.display.set_caption(self.titulo)

        with open(PAREDES) as p:
            for line in p:
                info = line.strip().split(',')
                x = int(info[0])*25
                y = int(info[1])*25
                pared = CuadroPared(PARED_PATH, Posicion(x, y))
                self.mapa.agregarCuadros(pared)
        with open(CAMINO_PATH) as c:
            for line in c:
                info = line.strip().split(',')
                x = int(info[0])*25
                y = int(info[1])*25
                paginaWeb = CuadroPaginaWeb(WEB_PATH, VIRUS_PATH, Posicion(x,y))
                self.mapa.agregarCuadros(paginaWeb)
        with open(MENSAJES_PATH) as m:
            for line in m:
                datos = line.strip().split(',')
                mensaje = Mensaje(datos[0], datos[1], Posicion(0,0))
                self.mapa.agregarCuadros(mensaje)
        objetivo = CuadroObjetivo(OBJETIVO_PATH, Posicion(18*25,15*25))
        self.mapa.agregarCuadros(objetivo)
        solapamiento = Solapamiento(self.mapa, self)
        personaje = CuadroPersonaje(PERSONAJE_PATH, Posicion(18*25,5*25), solapamiento)
        self.mapa.agregarCuadros(personaje)

        self.mapa.dibujar(self.ventana)
        objetivo.dibujar(self.ventana)
        for camino in self.mapa.dictCuadros['cuadroPaginaWeb']:
            camino.dibujar(self.ventana)
        for pared in self.mapa.dictCuadros['cuadroPared']:
            pared.dibujar(self.ventana)
        personaje.dibujar(self.ventana)
        bandera=True
        while bandera:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
                    pygame.quit()
                    break
            lstmsj = self.mapa.dictCuadros['mensaje']
            msj = lstmsj[0]
            for m in lstmsj:
                if m.getNombre() == 'instrucciones' and INSTRUCCIONES:
                    m.autorizarDibujo(True)
                    INSTRUCCIONES = False
                    break
                if m.getAparecer():
                    msj = m
            try:
                msj.esperar(self)
            except:
                break

            if not msj.getAparecer():
                try:
                    self.mapa.dictCuadros['personaje'].mover(25)
                except:
                    break

            self.mapa.dibujar(self.ventana)
            objetivo.dibujar(self.ventana)
            for camino in self.mapa.dictCuadros['cuadroPaginaWeb']:
                camino.dibujar(self.ventana)
            for pared in self.mapa.dictCuadros['cuadroPared']:
                pared.dibujar(self.ventana)
            personaje.dibujar(self.ventana)
            for mensaje in self.mapa.dictCuadros['mensaje']:
                mensaje.dibujar(self.ventana)
            pygame.display.update()

    def reiniciarJuego(self):
        pygame.quit()
        self.iniciarJuego()

    def salirJuego(self):
        pygame.quit()

    def verificarCondiciones(self, tipoCuadroSolapado):
        """
        En base al tipo de cuadro solapado, determina si se gano o se perdio el juego
        """
        if tipoCuadroSolapado == 'objetivo':
            for mensaje in self.mapa.dictCuadros['mensaje']:
                if mensaje.getNombre() == 'victoria':
                    mensaje.autorizarDibujo(True)
        elif tipoCuadroSolapado == 'virus':
            for mensaje in self.mapa.dictCuadros['mensaje']:
                if mensaje.getNombre() == 'fallo':
                    mensaje.autorizarDibujo(True)
        else:
            pass

    def update(self, tipoCuadroSolapado):
        self.verificarCondiciones(tipoCuadroSolapado)
