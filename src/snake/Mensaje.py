import pygame
import os.path

mensajeMenu= pygame.image.load(os.path.join(os.path.dirname(__file__), "img/MensajeMenu.png"))
mensajeMenu = pygame.transform.scale(mensajeMenu, (768, 512))
mensajeVida= pygame.image.load(os.path.join(os.path.dirname(__file__), "img/MensajeVida.png"))
mensajePerdida= pygame.image.load(os.path.join(os.path.dirname(__file__), "img/MensajePerdida.png"))

class Mensaje(object):

    def __init__(self):
        self.imagenMenu = [mensajeMenu,False]#Cambiar.
        self.imagenVida = [mensajeVida,False]#Cambiar.
        self.imagenPerdida=[mensajePerdida,False]
    #Definir la imagen y la posición.

    def dibujar(self,ventana):
        if self.imagenMenu[1]:
            ventana.blit(self.imagenMenu[0], (0,0))
        elif self.imagenVida[1]:
            ventana.blit(self.imagenVida[0], (133,94))
        elif self.imagenPerdida[1]:
            ventana.blit(self.imagenPerdida[0], (133,94))

    def estadoMensaje(self,estado):
        self.imagenMenu[1]=estado[0]
        self.imagenVida[1]=estado[1]
        self.imagenPerdida[1]=estado[2]
