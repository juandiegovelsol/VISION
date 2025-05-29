def darPuntaje():
    while True:
        # Solicitar que el usuario ingrese una puntuación valida de 1 a 5
        print('¿Qué puntuación le da a la liga que escogió de 1 a 5?')
        puntuacion = input('')
        if puntuacion.isdigit() and 1 <= int(puntuacion) <= 5:
            return puntuacion
        else:
            print("Por favor, ingrese un número válido entre 1 y 5.")

print('Hola. Bienvenido a votamatic')
print('1. Bundesliga')
print('2. Liga Santander')
print('3. Premiere Liga')

eleccionUsuario = input('Escoja el número de su Liga\n')

if eleccionUsuario == '1':
    puntos = darPuntaje()
    eleccion = 'Bundesliga'
elif eleccionUsuario == '2':
    puntos = darPuntaje()
    eleccion = 'Liga Santander'
elif eleccionUsuario == '3':
    puntos = darPuntaje()
    eleccion = 'Premiere Liga'
else:
    eleccion = None
    puntos = None
    print('Opción inválida. Por favor, seleccione 1, 2 o 3.')

if eleccion and puntos:
    print(f'Usted eligió {eleccion} y le da {puntos} de puntaje.')