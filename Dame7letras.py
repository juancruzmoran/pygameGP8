import random

def dame7Letras():
    vocales = "aeiou"
    consonantesFaciles = "bcdfghjlmnpqrstvw"
    consonanteDificil = "kxyz"

    # ESto obtiene 2 o 3 vocales aleatoriamente
    NumVocales = random.randint(2, 3)
    letras = random.sample(vocales, NumVocales)

    #Busca obtener una consonante facil al azar
    letraConsonanteFacil = random.choice(consonantesFaciles)
    letras.append(letraConsonanteFacil)

   # Busca encontrar una consonante facil, opcionanlmente
    if random.randint(0, 1) == 0:
        letraConsonanteDificil = random.choice(consonanteDificil)
        letras.append(letraConsonanteDificil)

    # Rellena el resto de las letras con consonantes o vocales
    numLetrasRestantes = 7 - len(letras)
    for _ in range(numLetrasRestantes):
        if random.randint(0, 1) == 0:
            letra = random.choice(consonantesFaciles)
        else:
            letra = random.choice(vocales)
        letras.append(letra)

    # En esta parte mezcla las letras aleatoriamente
    random.shuffle(letras)

    # Convierte la lista en una letras en una cadeda
    resultado = ''.join(letras)
    return resultado

letras = dame7Letras()
print(letras)
