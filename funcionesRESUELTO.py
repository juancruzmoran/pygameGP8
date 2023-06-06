from principal import *
from configuracion import *
import random
import math

# Lee el archivo y carga en la lista "diccionario" todas las palabras
def lectura(diccionario):
        with open("/diccionario.txt", "r") as file:
         for line in file:
            diccionario.append(line.strip())

# Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo con una consonante difícil (kxyz)
def dame7Letras():
    vocales = "aeiou"
    consonantes = "bcdfghjlmnpqrstvwxyz"
    letras = ""
    contador_vocales = 0
    contador_consonantes_dificiles = 0

    while len(letras) < 7:
        if contador_vocales < 2 or contador_vocales == 2 and contador_consonantes_dificiles < 1:
            letra = random.choice(vocales)
            contador_vocales += 1
        else:
            letra = random.choice(consonantes)
            contador_consonantes_dificiles += 1

        if letra not in letras:
            letras += letra

    return letras

# Elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla):
    return random.choice(letrasEnPantalla)

# Si es válida la palabra, devuelve puntos; sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
        return Puntos(candidata)
    else:
        return -1

# Chequea que se use la letra principal, solo use letras de la pantalla y
# exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if letraPrincipal not in candidata:
        return False

    for letra in candidata:
        if letra not in letrasEnPantalla:
            return False

    return candidata in diccionario

# Devuelve los puntos
def Puntos(candidata):
    longitud = len(candidata)
    if longitud >= 8:
        return 10
    elif longitud >= 6:
        return 7
    elif longitud >= 4:
        return 5
    else:
        return 1

# Busca en el diccionario palabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabras_correctas = []

    for palabra in diccionario:
        if letraPrincipal in palabra:
            letras_validas = letrasEnPantalla.copy()
            es_valida = True

            for letra in palabra:
                if letra in letras_validas:
                    letras_validas.remove(letra)
                else:
                    es_valida = False
                    break

            if es_valida:
                palabras_correctas.append(palabra)

    return palabras_correctas