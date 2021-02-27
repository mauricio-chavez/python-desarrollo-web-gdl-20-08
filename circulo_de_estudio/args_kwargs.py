"""Argumentos arbitrarios"""


def mi_funcion(a1, a2, promedio=False):
    """Explica los tipos de argumentos"""
    resultado = a1 + a2

    if promedio:
        resultado = resultado / 2

    return resultado


# mi_funcion(1, 2)  # 3
#
#
# mi_funcion(1, 3, True)
#
#
# mi_funcion(a2=3, promedio=True, a1=5)


def sumatoria(*numeros):
    """Argumentos arbitrarios"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


def create_user(email, password, **attributes):
    user = {
        "email": email,
        "password": password
    }

    for key in attributes:
        user[key] = attributes[key]

    return user


# Es importante el orden, primero van los posicionales, luego van los opcionales,
# luego los posicionales arbitrarios (args) y finalmente los llave valor arbitrarios (kwargs)

if __name__ == '__main__':
    user = create_user('mauricio@nerds.ai', 'miContraseñaSegura123', birthday='21 de diciembre', lenguaje='Elixir')
    print(user)
