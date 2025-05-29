# Función para introducir dos números desde la terminal
def introducirNumeros ():
    """
    La funcion solicita al usuario que introduzca dos números enteros.
    Los almacena como variables globales numero1 y numero2.
    """
    global numero1, numero2
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))

# Función para sumar dos números
def sumar (a, b):
    """
    Muestra en pantalla la suma de a y b.
    """
    print("La suma de ", a, " + ", b, " = ", a + b)

# Función para restar dos números
def restar (a, b):
    """
    Muestra en pantalla la resta de a menos b.
    """
    print("La resta de ", a, " - ", b, " = ", a - b)

# Función para multiplicar dos números
def multiplicación (a, b):
    """
    Muestra en pantalla el producto de a por b.
    """
    print("La multiplicación de ", a, " x ", b, " = ", a * b)

# Función para dividir dos números
def division (a, b):
    """
    Muestra en pantalla el cociente de a entre b.
    Verifica que b no sea cero antes de dividir.
    """
    if b == 0:
        print("No se puede dividir entre cero")
    else:
        print("La división de ", a, " / ", b, " = ", a / b)

# Función para calcular la potencia de un numero de base a y exponente b
def potencia (a, b):
    """
    Muestra en pantalla la potencia de a elevado a b.
    Es decir, a^b.
    """
    print("La potencia de ", a, " ^ ", b, " = ", a ** b)

# Ejecución de las funciones
introducirNumeros()
sumar(numero1, numero2)
restar(numero1, numero2)
multiplicación(numero1, numero2)
division(numero1, numero2)
potencia(numero1, numero2)