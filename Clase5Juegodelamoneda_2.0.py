import random
print("Juego de la moneda!!")
#print("Se tira la moneda 10 veces. Si sale cara más veces, gana el jugador 1. Si sale seca más veces gana el jugador 2. Si salen iguales ¡los dos hacen la prenda!")

numero_de_tiradas = int(input("Ingrese la cantidad de veces que quiere tirar la moneda:  "))


tiradas = 0
juego = []

jugador1 = input("Jugador 1 ngrese su nombre: ")
jugador2 = input("Jugador 2 ingrese su nombre: ")
prenda1 = input("Ingrese prenda Jugador 1: ")
prenda2 = input("Ingrese prenda Jugador 2: ")


for i in range(0,numero_de_tiradas):
    moneda = random.randint(1,2)
    tiradas +1
    juego.append(moneda)
    
    
    
print(moneda)
print(juego)
    
    
    
if juego.count(2) > 5:
    print(f"Ganaste {jugador1}")
else:
    print(f"Ganaste {jugador2}")    