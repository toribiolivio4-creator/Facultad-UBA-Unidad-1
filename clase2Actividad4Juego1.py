import random
print("Juego de la moneda")
jugador1 = input("Jugador 1 ngrese su nombre: ")
jugador2 = input("Jugador 2 ingrese su nombre: ")
prenda1 = input("Ingrese prenda Jugador 1: ")
prenda2 = input("Ingrese prenda Jugador 2: ")

numero_aleatorio = random.randint(1,2)

if numero_aleatorio == 1:
    print("Ganaste " + jugador1 + " por lo que " + jugador2 + " vas a tener que cumplir la siguiente prenda: " + prenda1)
else:
    print("Ganaste " + jugador2 + " por lo que  " + jugador1 + " vas a tener que cumplir la siguiente prenda: " + prenda2)    
