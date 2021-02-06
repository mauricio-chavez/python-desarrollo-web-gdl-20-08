def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    return resultado

def producto(*factores):
    resultado = 1
    for factor in factores:
        resultado = resultado * factor
    return resultado

def promedio(*numeros):
    total = len(numeros)
    suma_numeros = suma(*numeros)
    return suma_numeros / total


if __name__ == '__main__':
    print(suma(1, 2, 3))
