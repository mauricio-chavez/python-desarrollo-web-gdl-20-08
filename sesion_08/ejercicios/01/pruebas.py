import unittest

from operaciones import sumar, promedio


class OperacionesTestCase(unittest.TestCase):
    """Suite de pruebas para operaciones"""

    def test_sumar(self):
        resultado = sumar(1, 2)
        esperado = 3
        self.assertEqual(resultado, esperado)

    def test_promedio(self):
        resultado = promedio(2, 2)
        esperado = 2
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
