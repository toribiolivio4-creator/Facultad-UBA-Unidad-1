print("El salario Minino Vital y Movil es de 202800 pesos")
salario = int(input("Ingrese el salario: "))
edad = int(input("Ingrese su edad: "))

if salario >= 202800 and edad >= 16:
    print("Usted está en regla.")
elif salario >= 202800 and edad < 16:
    print("Usted no está en regla.")
elif salario < 202800 and edad < 16:
    print("Usted no está en regla.")
elif salario < 202800 and edad > 16:
    print("Usted no está en regla.") 
else:
    print("Dato no encontrado.")               