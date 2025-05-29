def calcular_tiempo_caida(y1):
    """
    Calcula el tiempo que tarda un objeto en caída libre en llegar a una posición y1.
    
    Argumentos:
        y1 (float): Posición final (debe ser negativa)
    
    Retorna:
        float: Tiempo en segundos
        
    Lanza:
        ValueError: Si y1 no es negativo
    """

    # Validar que y1 sea un número
    if not isinstance(y1, (int, float)):
        raise TypeError("El parámetro y1 debe ser un número")

    # Validar que y1 sea negativo
    if y1 >= 0:
        raise ValueError("El parámetro y1 debe ser negativo")
    
    # Aplicar la fórmula: y1 = (1/2)*g*t²
    # Despejando t: t = sqrt(2*y1/g)
    
    tiempo = (2 * abs(y1) / 9.81) ** 0.5
    return tiempo

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con y1 = -5.10 m como en la imagen
    y1 = -5.1
    tiempo = calcular_tiempo_caida(y1)
    print(f"Un objeto tarda {tiempo:.2f} segundos en caer {abs(y1):.2f} metros")