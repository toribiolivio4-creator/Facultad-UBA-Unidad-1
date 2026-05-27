#Borracho
import numpy as np
import matplotlib.pyplot as plt
import random

diferentes_trayectorias = 3

for i in range(0,diferentes_trayectorias):
    pos = 0 #En esta variable guardaremos la posición en cada momento
    t = 0 # En esta variable guardaremos el tiempo
    trayectoria = [] # En esta variable guardaremos todas las posiciones recorridas
    tiempo = []
    
    while pos >= -20 and pos <= 20:
        pos=random.randint(-20,20)
        trayectoria.append(pos)
        tiempo.append(t)
        t = t + 1
        print(f'El borracho se movió {pos} metros')
        if t == 10:
            break
        
    print(trayectoria)
    print(tiempo)
    promedio = sum(tiempo)/10
    print(f'El tiempo promedio que tarda el borracho en llegar a cada posicion es de {promedio} minutos')


    plt.figure(figsize=(10,6))
    plt.title('Trayectoria del borracho')
    plt.ylim([-20,20])  #Metros aleatorios con 40 metros de deriva
    plt.plot(trayectoria, tiempo, marker='o', color='green') 
    plt.xlabel('Trayectoria en metros')
    plt.ylabel('Tiempo (minutos)')
    plt.grid(True)
    plt.show()