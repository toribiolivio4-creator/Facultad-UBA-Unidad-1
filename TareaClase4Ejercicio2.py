#Lista de numeros
lista_numeros=[0,3,2,7,8]
lista_numeros[0] = lista_numeros[0] + 3 #Le sumo 3 al indice 0
print(lista_numeros)

lista_numeros[1] = lista_numeros[1] - 2 #le resto 2 al indice 1
print(lista_numeros)

lista_numeros[-1] = lista_numeros[-1] * 5 #multiplico por 5 al ultomo elemento
print(lista_numeros)

largo_de_la_lista = len(lista_numeros) #cuantos elementos tiene la lista
print(largo_de_la_lista)

suma_de_los_elementos = lista_numeros[0] + lista_numeros[1] + lista_numeros[2] + lista_numeros[3] + lista_numeros[4]
print(suma_de_los_elementos)

suma_de_los_elementos = sum(lista_numeros)
print(suma_de_los_elementos)
