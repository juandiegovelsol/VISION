#import libraries
import numpy as np
import matplotlib.pyplot as plt

#define function
def function(x):
    return x**2

#define input
min, max = -1, 1
input = np.arange(min, max + 0.1, 0.1)  # Ajuste para incluir el valor máximo

#calculate output
output = function(input)

#plot the graph
plt.plot(input, output, label='x^2')  # Añadir etiqueta a la función
plt.title('Graph of x^2')
plt.xlabel('x-axis')  # Etiqueta del eje x
plt.ylabel('y-axis')  # Etiqueta del eje y
plt.grid(True)  # Mostrar cuadrícula
plt.legend()  # Mostrar leyenda
plt.show()