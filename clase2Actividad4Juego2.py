import random
print("Juego de la moneda!!")
jugador1 = input("Jugador 1 ngrese su nombre: ")
jugador2 = input("Jugador 2 ingrese su nombre: ")
prenda1 = input("Ingrese prenda Jugador 1: ")
prenda2 = input("Ingrese prenda Jugador 2: ")

numero_aleatorio = random.randint(1,2)
numero_aleatorio1 = random.randint(1,2)
numero_aleatorio2 = random.randint(1,2)


if numero_aleatorio == 1 and numero_aleatorio1 == 1 and numero_aleatorio2 == 1:
    print("Ganaste " + jugador1)
elif numero_aleatorio == 2 and numero_aleatorio1 == 2 and numero_aleatorio2 == 2:
    print("Ganaste " + jugador2)
elif numero_aleatorio == 1 and numero_aleatorio1 == 2 and numero_aleatorio2 == 2:
    print("Ganaste " + jugador2)
elif numero_aleatorio == 1 and numero_aleatorio1 == 1 and numero_aleatorio2 == 2:
    print("Ganaste " + jugador1)
elif numero_aleatorio == 1 and numero_aleatorio1 == 2 and numero_aleatorio2 == 1:
    print("Ganaste " + jugador1)
elif numero_aleatorio == 2 and numero_aleatorio1 == 1 and numero_aleatorio2 == 1:
    print("Ganaste " + jugador1)
elif numero_aleatorio == 2 and numero_aleatorio1 == 1 and numero_aleatorio2 == 2:
    print("Ganaste " + jugador2)
else:
    print("Error")                        
    
 
