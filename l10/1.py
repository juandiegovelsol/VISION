import unittest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# === PRUEBAS UNITARIAS ===
class TestOperaciones(unittest.TestCase):
    def setUp(self):
        pass  # Opcional: código que se ejecuta antes de cada prueba

    def test_suma(self):
        esperado = 3
        actual = suma(1, 2)
        self.assertEqual(actual, esperado)

    def test_resta(self):
        esperado = 5
        actual = resta(10, 5)
        self.assertEqual(actual, esperado)

    def test_multiplicacion(self):
        esperado = 50
        actual = multiplicacion(10, 5)
        self.assertEqual(actual, esperado)

# === EJECUCIÓN DE LAS PRUEBAS ===
if __name__ == '__main__':
    unittest.main()
