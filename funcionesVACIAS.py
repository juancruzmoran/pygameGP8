from principal import *
from configuracion import *
import random
import math
import chardet
#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    with open("lemario.txt", "rb") as archivo:
        contenido = archivo.read()
        deteccion = chardet.detect(contenido)
        codificacion = deteccion["encoding"]
    with open("lemario.txt", "r", encoding=codificacion) as archivo:
        palabras = archivo.read().splitlines()
    return palabras
#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)

def dame7Letras():
    vocales = "aeiou"
    consonantes_faciles = "bcdfghjlmnpqrstvw"
    consonantes_dificiles = "kxyz"

    letras = []
    # Agregar 2 o 3 vocales
    num_vocales = random.randint(2, 3)
    letras.extend(random.choices(vocales, k=num_vocales))

    # Agregar consonantes fáciles hasta completar 7 caracteres
    num_consonantes_faciles = 7 - num_vocales
    letras.extend(random.choices(consonantes_faciles, k=num_consonantes_faciles))

    # Agregar una consonante difícil si es posible
    if num_consonantes_faciles < 7 and random.random() < 0.5:
        letras.append(random.choice(consonantes_dificiles))

    # Mezclar las letras
    random.shuffle(letras)

    return "".join(letras)

def dameLetra(letrasEnPantalla):
    letra = random.choice(letrasEnPantalla)
    return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if candidata in diccionario:
        return Puntos(candidata)
    else:
        return -1

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if letraPrincipal not in candidata:
        return False
    for letra in candidata:
        if letra not in letrasEnPantalla:
            return False
    if candidata not in diccionario:
        return False
    return True

#devuelve los puntos
def Puntos(candidata):
    letras_puntuadas = ['a', 'e', 'i', 'o', 'u', 'n', 'r', 't', 'l', 's']
    puntos = 0
    for letra in candidata:
        if letra in letras_puntuadas:
            puntos += 1
    return puntos

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    return ['adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']
