#Actividad 1

precio = 2933
fondos = 15000
contador = 0

while fondos>precio:
    fondos = fondos - precio
    contador += 1
    print(f"Compré {contador} chocolate/s")


print('El vuelto será ', fondos, ' pesos')