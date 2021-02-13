def promedio(a, b):
    """Toma dos números y calcula el promedio"""
    try:
        return (a + b) / 2
    except TypeError:
        print('Ingresaste un dato no numérico')
        return 0
    except:
        print('Ha ocurrido un error')
        return 0


print(promedio(5, 4))
