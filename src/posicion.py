class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosicion(self):
        tupla = (self.x, self.y)
        return tupla

    def actualizarX(self, nuevoX):
        self.x = nuevoX

    def actualizarY(self, nuevoY):
        self.y = nuevoY
