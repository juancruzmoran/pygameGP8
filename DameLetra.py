import random

def dameLetra(letrasEnPantalla):
    # Seleciona una letra aleatoria dentro de la cadena
    indice = random.randint(0, len(letrasEnPantalla) - 1)

    # Segun la letra obtenida, la devuelve
    letra = letrasEnPantalla[indice]

    # Devuelve la letra seleccionada
    return letra
