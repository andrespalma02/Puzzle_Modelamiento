import pygame
from juego import *
import laberinto.settingsLaberinto as s
from laberinto.ventanaLaberinto import *
pygame.init()
s.init()
import os
import sys
sys.path.append('../juego.py')

bandera = True

class Laberinto(Juego):
    def __init__(self):
        self.ventana = None

    def iniciarJuego(self):
        self.ventana = VentanaLaberinto()
        self.ventana.cargarTablero()
        MOSTRAR_INSTRUCCIONES = True
        bandera = True

        while bandera:
            self.ventana.reloj.tick(s.FPS)
            manejo = self.ventana.manejarMensajes(MOSTRAR_INSTRUCCIONES, self)

            try:
                if manejo and bandera:
                    self.ventana.tablero.dictCuadros['personaje'].mover(s.velocidad, self.ventana.solapamiento)
                    self.ventana.tablero.dictCuadros['fondo'].dibujar(self.ventana.win)
                    for camino in self.ventana.tablero.dictCuadros['camino']:
                        camino.dibujar(self.ventana.win)
                    for virus in self.ventana.tablero.dictCuadros['virus']:
                        virus.dibujar(self.ventana.win)
                    self.ventana.tablero.dictCuadros['meta'].dibujar(self.ventana.win)
                    self.ventana.tablero.dictCuadros['personaje'].dibujar(self.ventana.win)
                    for vida in self.ventana.tablero.dictCuadros['vidas']:
                        vida.dibujar(self.ventana.win)
                    for mensaje in self.ventana.tablero.dictCuadros['mensaje']:
                        mensaje.dibujar(self.ventana.win)
                    pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        bandera = False
                        pygame.quit()
                        break
            except Exception:
                break

    def reiniciarJuego(self):
        bandera = False
        pygame.quit()
        pygame.init()
        self.iniciarJuego()

    def salirJuego(self):
        bandera = False
        pygame.quit()
