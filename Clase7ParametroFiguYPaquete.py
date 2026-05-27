#Albun de figuritas

import random
print("Cada sobre tiene 5 figuritas.")
figus_por_sobre = 5
cant_figus = int(input("Ingrese la cantidad de figuritas que tiene el albun:  "))
cant_de_sobres = int(input("Ingrese la cantidad de sobres que compraste: "))*5
albun = set(range(0,cant_figus))
albun_vacio = set()
figus_repetidas = []
contador = cant_de_sobres


while albun != albun_vacio:
    figurita = random.randint(0,cant_figus-1)
    contador += 1
    if figurita in albun_vacio:
        figus_repetidas.append(figurita)
    albun_vacio.add(figurita)
    

print(f"Se repitieron {len(figus_repetidas)} figuritas ")  
print(f"La cantidad de intentos fue: {contador}")  
print(f"El albun es: {albun_vacio}")
print(f"Compré {cant_de_sobres} figuritas")