from principal import *
from configuracion import *
import random
import math

#Lee el archivo lemario y las palabras que encuentra las agrega al diccionario
def lectura(diccionario):
    lemario = "lemario.txt"
    with open(lemario,"r",encoding="latin-1") as archivo:
        for linea in archivo:
            palabra = linea.rstrip('\n')
            diccionario.append(palabra)
    return diccionario

diccionario = []

#Toma 3 listas como parámetro, según las condiciones va agregrando letras de cada lista a una cadena, mezcla las letras y retorna la cadena. 
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

#elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla):
    cadena=letrasEnPantalla 
    letraAleatoria=random.choice(cadena) 

    return letraAleatoria 

#Esta funcion toma a la palabra del usuario y verifica que no haya salido (si ya salió resta), luego que cumpla los codicionales para otorgar los puntos y agregarla a la lista de palabras salidas.Si no cumple los requisitos, resta ptos.
palabrasSalidas=[]
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if candidata in palabrasSalidas:
        return -1
    elif len(candidata) >= 3 and letraPrincipal in candidata and candidata in diccionario:
        palabrasSalidas.append(candidata)
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

#devuelve los puntos
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
    cont=0  
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
