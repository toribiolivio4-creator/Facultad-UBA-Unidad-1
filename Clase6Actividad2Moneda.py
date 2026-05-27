#Actividad 2
import random

#print("Moneda Recargada!!")

cruz = 0
moneda = 0

while moneda == 0:
    moneda = random.randint(0,1) #0 es cruz, 1 es cara
    if moneda == 0:
        print("Salió cruz")
        cruz = cruz + 1
        print(f"Vas a tener que saltar {cruz} veces en una pata!!")
    elif moneda == 1:
        print(f"Salió cara")
    else:
        print("Dato no encontrado")
            
        
        
    
