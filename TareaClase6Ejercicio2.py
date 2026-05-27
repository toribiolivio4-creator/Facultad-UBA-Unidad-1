#Otra vez figuritas

figus_Diego = [1,3,5,7,9]
figus_Lola = [2,3,7,9,10]

albun_conjunto = figus_Lola + figus_Diego
albun_ordenado = sorted(albun_conjunto)
print(albun_ordenado)
figus_repetidas = []
figus_no_repetidas = []


for i in albun_ordenado:
    if albun_ordenado.count(i) < 2:
        figus_no_repetidas.append(i)
    else:
        figus_repetidas.append(i)
        

print(f"Las figuritas {figus_no_repetidas} no se repiten")         
print(f"Las figuritas {figus_repetidas} se repiten")       