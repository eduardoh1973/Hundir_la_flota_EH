from utils import crear_tablero, colocar_barcos, disparar, crear_lista_barcos, crear_barco_eslora

#variables jugador
tablero_jugador_disparos = crear_tablero() #tablero donde se marcan los disparos del jugador.
tablero_jugador_barcos = crear_tablero() #tablero donde se marcan los barcos del jugador.
lista_disparos_jugador = []

#variables rival
tablero_rival_disparos = crear_tablero() 
tablero_rival_barcos = crear_tablero()
lista_disparos_rival = []

#funcion de pedir barcos al jugador y al rival
lista_barcos_jugador = [[(0,1),(0,2)], [(3,4),(4,4),(5,4)]]
lista_barcos_rival = [[(3,1),(3,2)], [(3,7),(4,7),(5,7)]]

print("tablero_jugador (vacio):")
print(tablero_jugador_barcos)
print("-------------")

#colocar barcos jugador 
tablero_jugador_barcos = colocar_barcos((lista_barcos_jugador), tablero_jugador_barcos) #aleatorio sería tablero_jugador_barcos = colocar_barcos((barco), tablero_jugador_barcos)
#colocar barcos rival
tablero_rival_barcos = colocar_barcos((lista_barcos_rival), tablero_rival_barcos)

print("tablero jugador con barcos:")
print(tablero_jugador_barcos)
print("----------------")


#Turno del jugador
print("Tira el jugador")
repite = True
while repite:
    repite = disparar(tablero_rival_barcos)


