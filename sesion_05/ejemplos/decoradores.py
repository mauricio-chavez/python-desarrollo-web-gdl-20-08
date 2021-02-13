def puntos_dobles(funcion):
    def envoltorio(puntaje):
        return funcion(puntaje) + 100
    return envoltorio

@puntos_dobles
def matar(puntaje):
    return puntaje + 100

@puntos_dobles
def comer(puntaje):
    return puntaje + 50


puntaje = 200
nuevo_puntaje = matar(puntaje)
print(nuevo_puntaje)
