def sumatoria(*mis_parametros):
    suma = 0
    for numero in mis_parametros:
        suma = suma + numero
    return suma


resultado = sumatoria(1, 2, 3, 4, 5)
print(resultado)


def crear_usuario(**parametros_extra):
    user = {
        'email': 'mauricio@bedu.org',
        'password': 'sdasdasd'
    }

    for llave in parametros_extra:
        user[llave] = parametros_extra[llave]

    print(user)


crear_usuario(birthday='01/01/2020', language='spanish')


def hola(email, password, *args, **kwargs):
    print(email, password)
    print(args)
    print(kwargs)


## Tipos de argumento

# Posicionales (obligatorios)

# Opcionales

# Posicionales arbitrarios

# Opcionales arbitrarios

## NOTA: El orden es importante: primero todos los posicionales, luego opcionales, después
# posicionales arbitrarios y al último opcionales arbitrarios
