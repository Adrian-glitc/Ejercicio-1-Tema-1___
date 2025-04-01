from receta import Receta
if __name__ == "__main__":
    texto_corrupto = "sainolac 052 anitnoc ed atecer al"
    receta = Receta(texto_corrupto)
    receta.procesar_texto()
    print(receta.obtener_resultado())
    