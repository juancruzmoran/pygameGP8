def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    puntos = 0

    # Chequea si la palabra es valida
    if candidata in diccionario:
        # Verificar si la palabra contiene la letra principal
        if letraPrincipal in candidata:
            # Verificar si todas las letras de la palabra están en las letras en pantalla
            letrasValidas = True
            for letra in candidata:
                if letra not in letrasEnPantalla:
                    letrasValidas = False
                    break

            if letrasValidas:
                puntos = len(candidata)  # Puntos correspondientes a la longitud de la palabra

    if puntos > 0:
        return puntos
    else:
        return -1  # Acá resta 1 punto si la palabra no es valida
