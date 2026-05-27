#Actividad 2
import random

#print("Moneda Recargada!!")


cruz = 0
moneda = random.randint(0,1)

while moneda == 1:
    moneda = random.randint(0,1)
    cruz = cruz + 1
    
print(f"Vas a tener que saltar {cruz} veces en una pata!!")        