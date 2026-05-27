# Verde= 1
# Amarillo = 2
# Naranja = 3
# Rojo = 4

semaforo = int(input("Ingrese 1 / 2 / 3 / 4:"))
if semaforo == 1:
    print("Siga")
elif semaforo == 2:
    print("Acelere")
elif semaforo == 3:
    print("Frene")
elif semaforo == 4:
    print("Detengase")
else: 
    print("El semaforo está apagado")            