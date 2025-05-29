def introducirNumeros():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))

def sumar(a, b):
    print("La suma de ", a, "+", b, "=", a + b)

def restar(a, b):
    print("La resta de ", a, "-", b, "=", a - b)

def multiplicación(a, b):
    print("La multiplicación de ", a, "x", b, "=", a * b)

def division(a, b):
    if b == 0:
        print("No se puede dividir entre cero")
    else:
        print("La división de ", a, "/", b, "=", a / b)

def potencia(a, b):
    print("La potencia de ", a, "^", b, "=", a ** b)

introducirNumeros()
sumar(numero1, numero2)
restar(numero1, numero2)
multiplicación(numero1, numero2)
division(numero1, numero2)
potencia(numero1, numero2)