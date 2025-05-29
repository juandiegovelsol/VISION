import math

# Ejemplo de cómo evitar expresiones complejas
def validate_number(x):
    '''Valida que el elemento sea un número'''
    if isinstance(x,(int, float)):
        return x
    elif isinstance(x, str):
        try: 
            return float(x)
        except ValueError:
            return None
    return None

def square_root_numbers(numbers):
    '''Retorna una lista de las raices cuadradas de los números'''
    square_roots = []
    for number in numbers: 
        num = validate_number(number)
        if num is not None and num >= 0:
            square_roots.append(math.sqrt(num))
    return square_roots

def cube_root_numbers(numbers):
    '''Retorna una lista de las raices cúbicas de los números'''
    cube_roots = []
    for number in numbers: 
        num = validate_number(number)
        if num is not None:
            cube_roots.append(math.cbrt(num))
    return cube_roots

def square_numbers(numbers):
    '''Retorna una lista de los cuadrados de los números.'''
    squares = []
    for number in numbers:
        num = validate_number(number)
        if num is not None: 
            squares.append(num**2)
    return squares

def cube_numbers(numbers):
    '''Retorna una lista de los cubos de los números'''
    cubes = []
    for number in numbers:
        num = validate_number(number)
        if num is not None: 
            cubes.append(num**3)
    return cubes

def main():
    numbers = [1, 2, 3, 4]

    results_square_roots = square_root_numbers(numbers)
    results_cubes_roots = cube_root_numbers(numbers)
    results_squares = square_numbers(numbers)
    results_cubes = cube_numbers(numbers)

    print("Resultado raíces cuadradas:", results_square_roots)
    print("Resultado raíces cúbicas:", results_cubes_roots)
    print("Resultado cuadrados:", results_squares)
    print("Resultado cubos:", results_cubes)

if __name__ == "__main__":
    main()