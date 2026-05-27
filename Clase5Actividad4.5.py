#Cada jugador tira la moneda hasta que salga cara. Se cuentan la cantidad de secas que salieron hasta que salió la primer cara. Ese jugador va a tener que hacer esa cantidad de saltos en un pie.

import random

secas = 0
moneda = random.randint(0,1) #0 es cara, 1 es seca
while moneda == 1:
    moneda = random.randint(0,1)
    secas = secas + 1

print('Tenés que saltar ',secas, ' veces')