#Datos
import csv
with open("Facultad\\Datos.csv", 'r', encoding='utf-8') as f:
    datos = [line.strip() for line in f if line.strip()]
    
nombre = input('Ingresá tu nombre: ').capitalize()
apellido = input('Ingresá tu apellido: ').capitalize()
print(f'Hola {nombre} {apellido}, como andas!')

if nombre in datos[1] and apellido in datos[2]:
    print(f'dato encontrado, y tu deuda es de {datos[4]}')
    if datos[4] < 0:
        respuesta = input('Querés pagar tu deuda? SI/NO').lower()
        if respuesta == 'no':
            print('Te vas a quedar sin el servicio!!')
        elif respuesta == 'si':
            print('Joyaa, vas a conservar tu plan!!')
        else:
            print('respuesta incerrecta, ponga si o no')        
else:
    print('Datos no encontrados, vamos a registrarte!')    
    dni = int(input('Ingrese su DNI: '))
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese si apellido: ')
    plan = '300M'
    saldo = int(input('Ingrese su saldo: '))
    direcciones = input('Ingrese su direccion: ')
    
    nuevo_dato = [dni,nombre,apellido,plan,saldo,direcciones]
    
    with open('Datos.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(nuevo_dato)

    
    print("Datos agregado correctamente.")
    
    print(datos)