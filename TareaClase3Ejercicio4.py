import random

jugador1 = "Salvador"
jugador2 = "José"

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

if dado1 == 1 and dado2 == 5:
    print("Ganó " + jugador2)
elif dado1 == 5 and dado2 == 1:
    print("Ganó " + jugador2)
else:
    print("Ganó " + jugador1)        