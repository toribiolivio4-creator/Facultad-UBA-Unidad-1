#Jony
print("si tengo plata y no tengo que trabjar puedo preparar un asado con mis amigos.")
plata = input("Tenés plata?: ")
trabajar = input("Tenés que trabajar? (si / no)")

if plata == "no":
    trabajar = False
else:
    trabajar = True    
    
if plata == "si" and not trabajar:
    print("Hay asado")
else:
    print("No hay asado")    