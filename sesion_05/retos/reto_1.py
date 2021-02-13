def triple(funcion):
    def wrapper(*args, **kwargs):
        funcion(*args, **kwargs)
        funcion(*args, **kwargs)
        funcion(*args, **kwargs)
    return wrapper

@triple
def saludar():
    print('Hola')

@triple
def despedida(nombre):
    print('Adiós', nombre)


saludar()
despedida('Mauricio')
