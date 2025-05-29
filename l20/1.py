def darPuntaje():
    """
    Solicita y válida una puntuación del 1 al 5 del usuario.
    Retorna la puntuación como string una vez validada.
    """
    print('¿Que puntuación le da a la liga que escogió de 1 a 5?')
    puntuacion = input('')
    
    # Validación de la puntuación ingresada
    while not puntuacion.isdigit() or int(puntuacion) < 1 or int(puntuacion) > 5:
        print('Por favor ingrese un número válido entre 1 y 5')
        puntuacion = input('')
    
    return puntuacion

# Mensaje de bienvenida y presentación de opciones
print('Hola. Bienvenido a votamatic')
print('1. Bundesliga')
print('2. Liga Santander')
print('3. Premiere Liga')

# Captura y validación de la selección del usuario
eleccionUsuario = input('Escoja el número de su Liga\n')

# Validación de la selección con oportunidad de reintentar
while eleccionUsuario not in ['1', '2', '3']:
    print('Opción inválida. Por favor seleccione 1, 2 o 3.')
    eleccionUsuario = input('Escoja el número de su Liga\n')

# Procesamiento de la selección válida
if eleccionUsuario == '1':
    puntos = darPuntaje()
    eleccion = 'Bundesliga'
elif eleccionUsuario == '2':
    puntos = darPuntaje()
    eleccion = 'Liga Santander'
elif eleccionUsuario == '3':
    puntos = darPuntaje()
    eleccion = 'Premiere Liga'

# Presentación del resultado usando f-string para consistencia
print(f'Usted elige {eleccion} y le da {puntos} de puntaje.')