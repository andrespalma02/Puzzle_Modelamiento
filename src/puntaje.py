class Puntaje():
    def __init__(self, acumulador, maximo):
        self.acumulador = acumulador
        self.maximo = maximo

    def aumentar(self, puntaje):
        self.acumulador += puntaje

    def getMaximo(self):
        return self.maximo

    def getAcumulador(self):
        return self.acumulador
