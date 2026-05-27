# Ruleta
import random
ruleta = []
cantidad_de_tiradas = int(input('Ingresá la cantidad de veces que queres tirar:  '))
capital = int(input('Ingresá el capital que querés apostar:  '))
apuesta = int(input('Ingresá la cantidad de dinero que querés apostar por tirada:  '))
n_suerte = int(input('Ingresá un numero entre el 0 y el 36:  '))
cuenta_del_casino = 0


while capital > 0:
    if n_suerte >= 0 and n_suerte <= 36:
        
        azar = random.randint(0,36)
        ruleta.append(azar)
        
        if n_suerte == azar:
            print('Ganaste!!')
            print(azar)
            capital = capital + apuesta
            cuenta_del_casino = cuenta_del_casino - apuesta
        else:
            print('Perdiste!!')  
            print(azar)
            capital = capital - apuesta
            cuenta_del_casino = cuenta_del_casino + apuesta
    else: 
        print('Error, ingresá un numero entre el 0 y el 36!!') 
        
print(f'Tu dinero es {capital}')               
print(f'La cuenta del banco es de {cuenta_del_casino}')          


