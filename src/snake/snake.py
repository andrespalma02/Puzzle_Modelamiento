import pygame
from snake.Control_Movimiento import *
from snake.Mensaje import *
from snake.Ventana import *
class Snake(object):
    def __init__(self):
        self.ventana=None
        self.velocidad=3
        self.vidas=2
        self.puntuacion=0

    def iniciarJuego(self):
        pygame.init()
        mensaje=Mensaje()
        self.ventana=Ventana()
        mapa=self.ventana.obtenerMapa()
        cabeza=mapa.obtenerComponentes()[0]
        cola=mapa.obtenerComponentes()[1]
        malware=mapa.obtenerMalware()
        pantalla=self.ventana.cargarPantalla()#pygame
        run=mapa.verificarColision(self.ventana.obtenerLimites(),malware.obtenerPosicion())
        limiteVentanaX=self.ventana.obtenerLimites()[0]
        limiteVentanaY=self.ventana.obtenerLimites()[1]
        clock= pygame.time.Clock()
        bandera=True
        mensaje.estadoMensaje((True,False,False))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return True
            if keys[pygame.K_RETURN]:
                break
        while bandera and self.vidas>=0:
            clock.tick(self.velocidad)
            while not run[1]:
                clock.tick(self.velocidad)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return True
                cabeza.mover(limiteVentanaX,limiteVentanaY)
                run=mapa.verificarColision(self.ventana.obtenerLimites(),malware.obtenerPosicion())
                if run[0]:
                    malware=mapa.obtenerMalware()
                    #self.modificarPuntuacion(malware.obtenerValor())
                    #añada un segmentpo de cola
                    self.ventana.dibujarFondo(pantalla)
                    malware.dibujar(pantalla)
                    mapa.dibujarMapa(pantalla)
                    cola.agregarSegmento(cabeza.obtenerPosicion())
                else:
                    self.ventana.dibujarFondo(pantalla)
                    malware.dibujar(pantalla)
                    mapa.dibujarMapa(pantalla)
                    cola.mover(cabeza.obtenerPosicion())
                pygame.display.update()


            self.vidas-=1
            cabeza.retornarPosicion(limiteVentanaX,limiteVentanaY)
            mapa.dibujarMapa(pantalla)
            #mostrar el mensaje
            if self.vidas>=0:
                mensaje.estadoMensaje((False,True,False))
                mensaje.dibujar(pantalla)
            else:
                mensaje.estadoMensaje((False,False,True))
                mensaje.dibujar(pantalla)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return True
                keys = Control_Movimiento.detectarMovimiento()
                if keys[pygame.K_ESCAPE]:
                    bandera=False
                    break
                elif keys[pygame.K_SPACE] and self.vidas>=0:
                    break
                elif keys[pygame.K_RETURN] and self.vidas<0:
                    self.reiniciar(cola)
                    break
            cabeza.cambiarPosicion(0,-64)
            self.ventana.dibujarFondo(pantalla)
            malware.dibujar(pantalla)
            mapa.dibujarMapa(pantalla)
            pygame.display.update()
            for segmento in cola.obtenerCola():
                segmento.cambiarPosicion((-128,-128))
            run=[False,False]
        pygame.quit()
        return True

    def reiniciar(self,cola):
        long= len(cola.obtenerCola())
        self.vidas=2
        for i in range(long):
            cola.quitarUltimo()
        """
    def modificarPuntuacion(self,valor):
        self.puntuacion+=valor

    def cambiarVelocidad(self,valor):
        self.velocidad=valor
        """
