"""Operaciones básicas de aritmética"""

def suma(*numeros):
    """Suma todos los números pasados como argumento"""
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    return resultado

def producto(*factores):
    """Multiplica todos los números pasados como argumento"""
    resultado = 1
    for factor in factores:
        resultado = resultado * factor
    return resultado

def promedio(*numeros):
    """Promedia todos los números pasados como argumento"""
    total = len(numeros)
    suma_numeros = suma(*numeros)
    return suma_numeros / total
