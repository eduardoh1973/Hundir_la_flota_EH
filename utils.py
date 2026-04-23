import numpy as np
import random 

def crear_tablero():
    tablero = np.full((10,10), " ")
    return tablero

def pedir_barcos_jugador():
    pos_inicial_f = int(input("fila"))
    pos_inicial_c = int(input("columna"))
    inicio = (pos_inicial_f, pos_inicial_c)

def colocar_barcos(lista_barcos, tablero):
    for i in lista_barcos:
        for j in i:
            tablero[j] ="o"
    return tablero

def disparar(tablero):
    while True:
        try:
            fila = int(input("fila: "))
            columna = int(input("columna: "))
            break
        except ValueError:
            print("Error: escriba un numero entero")

    if tablero[fila, columna] == "o":
        tablero[fila, columna] = "X"
        print("tocado")
        return True
    else:
        tablero[fila, columna] = "A"
        print("agua")
        return False
     
    
def crear_barco_eslora(eslora):
    tamaño = 10
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":
        fila = random.randint(0, tamaño - 1)
        col_inicio = random.randint(0, tamaño - eslora)
        return [(fila, col_inicio + i) for i in range(eslora)]

    else:
        fila_inicio = random.randint(0, tamaño - eslora)
        col = random.randint(0, tamaño - 1)
        return [(fila_inicio + i, col) for i in range(eslora)]


def crear_lista_barcos():
    lista_esloras = (2,2,2,3,3,4)
    lista_barcos = []

    for eslora in lista_esloras:
        barco = crear_barco_eslora(eslora)
        lista_barcos.append(barco)
    
    return lista_barcos


