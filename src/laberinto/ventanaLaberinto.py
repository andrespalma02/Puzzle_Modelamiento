import pygame
import laberinto.settingsLaberinto as s
from laberinto.cuadrosLaberinto import *
from laberinto.solapamientoLaberinto import *
from herramientas import *
from puntaje import *
pygame.init()
s.init()

CAMINOLAB_PATH = obtenerPathAbsoluto('laberinto/assets/CaminoLaberinto1.txt')
POSICION_VIRUS_PATH = obtenerPathAbsoluto('laberinto/assets/VirusLaberinto1.txt')
FONDO_PATH = obtenerPathAbsoluto('laberinto/img/Fondo_Laberinto.png')
PISO_PATH = obtenerPathAbsoluto('laberinto/img/Piso_Laberinto.png')
VIRUS_PATH = obtenerPathAbsoluto('laberinto/img/Virus.png')
META_PATH = obtenerPathAbsoluto('laberinto/img/Meta.png')
PERSONAJE_PATH = obtenerPathAbsoluto('laberinto/img/niña.png')
MENSAJES_PATH = obtenerPathAbsoluto('laberinto/assets/direccionesMensajesLaberinto.txt')
CORAZON_PATH = obtenerPathAbsoluto('laberinto/img/vida1.png')
CORAZON_VACIO_PATH = obtenerPathAbsoluto('laberinto/img/vida0.png')


class VentanaLaberinto:
    def __init__(self):
        self.dimensiones = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)
        self.titulo = "Laberinto"
        self.reloj = pygame.time.Clock()
        self.tablero = None
        self.solapamiento = None
        self.win = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)

    def cargarTablero(self):
        self.tablero = TableroLaberinto()
        self.tablero.agregarCuadros(FondoLaberinto(FONDO_PATH, PosicionLaberinto(0, 0)))

        with open(CAMINOLAB_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(CaminoLaberinto(PISO_PATH, posicion))

        with open(POSICION_VIRUS_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(VirusLaberinto(VIRUS_PATH, posicion))

        with open(MENSAJES_PATH) as f:
            for line in f:
                textos = line.strip().split(',')
                self.tablero.agregarCuadros(MensajeLaberinto(textos[0], textos[1]))

        self.tablero.agregarCuadros(PersonajeLaberinto(PERSONAJE_PATH, PosicionLaberinto(1 * s.dim_Cuadro, 0)))

        for vida in range(s.columnas - s.maximo_de_vidas, s.columnas):
            self.tablero.agregarCuadros(VidaLaberinto(CORAZON_VACIO_PATH, CORAZON_PATH, PosicionLaberinto(vida * s.dim_Cuadro, 0)))
        self.tablero.agregarCuadros(MetaLaberinto(META_PATH, PosicionLaberinto(20 * s.dim_Cuadro, 12 * s.dim_Cuadro)))
        self.solapamiento = SolapamientoLaberinto(self.tablero)

        self.tablero.dictCuadros['fondo'].dibujar(self.win)
        for camino in self.tablero.dictCuadros['camino']:
            camino.dibujar(self.win)
        for virus in self.tablero.dictCuadros['virus']:
            virus.dibujar(self.win)
        self.tablero.dictCuadros['meta'].dibujar(self.win)
        self.tablero.dictCuadros['personaje'].dibujar(self.win)
        for vida in self.tablero.dictCuadros['vidas']:
            vida.dibujar(self.win)
        for mensaje in self.tablero.dictCuadros['mensaje']:
            if mensaje.getNombre() == 'instrucciones':
                mensaje.permitirDibujo(True)
                mensaje.dibujar(self.win)
        pygame.display.update()

    def manejarMensajes(self, instr, juego):
        lstMsj = self.tablero.dictCuadros['mensaje']
        for m in lstMsj:
            if m.getAparecer():
                keys = ListenerLaberinto.detectar()
                if m.getNombre() == 'instrucciones' and keys[pygame.K_SPACE]:
                    m.permitirDibujo(False)
                    return True
                elif m.getNombre() == 'victoria' and keys[pygame.K_ESCAPE]:
                    juego.salirJuego()
                    return True
                elif m.getNombre() == 'perdida':
                    if keys[pygame.K_SPACE]:
                        juego.reiniciarJuego()
                        return True
                    elif keys[pygame.K_ESCAPE]:
                        juego.salirJuego()
                        return True
                return False
        return True
