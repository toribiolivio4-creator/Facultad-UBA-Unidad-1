#Semaforo recargado

import random

luz = random.choice(["rojo", "amarillo", "verde"])
print(f"La luz es: {luz}")

for i in luz:
    if luz == "rojo":
        print("Pare")
        break
    elif luz == "amarillo":
        print("Acelere")
        break
    elif luz == "verde":
        print("Siga")
        break
    else: 
        print("Semaforo apagado")            


