from snake.Fabrica_Malware import Fabrica_Malware
from snake.Figura_Troyano import Figura_Troyano

class Fabrica_Troyano(Fabrica_Malware):

    def crearImagen(self, pos) -> Figura_Troyano:
        return Figura_Troyano(pos[0],pos[1])
