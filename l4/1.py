# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def function(x):
    return x**2

# Definir las entradas
min_val, max_val = -1, 1
input = np.arange(min_val, max_val + 0.1, 0.1)  # Incluye el valor máximo

# Calcular la salida
output = function(input)

# Graficar
plt.plot(input, output, label='f(x) = x²', color='blue')
plt.title('Gráfico de $x^2$')
plt.xlabel('x')  # Nombra el eje x
plt.ylabel('f(x)') # Nombra el eje y
plt.grid(True) # Activa la cuadricula 
plt.legend() # Muestra la leyenda
plt.show()