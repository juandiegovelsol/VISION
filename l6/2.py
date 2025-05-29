def square_numbers(numbers):
    """Return a list of the squares of the numbers."""
    squares = []
    for number in numbers:
        try:
            squares.append(float(number) ** 2)
        except (ValueError, TypeError):
            continue
    return squares

def cube_numbers(numbers):
    """Return a list of the cubes of the numbers."""
    cubes = []
    for number in numbers:
        try:
            cubes.append(float(number) ** 3)
        except (ValueError, TypeError):
            continue
    return cubes

def sqrt_numbers(numbers):
    """Return a list of the square roots of the numbers."""
    from math import sqrt
    sqrts = []
    for number in numbers:
        try:
            if float(number) >= 0:
                sqrts.append(sqrt(float(number)))
        except (ValueError, TypeError):
            continue
    return sqrts

def cbrt_numbers(numbers):
    """Return a list of the cube roots of the numbers."""
    cbrts = []
    for number in numbers:
        try:
            cbrts.append(float(number) ** (1/3))
        except (ValueError, TypeError):
            continue
    return cbrts

def main():
    numbers = [1, 2, 3, 4, 'a', '5', 'b']
    print("Squares:", square_numbers(numbers))
    print("Cubes:", cube_numbers(numbers))
    print("Square roots:", sqrt_numbers(numbers))
    print("Cube roots:", cbrt_numbers(numbers))

if __name__ == "__main__":
    main()