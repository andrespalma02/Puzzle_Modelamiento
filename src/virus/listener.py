import pygame

pygame.init()

class Listener():
    def detectar(self) -> tuple:
        return pygame.key.get_pressed()
