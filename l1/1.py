import numpy as np
from scipy.integrate import quad

# Define la función que representa el integrando de la fórmula de longitud de arco.
def integrando(x):
    return np.sqrt(1 + np.cos(x)**2)

# Solicita al usuario los valores de a y b en radianes.
a = float(input("Introduce el valor de a (en radianes): "))
b = float(input("Introduce el valor de b (en radianes): "))

# Calcula la longitud del arco utilizando integración numérica
longitud, _ = quad(integrando, a, b)

# Muestra el resultado de la longitud de arco con 4 cifras decimales.
print(f"La longitud del arco entre a = {a} y b = {b} es: {longitud:.4f}")