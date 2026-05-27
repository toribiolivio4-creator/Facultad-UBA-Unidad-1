#For
#Table de multiplicar

#numero = int(input("Ingrese un valor: "))

for numero in range(1,10):
    print(f"--- Tabla del {numero}")
    for i in range(0,10):
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")
    