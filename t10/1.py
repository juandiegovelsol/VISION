import math

def calcular_alcance(v0, alpha_deg):
    """
    Calcula el alcance de un proyectil.
    
    Argumentos:
        v0 (float): Velocidad inicial en m/s
        alpha_deg (float): Ángulo de lanzamiento en grados
    
    Retorna:
        float: Alcance del proyectil en metros
    
    Lanza:
        TypeError: Si los parámetros no son números
        ValueError: Si la velocidad no es positiva o el ángulo no está en (0,90)
    """
    # Constante de gravedad en sistema internacional de medida
    G = 9.81
    
    # Validación de tipos
    if not isinstance(v0, (int, float)) or not isinstance(alpha_deg, (int, float)):
        raise TypeError("Todos los parámetros deben ser números.")
    
    # Validación de rango
    if v0 <= 0:
        raise ValueError("La velocidad inicial v0 debe ser un número positivo.")
    
    # Validación de ángulo
    if alpha_deg <= 0 or alpha_deg >= 90:
        raise ValueError("El ángulo alpha debe estar entre 0° y 90° (no incluidos).")

    # Conversión a radianes
    alpha_rad = (alpha_deg * math.pi) / 180

    # Fórmula del alcance: R = v0^2 * sin(2α) / G
    alcance = (v0 * v0 * math.sin(2 * alpha_rad)) / G

    return round(alcance, 2)

# Ejemplo de uso:
try:
    v0 = 20  # m/s
    angulo = -45  # grados
    rango = calcular_alcance(v0, angulo)
    print(f"El proyectil recorre {rango} m antes de volver a y = 0.")
except Exception as err:
    print(f"Error: {str(err)}")