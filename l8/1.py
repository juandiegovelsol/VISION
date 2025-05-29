value = input('Por favor ingrese un número natural: ')
try:
    value = int(value)
    if value <= 0:
        print('Esto no es un número natural.')
        exit()
except ValueError:
    # Manejo por si es un número real
    try:
        value = float(value)
        print('Esto no es un numero natural')
        exit()
    except ValueError:
        # Manejo de que no sea de un tipo numerico
        print('Esto no es un número.')
        exit()

# Manejo para evitar la division en 0
try: 
    print('El recíproco de', value, 'es', 1/value)
except ZeroDivisionError:
    print('El número no puede ser 0.')
    exit()