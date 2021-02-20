class Operaciones:
    def sumar(self, a, b):
        """Prueba unitaria"""
        return a + b

    def promedio(self, a, b):
        """Prueba unitaria"""
        suma = self.sumar(a, b)
        return suma / 2
