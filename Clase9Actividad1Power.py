#Temperaturas maximas
import numpy as np
import matplotlib.pyplot as plt

maximas_2025 = [19, 20, 24, 23, 23, 23, 15, 21, 21, 18, 17, 19, 19, 22, 24, 21, 22, 19, 19, 20, 21, 22, 21, 15, 10, 16, 12, 12, 15, 12, 13]
maximas_2024 = [17, 15, 16, 19, 20, 15, 17, 18, 17, 17, 13, 12, 13, 13, 16, 17, 12, 11, 10, 15, 14, 15, 13, 9, 11, 10, 12, 15, 14, 15, 15]

dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

promedio_2024 = sum(maximas_2024)/len(maximas_2024)
promedio_2025 = sum(maximas_2025)/len(maximas_2025)

print(f'El promedio de temperturas de 2024 fue de: {promedio_2024} grados')
print(f'El promedio de temperaturas de 2025 fue de: {promedio_2025} grados')



plt.plot(dias, maximas_2024, linewidth=3, color="red")
plt.plot(dias, maximas_2025, linewidth=3, color="blue")
plt.xlabel('Dias')
plt.ylabel('temperaturas')
plt.title('promedio de temperaturas 2024')
plt.grid(True)
plt.show()
    

