import unittest
from unittest.mock import MagicMock
from stack import Stack
from operaciones import Operaciones


class StackTestCase(unittest.TestCase):
    """Suite de pruebas para el stack"""

    def setUp(self):
        """Instanciates stack"""
        self.stack = Stack()

    def test_push(self):
        """Tests that pushing to a stack is correct"""
        self.assertEqual(len(self.stack), 0)
        self.stack.push('elefante')
        self.assertEqual(self.stack.peak(), 'elefante')
        self.assertEqual(len(self.stack), 1)

    def test_pop(self):
        """tests pop"""
        self.stack.push('leon')
        self.assertEqual(len(self.stack), 1)

        popped_item = self.stack.pop()
        self.assertEqual(popped_item, 'leon')
        self.assertEqual(len(self.stack), 0)

    def test_peak(self):
        """tests pop"""
        self.stack.push('jirafa')
        self.assertEqual(len(self.stack), 1)

        peaked_item = self.stack.peak()
        self.assertEqual(peaked_item, 'jirafa')
        self.assertEqual(len(self.stack), 1)

    def test_peak_in_empty_stack(self):
        """tests peak with an empty stack"""
        self.assertEqual(len(self.stack), 0)
        with self.assertRaises(IndexError):
            self.stack.peak()

    def test_mock(self):
        """Tests with a mock"""
        self.stack.peak = MagicMock(return_value='gato')
        peaked_item = self.stack.peak()
        self.assertEqual(peaked_item, 'gato')

    def tearDown(self):
        """Clears stack"""
        self.stack.clear()


class OperacionesTestCase(unittest.TestCase):
    """Suite de pruebas con mocks"""

    def test_suma(self):
        operaciones = Operaciones()
        resultado = operaciones.sumar(5, 4)
        self.assertEqual(resultado, 9)

    def test_promedio(self):
        operaciones = Operaciones()
        operaciones.sumar = MagicMock(return_value=6)
        resultado = operaciones.promedio(10, 5)
        self.assertEqual(resultado, 3)


if __name__ == '__main__':
    unittest.main()
