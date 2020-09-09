import os


# Este método permite obtener una dirección absoluta de un fichero o archivo
def obtenerPathAbsoluto(pathRelativo, file):
    pathAbsolutoScript = os.path.dirname(file)
    pathAbsoluto = os.path.join(pathAbsolutoScript, pathRelativo)
    return pathAbsoluto
