#La escondida: Escribí un programa que pida un número y "cuente" imprimiendo todos los números uno por uno hasta ese número.

numero = int(input("Ingrese un numero: "))
if numero >= 0:
    for i in range(1,numero+1,1):
        print(i)
        i += 1
else:
    print("Ingrese un numero positivo")       
