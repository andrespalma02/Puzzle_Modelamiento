class SolapamientoLaberinto:

    def __init__(self, tablero):
        self.tablero = tablero

    def verificar(self, posiblePos):
        caminoB = False
        virusB = False
        metaB = False
        dict = self.tablero.dictCuadros
        for piso in dict['camino']:
            (pisoX, pisoY) = (piso.posicion.x, piso.posicion.y)
            if (pisoX, pisoY) == posiblePos:
                caminoB = True
        for virus in dict['virus']:
            (virusX, virusY) = (virus.posicion.x, virus.posicion.y)
            if (virusX, virusY) == posiblePos:
                dict['personaje'].numeroVidas -= 1
                corazon = dict['personaje'].numeroVidas
                dict['vidas'][corazon].lleno = 0
                if dict['personaje'].numeroVidas == 0:
                    for mensaje in dict['mensaje']:
                        if mensaje.getNombre() == 'perdida':
                            mensaje.permitirDibujo(True)
                virusB = True
        (metaX, metaY) = (dict['meta'].posicion.x, dict['meta'].posicion.y)
        if (metaX, metaY) == posiblePos:
            for mensaje in dict['mensaje']:
                if mensaje.getNombre() == 'victoria':
                    mensaje.permitirDibujo(True)
            metaB = True
        return caminoB or virusB or metaB
