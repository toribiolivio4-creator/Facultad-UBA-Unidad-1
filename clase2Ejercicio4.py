sueldo = int(input("Ingrese su sueldo actual: "))
horas_mensuales = int(input("Ingrese la cantidad de horas por mes que trabaja: "))

sueldo_hora = sueldo / horas_mensuales

if sueldo_hora > 1528:
    print("Felicitaciones, usted gana por encima del sueldo minimo.")
elif sueldo_hora == 1528:
    print("Usted gana el sueldo minimo.")
else:
    print("A usted lo/la están explotando.")         