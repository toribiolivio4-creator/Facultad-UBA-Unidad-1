print("Argentina 1985")

edad = int(input("Ingrese su edad: "))
dinero = int(input("Ingrese la cantidad de dinero que usted tiene: "))

if edad >= 18 and dinero >= 1200:
    print("Podes ver la peli!!")
elif edad >= 18 and dinero < 1200:
    print("Lo lamento, te falta guita")
elif edad < 18 and dinero >= 1200:
    print("Tenes plata, pero sos muy chico para ver esta pelicula.")
else:
    print("Dato no encontrado.")
                   
