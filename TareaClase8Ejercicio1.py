import numpy as np
import matplotlib.pyplot as plt

desempleo = [6.6,5.9,5.7,7.3,7.6,8.4,8.5,8.6,9.1,8.3,8.2,9.1,10.3,11.9,13.1,13.2,13.5,14.3,14.6,15.6,19.3,17.1,14.9,12.5,11.2,8.9,8.9,10.1,9.1,8.5,8.7,8.6,9.0,8.4,10.6,10.5,11.2,12.7,12.5,12.2,10.7]
años = [1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]

plt.figure(figsize=(10, 6))  # <-- aquí va al principio

plt.plot(años, desempleo, linewidth=3, color="red")
plt.xlabel('Años')
plt.ylabel('Desempleo (%)')
plt.title('Desempleo a través de los años')

plt.ylim([0, 30])  # Ajuste del eje Y

# Líneas verticales para marcar presidentes
plt.axvline(2007, color='blue', linestyle='--')
plt.axvline(2015, color='blue', linestyle='--')
plt.axvline(2019, color='blue', linestyle='--')
plt.axvline(2003, color='blue', linestyle='--')

# Etiquetas de presidentes
plt.text(2007 + 0.5, 25, "Cristina Kirchner", rotation=90, color='blue')
plt.text(2015 + 0.5, 25, "Macri", rotation=90, color='blue')
plt.text(2019 + 0.5, 25, "Alberto Fernández", rotation=90, color='blue')
plt.text(2003 + 0.5, 25, "Nestor Kirchner", rotation=90, color='blue')

plt.show()

#Cuando más aumentó el desempleo fue en el 2001-2002
#Cuando más disminuyó fue entre el 2003 y 2007


#Calculo la Tasa mas alta de desempleo:
max_desempleo = max(desempleo)
indice_max = np.argmax(desempleo)
año_max = años[indice_max]

print(f"La tasa más alta fue {max_desempleo}% en el año {año_max}.")

#Calculo la Tasa mas baja de desempleo:
min_desempleo = min(desempleo)
indice_min = np.argmin(desempleo)
año_min = años[indice_min]

print(f"La tasa más alta fue {min_desempleo}% en el año {año_min}.")

