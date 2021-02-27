def puntos_dobles(funcion):
    def envoltorio(actual, puntaje):
        dobles = puntaje * 2
        return funcion(actual, dobles)

    return envoltorio


@puntos_dobles
def sumar_puntos(actual, puntaje):
    """Suma puntos al puntaje aactual"""
    return actual + puntaje


@puntos_dobles
def restar_puntos(actual, puntaje):
    return actual - puntaje


if __name__ == '__main__':
    puntos = sumar_puntos(100, 20)
    print(puntos)
