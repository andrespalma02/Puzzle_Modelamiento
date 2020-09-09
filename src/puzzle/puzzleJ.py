import pygame
import os
import sys
sys.path.append('../juego.py')
from juego import *
from puzzle.puzzle import *

class Puzzle(Juego):

    def __init__(self):
        pygame.init()
        self.dimensiones = (500,500)
        self.titulo = 'I <3 PUZZLE'
        self.ventana = None
        self.clock = pygame.time.Clock()
        self.fondo = None

    def iniciarJuego(self):
        CUADROVACIO_PATH = 'puzzle/CuadroVacio.png'
        MONITOR_PATH = 'puzzle/ImagenMonitor.png'

        titulo_juego = pygame.display.set_caption(self.titulo) 
        imagen=Imagen()
        imagen.dibujar(Posicion(0, 0), MONITOR_PATH)
        imagen.descomponer()
        puzzle = Puzzle()
        puntaje = Puntaje(puzzle)
        verificacion = Verificacion(imagen, puntaje)
        contador = Contador(verificacion)
        colision = Colision(contador, imagen)
        self.ventana = pygame.display.set_mode(self.dimensiones)

        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        self.fondo = self.ventana.fill((255, 255, 255))  # Dar un color blanco a la pantalla
        pygame.display.set_caption(self.titulo)

        iniciado = True
        while iniciado:
            
            try:
                self.clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        iniciado=False
                        pygame.quit()
                        break
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.reiniciarJuego()
                        if event.key == pygame.K_SPACE:
                            iniciado=False
                            self.salirJuego()
                            break

                    if puntaje.puntajeFinal != 0:
                        ctypes.windll.user32.MessageBoxW(0, "TU PUNTAJE OBTENIDO FUE:" + str(puntaje.puntajeFinal)
                                                        , "FELICIDADES GANASTE!!", 1)                  
                        pygame.quit()
                        puzzle.finalizarJuego()
                        iniciado = False
                    
                pantalla_juego.fill((255, 255, 255)) 
                imagen.mover(colision)
                imagen.actualizarImagen(pantalla_juego)
                pygame.display.update()    

            except Exception:
                break

 
    def reiniciarJuego(self):
        pygame.quit()
        self.iniciarJuego()

    def salirJuego(self):
        pygame.quit()
