import random

def adding(a, b):
    """
    Argumentos:
        a (int o float): Primer número
        b (int o float): Segundo número

    Retorna:
        Imprime el resultado de la suma.
    """
    resultado = a + b
    print(f"El resultado de sumar {a} y {b} es {resultado}")


def randomizer():
    """
    Retorna:
        int: Un número aleatorio entre 10 y 200
    """
    numero = random.randint(10, 200)
    return numero


def reducing(a, b):
    """
    Argumentos:
        a (int o float): Primer número
        b (int o float): Segundo número

    Retorna:
        Imprime el resultado de la resta.
    """
    resultado = a - b
    print(f"El resultado de restar {b} a {a} es {resultado}")

# Ejemplos

# Función 1
adding(3,5) # Salida esperada: El resultado de sumar 3 y 5 es 8

#Función 2
print(f"Número aleatorio entre 10 y 200: {randomizer()}") # Salida esperada: Un número aleatorio entre 10 y 200

#Función 3
reducing(10,2) # Salida esperada: El resultado de restar 2 a 10 es 8