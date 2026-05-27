#Sale el sol
print("Sol Afuera: 1, Lluvioso: 2, Nublado: 3")
sol = int(input("Ingrese 1 / 2 / 3 en funcion de como esté el tiempo"))
if sol == 1:
    print("No uso paraguas porque está soleado")
elif sol == 2:
    print("Uso paraguas porque está lluvioso")
elif sol == 3: 
    print("Llevo el paraguas por las dudas porque está nublado")
else:
    print("Dato no encontrado")
                
#Guita para el asado
print("Ingrese SI / NO si tengo plata o ganas, o ambos")
ganas = str(input("Tengo ganas?"))
guita = str(input("Tengo plata?"))

if ganas == "si" and guita == "si":
    print("Hago el asado!!!")
elif ganas == "si" and guita == "no":
    print("Tengo ganas, pero no tango plata para hacer el asado")
elif ganas == "no" and guita == "si":
    print("Tengo la plata, pero no tengo la plata para el asado")
else:
    print("Fijate que ingresaste un dato diferente de SI / NO")        
    
#Paquete de chocolinas
print("Si el paquete de chocoliinas sale menos de 300 pesos")

precio_chocolinas = int(input("Ingrese el precio de las chocolinas: "))

if precio_chocolinas < 300:
    print("Me compro 2 paquetes de chocolinas")
else:
    print("Me compro la chocodia")
    

#Livio: si está lluvioso o está nublado hago torta fritas, si está soledo no hago torta fritas.
#Evelin: si no hace frio y tengo plata salgo el sabado.
#Jony: si tengo plata y no tengo que trabjar puedo preparar un asado con mis amigos.
#Facu: Si está soledado me meto a la pileta, si está ventoso me meto igual  y si está lluvioso no me meto.