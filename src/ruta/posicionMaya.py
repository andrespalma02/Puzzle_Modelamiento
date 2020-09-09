class PosicionRuta:
    def __init__(self, tupla):
        self.x, self.y = tupla[0], tupla[1]

    def getPosicion(self):
        return self.x, self.y

    def actualizarX(self, nuevoX):
        self.x = nuevoX

    def actualizarY(self, nuevoY):
        self.y = nuevoY
