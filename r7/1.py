import math

#Calcula el área de un círculo.
def area_circulo(radio):

    return math.pi * radio ** 2

#Calcula el área de un cuadrado.
def area_cuadrado(lado):
 
    return lado ** 2

#Calcula el área de un paralelogramo.
def area_paralelogramo(base, altura):
   
    return base * altura

def menu():
    """
    Menú de opciones:
    1. Círculo
    2. Cuadrado 
    3. Paralelogramo

    El usuario selecciona una opción y se le solicita la entrada correspondiente.
    """
    while True:
        print("\nSeleccione la figura para calcular el área:")
        print("1) Círculo")
        print("2) Cuadrado")
        print("3) Paralelogramo")
        print("4) Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            resultado = area_circulo(radio)
            print("Área del círculo =", resultado)

        elif opcion == "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            resultado = area_cuadrado(lado)
            print("Área del cuadrado =", resultado)

        elif opcion == "3":
            base = float(input("Ingrese la base del paralelogramo: "))
            altura = float(input("Ingrese la altura del paralelogramo: "))
            resultado = area_paralelogramo(base, altura)
            print("Área del paralelogramo =", resultado)

        elif opcion == "4":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Llamar al menú principal
menu()