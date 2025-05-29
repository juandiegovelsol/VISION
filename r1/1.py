import matplotlib.pyplot as plt
import numpy as np

# Crear un rango de valores x desde -10 hasta 10
x = np.linspace(-10, 10, 400)

# Definir las funciones
y1 = x  # y = x
y2 = np.full_like(x, 2)  # y = 2 (función constante)
y3 = np.abs(x) + 1  # y = |x| + 1

# Crear el gráfico
plt.figure(figsize=(8, 8))
plt.plot(x, y1, label='y = x', color='red', linestyle='-')
plt.plot(x, y2, label='y = 2', color='green', linestyle='--')
plt.plot(x, y3, label='y = |x| + 1', color='blue', linestyle=':')

# Ajustar límites de los ejes
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Añadir etiquetas y leyenda
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Mostrar el gráfico
plt.show()