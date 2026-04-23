from utils import crear_tablero, colocar_barcos, disparar, crear_lista_barcos, crear_barco_eslora
import random

#variables jugador
tablero_jugador_disparos = crear_tablero() #tablero donde se marcan los disparos del jugador.
tablero_jugador_barcos = crear_tablero() #tablero donde se marcan los barcos del jugador.
lista_disparos_jugador = []

#variables rival
tablero_rival_disparos = crear_tablero() 
tablero_rival_barcos = crear_tablero()
lista_disparos_rival = []

#funcion de pedir barcos al jugador y al rival
lista_barcos_jugador = crear_lista_barcos()
lista_barcos_rival = crear_lista_barcos()

print("tablero_jugador (vacio):")
print(tablero_jugador_barcos)
print("-------------")

#colocar barcos jugador 
tablero_jugador_barcos = colocar_barcos(lista_barcos_jugador, tablero_jugador_barcos) #aleatorio sería tablero_jugador_barcos = colocar_barcos((barco), tablero_jugador_barcos)
#colocar barcos rival
tablero_rival_barcos = colocar_barcos(lista_barcos_rival, tablero_rival_barcos)

print("tablero rival con barcos:")
print(tablero_rival_barcos)
print("----------------")

print("tablero jugador con barcos:")
print(tablero_jugador_barcos)
print("----------------")

while True:
    #Turno del jugador
    print("Tira el jugador")
    while True:
        tocado = disparar(tablero_rival_barcos)
    
    
        print("\n--- Estado actual del tablero rival ---")
        print(tablero_rival_barcos)
        print("---------------------------------------\n")

        if not tocado:
             print("Agua, turno del rival")
             break
    
    # para terminar el juego:        
        if "o" not in tablero_rival_barcos:
             print("Fin del juego, has hundido todos los barcos")
             exit()

    #Turno del rival
    print("tira el rival")
    while True:
        #el rival tira aleatoriamente dentro de las coordenadas del tablero
        f, c = random.randint(0, 9), random.randint(0, 9) 
          
        if tablero_jugador_barcos[f, c] == "o":
            tablero_jugador_barcos[f, c] = "X"
            print("Tocado por tu rival")

        if "o" not in tablero_jugador_barcos:
                print("Fin del juego, el rival ha hundido todos tus barcos")
                exit()
        else:
            tablero_jugador_barcos[f, c] = "A"
            print("El rival ha disparado agua. Tu turno.")
            break 


    


