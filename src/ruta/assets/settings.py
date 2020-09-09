# cambie los valores x,y en tamañoVentana para que el juego se ajuste a su pantalla
tamañoVentana = ancho, alto = 900, 521 

tamañoCamino = int(ancho*0.5), alto
tamañoPersonaje = int(ancho*0.11), int(alto*0.18)
tamañoBoton = int(ancho*0.13), int(alto*0.1)
tamañoFigPregunta = int(ancho*0.5), int(alto*0.45)
tamañoFigVida = int(ancho*0.18), int(alto*0.07)
tamañoOpcion = int(ancho*0.1), int(alto*0.15)
tamañoMarcador = int(ancho*0.18), int(alto*0.07)

#Coordenadas de Posicion de Botones GUI
coordenadaBotonJugar = (ancho*0.7, alto*0.75)
coordenadaBotonAtras = (ancho*0.17), (alto*0.75)
coordenadaBotonOk = (ancho*0.45, alto*0.85)

#Coordenadas de Posicion de las Figuras
coordenadaCamino = (ancho*0.25,0)
coordenadaFondo = (0,0)
coordenadaPersonaje = (129*4, 100)
coordenadaFigVida = ( ancho*0.035, alto*0.08)
coordenadaFigPregunta = (ancho*0.55, alto*0.08)
coordenadaMarcador = ( ancho*0.8, alto*0.2)
coordenadaOpcion = [( ancho*0.3, alto*0.82), (ancho*0.45, alto*0.82), (ancho*0.6, alto*0.82)]

#para definir cuanto se desplazará el camino de manera de escala (en figuras.py, clase Mapa)
factorDesplazamiento = int(11*(ancho/1164))

settings = {
    "tamañoVentana": tamañoVentana,
    "tamañoCamino": tamañoCamino,
    "tamañoBoton": tamañoBoton,
    "tamañoPersonaje": tamañoPersonaje,
    "tamañoFigPregunta": tamañoFigPregunta,
    "tamañoFigVida": tamañoFigVida,
    "tamañoOpcion": tamañoOpcion,
    "tamañoMarcador": tamañoMarcador,
    "coordenadaFondo": coordenadaFondo,
    "coordenadaCamino": coordenadaCamino,
    "coordenadaPersonaje": coordenadaPersonaje,
    "coordenadaFigPregunta": coordenadaFigPregunta,
    "coordenadaOpcion": coordenadaOpcion,
    "coordenadaFigVida": coordenadaFigVida,
    "coordenadaMarcador": coordenadaMarcador,
    "coordenadaBotonJugar": coordenadaBotonJugar,
    "coordenadaBotonAtras": coordenadaBotonAtras,
    "coordenadaBotonOk": coordenadaBotonOk,
    "factorDesplazamiento": factorDesplazamiento,
    "nombre": "Juego Ruta Maya",
    "icon": "",
}
