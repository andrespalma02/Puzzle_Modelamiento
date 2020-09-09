from snake.Segmento_Cuerpo import Segmento_Cuerpo
class Colision():

    def colisionarCabezaMalware(self,posCabeza,posMalware):
        if posCabeza==posMalware:
            return True
        else:
            return False

    def colisionarCabezaVentana(self,posCabeza,limiteVentanaX,limiteVentanaY):
        if posCabeza[0] < 0 or posCabeza[0]>limiteVentanaX-64 or posCabeza[1] < 0 or posCabeza[1]>limiteVentanaY-64:
            return True
        else:
            return False

    def colisionarCabezaSegmento(self,posCabeza,cola):
        run = False
        if len(cola)>3:
            segmento : Segmento_Cuerpo
            for i in range (len(cola)):
                if cola[i].obtenerPosicion()==posCabeza:
                    run=True
                    break

        return run
