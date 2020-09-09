import os


# Este método permite obtener una dirección absoluta de un fichero o archivo
def obtenerPathAbsoluto(pathRelativo):
    pathAbsolutoScript = os.path.dirname(__file__)
    pathAbsoluto = os.path.join(pathAbsolutoScript, pathRelativo)
    return pathAbsoluto