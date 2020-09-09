import pygame

pygame.init()


class ListenerLaberinto:
    @staticmethod
    def detectar() -> tuple:
        return pygame.key.get_pressed()
