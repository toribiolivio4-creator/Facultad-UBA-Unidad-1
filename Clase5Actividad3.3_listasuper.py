
fondos= 15000

lista_precios = [900, 7080, 2060, 2933, 1860, 950, 1145, 3000]
productos = ['sal', 'café','pan lactal', 'chocolate', 'papel higénico', 'lavandina', 'leche', 'huevos']

lista_mezclada = list(zip(productos,lista_precios))
print(lista_mezclada)

carrito = []

for producto,precio in lista_mezclada:
    if fondos >= precio:
        fondos -= precio
        carrito.append(producto)
        print(f"Compraste {producto} por ${precio}. Fondos restantes: ${fondos}")
    else:
        print(f"No alcanza para {producto}, cuesta ${precio} y tenés ${fondos}")    
        
        
print("\nResumen de compras:")
print(carrito)
print(f"Dinero restante: ${fondos}")        

hola, chau = {"Hola":"Chauu"}
print(hola,chau)