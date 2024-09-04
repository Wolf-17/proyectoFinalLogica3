import random

def crearTablero(dimension):
    return[["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("\n Tablero de Disparos: ")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\n Tablero de disparos del oponente: ")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))

def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando {barco ['nombre']} de tamaño {barco['dimension']}")
                fila= int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                orientacion = input("Ingresa la orientacion (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice(['h', 'v'])

            if validarColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                colocarBarcos(tablero, fila, columna, barco['dimension'], orientacion)
                colocado = True
            elif jugador == "jugador":
                print("Colocacion es invalida, Intenta de nuevo")

def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if  orientacion == 'h':
        if columna + dimension > len(tablero):   
            return False
        for i in range(dimension):
            if tablero[fila][columna+i] != "~":
                return False
    else:
        if fila + dimension>len(tablero):
            return False
        for i in range(dimension):
             if tablero[fila+i][columna] != "~":
                return False
    return True

