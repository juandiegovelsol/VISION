import math

def formula_cuadratica(a, b, c):
    # Verifica que 'a' no sea cero
    if a == 0:
        raise ValueError("El coeficiente cuadrático 'a' debe ser distinto de cero.")

    # Calcula el discriminante
    discriminante = b**2 - 4*a*c

    # Calcula las raíces usando la fórmula cuadrática
    if discriminante >= 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)

    return (raiz1, raiz2)

# Ejemplo de uso
if __name__ == "__main__":
    # Ecuación: x^2 - 3x + 2 = 0  → raíces reales 1 y 2
    r1, r2 = formula_cuadratica(1, -3, 2)
    print(f"Raíces: {r1} y {r2}")

    # Ecuación: x^2 + 2x + 5 = 0 → raíces complejas
    c1, c2 = formula_cuadratica(1, 2, 1)
    print(f"Raíces: {c1} y {c2}")