from snake.Fabrica_Malware import Fabrica_Malware
from snake.Figura_Spyware import Figura_Spyware

class Fabrica_Spyware(Fabrica_Malware):

    def crearImagen(self, pos) -> Figura_Spyware:
        return Figura_Spyware(pos[0],pos[1])
