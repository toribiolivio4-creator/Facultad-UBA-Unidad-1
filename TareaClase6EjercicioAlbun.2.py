#Completar 100 albunes
import random
from collections import Counter
print("1: Patagonykus | 2: Yungavolucris | 3:Talenkauen | 4: Huinculsaurus | 5: Orkoraptor | 6: Noasaurus")

albunes = 100
figus_promedio = []


for i in range(albunes):
    albun = set(range(1,7))  #creo un albun con el rango de figuritas necesarias para completar el albun, y con el set evito que se repitan los numeros
    albun_incompleto = set() #creo un albun vacio (conjunto)
    contador = 0
    cant_de_figuritas = [] #creo una lista para guardar las figuritas que compro

    while albun_incompleto != albun: #mientras la cantidad de elemntos en albun vacio sea diferente a la cantidad de elementos en el albun principal se repite el bucle
        figurita = random.randint(1,6) #genero figuritas al azar del 1 al 6
        #print(figurita)
        albun_incompleto.add(figurita) #agrego esas figuritas al albun vacio
        contador += 1
        cant_de_figuritas.append(figurita)
        figus_promedio.append(figurita)
        #print(contador)
    
    print(f"El albun es: {albun_incompleto}")    
    print(f"Las figuritas que compré son:  {cant_de_figuritas}") 
    figus = len(cant_de_figuritas) # muestro cuantos elementos hay en esa lista (cada elemento es una figurita), y el largo de esa lista me da la cantidad figuritas que compré
    print(f"Tuve que comprar {figus} figuritas para completar el albun")   

    fig1 = cant_de_figuritas.count(1) #cuento cuantas fig. 1 compré y así con las demás
    fig2 = cant_de_figuritas.count(2)
    fig3 = cant_de_figuritas.count(3)
    fig4 = cant_de_figuritas.count(4)
    fig5 = cant_de_figuritas.count(5)
    fig6 = cant_de_figuritas.count(6)

    print(f"Compre {fig1} figurita/s del Patagonykus")
    print(f"Compre {fig2} figurita/s del Yungavolucris")
    print(f"Compre {fig3} figurita/s del Talenkauen")
    print(f"Compre {fig4} figurita/s del Hiunculsaurus")
    print(f"Compre {fig5} figurita/s del Orkoraptor")
    print(f"Compre {fig6} figurita/s del Noasaurus")

    max_figuritas = Counter(cant_de_figuritas)
    mas_comun = max_figuritas.most_common(1)
    print(f"La figurita que más me vendieron fue la numero {mas_comun}")
    

promedio = (len(figus_promedio))/100
promedio = round(promedio)
print(f"Tengo que usar un promedio de {promedio} figuritas por álbun para llenar 100 albunes.")
