edad = int(input("Ingrese su edad: "))
dinero = int(input("Ingrese su dinero disponible: "))

if edad >= 13 and dinero >= 1200:
    print("Usted puede ver la Pelicula")
elif edad < 13 and dinero >= 1200:
    print("Tenes plata, pero sos muy chico para esta pelicula")
elif edad >= 13 and dinero < 1200:
    print("Te falta plata")
else:
    print("No cumplis con los requisitos")            
    