import numpy as np
from scipy.integrate import quad

# Define la función a integrar
def integrand(u):
    return np.sqrt(1 + np.cos(u)**2)

# Define los límites de integración
a = 10  # cambia este valor según sea necesario
b = 20  # cambia este valor según sea necesario

# Calcula la longitud del arco
arc_length, _ = quad(integrand, a, b)

# Muestra el resultado con 4 cifras decimales
print(f"La longitud del arco es: {arc_length:.4f}")