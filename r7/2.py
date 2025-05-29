import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.
    Fórmula: área = π * radio^2
    """
    return math.pi * radio ** 2

def area_cuadrado(lado):
    """
    Calcula el área de un cuadrado.
    Fórmula: área = lado^2
    """
    return lado ** 2

def area_paralelogramo(base, altura):
    """
    Calcula el área de un paralelogramo.
    Fórmula: área = base * altura
    """
    return base * altura

def main():
    while True:
        print("Seleccione una figura para calcular el área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Paralelogramo")
        print("4. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"El área del círculo es: {area_circulo(radio)}")
        
        elif opcion == "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"El área del cuadrado es: {area_cuadrado(lado)}")
        
        elif opcion == "3":
            base = float(input("Ingrese la base del paralelogramo: "))
            altura = float(input("Ingrese la altura del paralelogramo: "))
            print(f"El área del paralelogramo es: {area_paralelogramo(base, altura)}")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()