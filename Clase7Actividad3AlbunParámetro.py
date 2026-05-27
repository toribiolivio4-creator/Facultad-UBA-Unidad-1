#Albun de figuritas

import random

cant_figus = int(input("Ingrese la cantidad de figuritas que tiene el albun:  "))
albun = set(range(0,cant_figus))
albun_vacio = set()
figus_repetidas = []
contador = 0


while albun != albun_vacio:
    figurita = random.randint(0,cant_figus-1)
    contador += 1
    if figurita in albun_vacio:
        figus_repetidas.append(figurita)
    albun_vacio.add(figurita)
    

print(f"Necesité conprar {len(figus_repetidas)} figuritas")  
print(f"La cantidad de intentos fue: {contador}")  
print(f"El albun es: {albun_vacio}")
    











