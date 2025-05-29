import numpy as np
import matplotlib.pyplot as plt

# Valores de x entre -10 y 10
x = np.linspace(-10, 10, 400)

# Funciones
y_lineal = x                     # y = x
y_constante = np.full_like(x, 2) # y = 2
y_valor_absoluto = np.abs(x) + 1 # y = |x| + 1

# Crear gráfica
plt.figure(figsize=(8, 8))

plt.plot(x, y_lineal, label='y = x', color='red', linestyle='-')          
plt.plot(x, y_constante, label='y = 2', color='blue', linestyle='--')    
plt.plot(x, y_valor_absoluto, label='y = |x| + 1', color='green', linestyle=':')  

# Ejes y límites
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráficas de funciones basicas')
plt.legend()
plt.show()