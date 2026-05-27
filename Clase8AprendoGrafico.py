import numpy as np
import matplotlib.pyplot as plt

dias=[1,2,3,4,5,6,7,8,9,10]
temperatura=[25,28,23,19,22,25,28,27,29,26]

plt.plot(dias,temperatura, linewidth=8, color="red")
plt.plot(dias,temperatura,color='red')
plt.xlabel('dias')
plt.ylabel('temperatura')
plt.title('temperaturas vs días')
plt.show()