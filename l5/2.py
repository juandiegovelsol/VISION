def calcular_formula(opcion, a, b):
    if opcion == 1:
        return a**2 + 2*a*b + b**2
    elif opcion == 2:
        return a**2 - 2*a*b + b**2
    elif opcion == 3:
        return (a - b) * (a + b)
    elif opcion == 4:
        return a**3 - b**3 - 3*a*b*(a - b)
    elif opcion == 5:
        return a**3 + b**3 + 3*a*b*(a + b)
    elif opcion == 6:
        return (a - b) * (a**2 + a*b + b**2)
    elif opcion == 7:
        return (a + b) * (a**2 - a*b + b**2)

def main():
    print("Seleccione una fórmula:")
    print("1. (a+b)² = a² + 2ab + b²")
    print("2. (a-b)² = a² - 2ab + b²")
    print("3. a² - b² = (a-b)(a+b)")
    print("4. (a-b)³ = a³ - b³ - 3ab(a-b)")
    print("5. (a+b)³ = a³ + b³ + 3ab(a+b)")
    print("6. a³ - b³ = (a-b)(a² + ab + b²)")
    print("7. a³ + b³ = (a+b)(a² - ab + b²)")

    opcion = int(input("Introduce el número de la fórmula deseada: "))

    if 1 <= opcion <= 7:
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
        resultado = calcular_formula(opcion, a, b)
        print(f"El resultado es: {resultado}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()