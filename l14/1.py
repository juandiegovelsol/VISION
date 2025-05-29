import cmath
import math

def formula_cuadratica(a, b, c):
    """
    Resuelve una ecuación cuadrática.

    Devuelve en una tupla las dos raíces que resuelven la ecuación:
        a x^2 + b x + c = 0.

    Utiliza la fórmula general para resolver una ecuación cuadrática.

    Parámetros:
      a -- coeficiente cuadrático (debe ser distinto de 0)
      b -- coeficiente lineal
      c -- término independiente

    Retorna:
      x1 -- solución 1 a la ecuación cuadrática.
      x2 -- solución 2 a la ecuación cuadrática.

    Excepciones:
      ValueError -- si a == 0
    """
    if a == 0:
        raise ValueError("El coeficiente cuadrático 'a' debe ser distinto de 0.")
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        # Usamos math.sqrt para que funcione con raíces reales
        raiz = math.sqrt(discriminante)
    else:
        # Usamos cmath.sqrt para que funcione también con raíces complejas
        raiz = cmath.sqrt(discriminante)
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)
    return (x1, x2)


# Ejemplo de uso
if __name__ == "__main__":
    # Ecuación: x^2 - 3x + 2 = 0  → raíces reales 1 y 2
    r1, r2 = formula_cuadratica(1, -3, 2)
    print(f"Raíces: {r1} y {r2}")

    # Ecuación: x^2 + 2x + 5 = 0 → raíces complejas
    c1, c2 = formula_cuadratica(1, 2, 5)
    print(f"Raíces: {c1} y {c2}")