def menu():
    print("Selecciona una fórmula algebraica para aplicar:")
    print("1. (a + b)² = a² + 2ab + b²")
    print("2. (a - b)² = a² - 2ab + b²")
    print("3. a² - b² = (a - b)(a + b)")
    print("4. (a + b)³ = a³ + b³ + 3ab(a + b)")
    print("5. (a - b)³ = a³ - b³ - 3ab(a - b)")
    print("6. a³ - b³ = (a - b)(a² + ab + b²)")
    print("7. a³ + b³ = (a + b)(a² - ab + b²)")

def calcular_formula(opcion, a, b):
    if opcion == 1:
        resultado = a**2 + 2*a*b + b**2
        formula = f"({a} + {b})² = {a**2} + 2*{a}*{b} + {b**2} = {resultado}"
    elif opcion == 2:
        resultado = a**2 - 2*a*b + b**2
        formula = f"({a} - {b})² = {a**2} - 2*{a}*{b} + {b**2} = {resultado}"
    elif opcion == 3:
        resultado = (a - b) * (a + b)
        formula = f"{a}² - {b}² = ({a} - {b})({a} + {b}) = {resultado}"
    elif opcion == 4:
        resultado = a**3 + b**3 + 3*a*b*(a + b)
        formula = f"({a} + {b})³ = {a**3} + {b**3} + 3*{a}*{b}*({a} + {b}) = {resultado}"
    elif opcion == 5:
        resultado = a**3 - b**3 - 3*a*b*(a - b)
        formula = f"({a} - {b})³ = {a**3} - {b**3} - 3*{a}*{b}*({a} - {b}) = {resultado}"
    elif opcion == 6:
        resultado = (a - b)*(a**2 + a*b + b**2)
        formula = f"{a}³ - {b}³ = ({a} - {b})({a}² + {a}*{b} + {b}²) = {resultado}"
    elif opcion == 7:
        resultado = (a + b)*(a**2 - a*b + b**2)
        formula = f"{a}³ + {b}³ = ({a} + {b})({a}² - {a}*{b} + {b}²) = {resultado}"
    else:
        formula = "Opción no válida."
    return formula

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Escribe el número de la fórmula que deseas utilizar (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            print("Debes introducir un número del 1 al 7.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero del 1 al 7.")

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número correctamente.")

def main():
    menu()
    opcion = pedir_opcion()
    a = pedir_numero("Introduce el valor de a: ")
    b = pedir_numero("Introduce el valor de b: ")
    resultado = calcular_formula(opcion, a, b)
    print("\nResultado:")
    print(resultado)

if __name__ == "__main__":
    main()