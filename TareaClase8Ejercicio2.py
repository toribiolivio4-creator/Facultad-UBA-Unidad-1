import numpy as np
import matplotlib.pyplot as plt

#Datos a nivel nacional
años = [1869,1895, 1914, 1947, 1960, 1970, 1980,1991,2001,2010]
poblacion = [1830214, 4044911, 7903662, 15893827 ,20010539,23362333 ,27947446 ,32615528 ,36260130, 40117096]

# Datos Marcos Paz
años_marcos_paz = [2010, 2022]
censo_marcos_paz = [54181, 67011]

plt.figure(figsize=(10,6)) #Defino 10 de alto por 6 de ancho
plt.title('Evolucion en la poblacion (azul) y poblacion en Marcos Paz(verde)')

# Población Marcos Paz
plt.plot(años_marcos_paz, censo_marcos_paz, marker='o', color='green', label='Marcos Paz')
#El parámetro maker define el tipo de marcador para cada coodenada del grafico

# Población nacional
plt.plot(años, poblacion, marker='o', label='Población Argentina')
plt.ylim([0, 45000000])  # 45 millones
plt.xlabel('Años')
plt.ylabel('Población (en millones)')
plt.grid(True)
plt.show()

print("Este argumento especifica el tipo de marcador que se utilizará para representar los puntos en el gráfico. 'o' representa un círculo. ")