from abc import ABC, abstractmethod
class Juego(ABC):
    @abstractmethod
    def iniciarJuego(self):
        pass

    @abstractmethod
    def reiniciarJuego(self):
        pass

    @abstractmethod
    def salirJuego(self):
        pass
