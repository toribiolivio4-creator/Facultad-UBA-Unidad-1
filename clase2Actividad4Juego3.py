import random

jugador1 = input("Jugador 1 ngrese su nombre: ")
jugador2 = input("Jugador 2 ingrese su nombre: ")
prenda1 = input("Ingrese prenda Jugador 1: ")
prenda2 = input("Ingrese prenda Jugador 2: ")

moneda1 = random.randint(1,2)
moneda2 = random.randint(1,2)

if moneda1 == 1 and moneda2 == 1:
    print("Ganaste " + jugador1)
else:
    print("Ganaste " + jugador2)           
