import random

def switch():
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))

    eleccion = 0

    while True:
        print("""
        Indique la operación a realizar:
        1) Sumar
        2) Restar
        3) Multiplicar
        4) Dividir
        5) Cambiar los números introducidos
        6) Usar dos números aleatorios
        7) Salir de la calculadora
        """)

        eleccion = int(input())

        if eleccion == 1:
            print(" ")
            print("RESULTADO: ", numero1, " + ", numero2, " = ", numero1 + numero2)
        elif eleccion == 2:
            print(" ")
            print("RESULTADO: ", numero1, " - ", numero2, " = ", numero1 - numero2)
        elif eleccion == 3:
            print(" ")
            print("RESULTADO: ", numero1, " x ", numero2, " = ", numero1 * numero2)
        elif eleccion == 4:
            print(" ")
            print("RESULTADO: ", numero1, " / ", numero2, " = ", float(numero1 / numero2))
        elif eleccion == 5:
            numero1 = int(input("Introduzca el primer número: "))
            numero2 = int(input("Introduzca el segundo número: "))
        elif eleccion == 6:
            numero1 = random.randint(1, 100)
            numero2 = random.randint(1, 100)
            print("Números aleatorios generados: ", numero1, ", ", numero2)
        elif eleccion == 7:
            print("Hasta pronto")
            break
        else:
            print("Elección no válida. Intente de nuevo.")