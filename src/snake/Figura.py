from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def dibujar(self) -> object:
        pass
        
    @abstractmethod
    def obtenerValor(self) -> object:
        pass

    @abstractmethod
    def obtenerPosicion(self) -> object:
        pass
