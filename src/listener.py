import pygame

pygame.init()


class Listener:
    @staticmethod
    def detectar() -> tuple:
        return pygame.key.get_pressed()
