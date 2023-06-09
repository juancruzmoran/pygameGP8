from principal import *
from configuracion import *
import random
import math

# Toma un diccionario como parámetro. Lee palabras del archivo "lemario.txt" y las agrega al diccionario. La función devuelve el diccionario actualizado.
def lectura(diccionario):
    lemario = "lemario.txt"
    with open(lemario,"r",encoding="latin-1") as archivo:
        for linea in archivo:
            palabra = linea.rstrip('\n')
            diccionario.append(palabra)
    return diccionario

diccionario = []

#Toma como parámetros 3 listas de letras, crea una cadena, agregar las letras con ciertas condiciones, y luego las desordena y retorna la cadena desordenada
def dame7Letras(list1,list2,list3): 
    cadena=""
    vocales=random.sample(list2, random.randint(2, 3)) 
    cadena=cadena+"".join(vocales) 

    cantidadDeLetras=4 if len(vocales)==2 else 3 
    letras=random.sample(list1,cantidadDeLetras) 
    cadena=cadena+"".join(letras) 

    consonanteDif=random.choice(list3)
    cadena=cadena+"".join(consonanteDif) 

    desordenarCadena=random.sample(cadena,len(cadena)) 
    cadenaDesordenada="".join(desordenarCadena) 

    return cadenaDesordenada

letras=["b","c","d","f","g","h","j","l","m","n","p","q","r","s","t","u","v","w"]
vocales=["a","e","i","o","u"]
consonanteDif=["k","x","y","z"]

dame7Letras(letras,vocales,consonanteDif) 

#Elige y devuelve una letra de la cadena que recibe (letras en pantalla).
def dameLetra(letrasEnPantalla): 
    cadena=letrasEnPantalla 
    letraAleatoria=random.choice(cadena) 

    return letraAleatoria

#Si la palabra cumple con los requisitos suma puntos, sino resta
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if len(candidata)>=3 and letraPrincipal in candidata and candidata in diccionario:
        return puntos(candidata)
    else:
        return -1

#chequea que se use la letra principal, solo use letras de la pantalla y exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if letraPrincipal in candidata:
        for letra in candidata:
            if letra not in letrasEnPantalla:
                return False
        if candidata in diccionario:
            return True
    return False

#devuelve los puntos:
def puntos(candidata):

    if len(candidata)==3:
        return(1)
    if len(candidata)==4:
        return(2)
    if len(candidata)==5 or len(candidata)==6:
        i=1
        for i in range(len(candidata)):
            i=i+1
        return(i)
    if len(candidata)==7:
        return(10)
    else:
        return(-1)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    algunasCorrectas = []
    cont=0  # Variable para contar las palabras encontradas
    for palabra in diccionario:
        if letraPrincipal in palabra:
            todasCumplen=True
            for letra in palabra:
                if letra not in letrasEnPantalla:
                    todasCumplen=False
                    break
            if todasCumplen:
                algunasCorrectas.append(palabra)
    return algunasCorrectas
