from juego import *
import pygame
import os
import sys
from ruta.figuras import *
from ruta.posicionMaya import *
from ruta.mensaje import *
from ruta.solapamiento import *
from ruta.assets.settings import *
from ruta.boton import *
from ruta.audioPregunta import *
from ruta.puntaje import *
sys.path.append('../juego.py')


class Ruta(Juego):
    def __init__(self):
        self.mapa = Mapa
        self.puntaje = PuntajeRuta        

    def mostrarMensajesIniciales(self):
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])
           # Mensajes iniciales GUI
        mensajeBienvenida = MensajeRuta(
            'img/fondoBienvenida.png', PosicionRuta((0, 0)))
        mensajeInstrucciones = MensajeRuta(
            'img/fondoInstrucciones.png', PosicionRuta((0, 0)))
        btnJugar = BotonRuta('JUGAR', PosicionRuta(
            settings["coordenadaBotonJugar"]))
        btnAtras = BotonRuta('ATRAS', PosicionRuta(
            settings["coordenadaBotonAtras"]))
        btnOk = BotonRuta('OK', PosicionRuta(settings["coordenadaBotonOk"]))
        mensajeBienvenida.agregarBoton(btnJugar)
        mensajeBienvenida.agregarBoton(btnAtras)
        mensajeInstrucciones.agregarBoton(btnOk)
        mensajeBienvenida.mostrar(self.ventana)
        mensajeInstrucciones.mostrar(self.ventana)


    def iniciarJuego(self):
        self.mostrarMensajesIniciales()
        
        # preconfiguraciones
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])
        pygame.display.set_caption(settings["nombre"])
        rutamayainiciado = True
        self.mapa = Mapa()

        audioPruebaSonido = AudioPregunta('sounds/p1.wav', "A")

        verificacion = VerificacionRuta(audioPruebaSonido, self.mapa)

        solapamientoOpcionA = SolapamientoRuta(30, verificacion)
        solapamientoOpcionB = SolapamientoRuta(30, verificacion)
        solapamientoOpcionC = SolapamientoRuta(30, verificacion)

        solapamientos = [solapamientoOpcionA,
                         solapamientoOpcionB, solapamientoOpcionC]

        self.mapa.agregarFigura(
            Fondo('img/fondoJuego.png', PosicionRuta(settings["coordenadaFondo"])))
        camino = Camino('img/fondoCamino.png',
                        PosicionRuta(settings["coordenadaCamino"]))
        self.mapa.agregarFigura(camino)
        self.mapa.agregarFigura(FiguraVida(
            PosicionRuta(settings["coordenadaFigVida"])))
        self.mapa.agregarFigura(Marcador('img/marcador.png',
                                    PosicionRuta(settings["coordenadaMarcador"]), 0))
        self.mapa.agregarFigura(Personaje(
            'img/personaje.png', PosicionRuta(settings["coordenadaPersonaje"]), solapamientos))

        opcionA = FiguraOpcion(
            'img/botonA.png', PosicionRuta(settings["coordenadaOpcion"][0]), "A", solapamientoOpcionA)
        opcionB = FiguraOpcion(
            'img/botonB.png', PosicionRuta(settings["coordenadaOpcion"][1]), "B", solapamientoOpcionB)
        opcionC = FiguraOpcion(
            'img/botonC.png', PosicionRuta(settings["coordenadaOpcion"][2]), "C", solapamientoOpcionC)

        self.mapa.agregarFigura(opcionA)
        self.mapa.agregarFigura(opcionB)
        self.mapa.agregarFigura(opcionC)

        while rutamayainiciado:
            self.mapa.mover(self.ventana)
            self.mapa.dibujar(self.ventana)
            audioPruebaSonido.reproducir(camino, self.mapa.obtenerOpciones())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rutamayainiciado = False
                    pygame.quit()
            pygame.display.update()

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
