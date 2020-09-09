import pygame
from ruta.listener import *

class ListenerRuta:
    @staticmethod
    def captarMouse():
        return pygame.mouse.get_pos()
