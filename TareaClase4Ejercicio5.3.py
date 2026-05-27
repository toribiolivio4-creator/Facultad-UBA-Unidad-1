#Contraseña

contraseña = input("Ingrese la contraseña: ")
intentos = 4

if contraseña != "Dacia":
    for i in range(intentos):
        input("Ingrese la contrseña: ")
        i += 1
else:
    print("Acceeso exitoso!!")        