#Salario minimo vital y móvil 296832
salario_minimo = 296832
sueldo = int(input("Ingrese su salario: "))

if sueldo > salario_minimo:
    print("Ganas por encima del salario minimo")
elif sueldo == salario_minimo:
    print("Ganas en SMVM") 
else:
    print("Te están explotando")       