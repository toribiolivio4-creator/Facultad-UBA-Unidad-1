import numpy as np
import matplotlib.pyplot as plt


años = [1869,1895, 1914, 1947, 1960, 1970, 1980,1991,2001,2010]
poblacion = [1830214, 4044911, 7903662, 15893827 ,20010539,23362333 ,27947446 ,32615528 ,36260130, 40117096]

# Convierto a millones
poblacion_millones = [p/1_000_000 for p in poblacion]

plt.figure(figsize=(10,6))
plt.title('Evolución de la población (millones)')
plt.ylim([0, 45])  # ajuste para mostrar un poco más que el máximo (~40 millones)
plt.plot(años, poblacion_millones, marker='o', color='green')
plt.xlabel('Años')
plt.ylabel('Población (millones)')
plt.grid(True)
plt.show()
