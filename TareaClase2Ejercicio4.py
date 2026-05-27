import random

jugador1 = "Jose"
jugador2 = "Salvador"
dado = random.randint(1,6)

if dado == 1 or dado == 5:
    print("Ganó " + jugador1)
else:
    print("Ganó " + jugador2)    

