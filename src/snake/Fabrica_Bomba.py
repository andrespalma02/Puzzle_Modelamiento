from snake.Fabrica_Malware import Fabrica_Malware
from snake.Figura_Bomba import Figura_Bomba

class Fabrica_Bomba(Fabrica_Malware):

    def crearImagen(self, pos) -> Figura_Bomba:
        return Figura_Bomba(pos[0],pos[1])
