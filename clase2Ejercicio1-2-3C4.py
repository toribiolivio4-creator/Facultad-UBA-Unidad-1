#SEMAFORO

#verde = 1
#amarillo = 2
#naranja = 3
#rojo = 4

luz = int(input("ingrese 1 / 2 / 3 / 4 "))

if luz == 1:
    print("Siga")
elif luz == 2:
    print("Acelere")
elif luz == 3:
    print("Frene")
elif luz == 4:
    print("Detengase")
else:
    print("El semaforo está apagado")                
    