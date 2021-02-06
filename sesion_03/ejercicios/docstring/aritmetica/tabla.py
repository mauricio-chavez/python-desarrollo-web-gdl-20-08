"""Utilería de tablas"""

# Documentación de funciones y de módulos, abajo y arriba respectivamente

def tabla_multiplicacion(n):
    """Muestra la tabla de multiplicar del número especificado"""
    for i in range(1, 11):
        print('{}x{}={}'.format(n, i, n*i))
