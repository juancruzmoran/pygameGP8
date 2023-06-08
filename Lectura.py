def lectura(diccionario):
    try:
        with open("lemario.txt", "r") as archivo:
            for palabra in archivo:
                palabra = palabra.strip().lower()  # Eliminar espacios en blanco y convertir a minúsculas
                diccionario[palabra] = True
    except FileNotFoundError:
        print("No se encontró el archivo 'lemario.txt'.")

#f- Principal

diccionario = {}
lectura(diccionario)



#Comentario:

#Esto lo realize con un archivo en un texto que lo llame "lemario.txt", quedaria agegarlo en la el archivo, en el caso que utilicemos esta funcion :)