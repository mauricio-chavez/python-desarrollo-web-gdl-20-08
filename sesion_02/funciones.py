# def sumar(a, b):
#     print(a + b)

# sumar(5, 4)

# def pares(x, y): # Inclusivo, exclusivo
#     nuevos_pares = []
#     for number in range(x, y):
#         if number % 2 == 0:
#             nuevos_pares.append(number)
#     return nuevos_pares

# for valor in range(1, 100000, 100):
#     pares(valor, valor + 100)

# mis_pares = pares(1, 100)
# print('El valor es:', mis_pares)

# def mi_funcion():
#     message = 'Hola'  
#     return message

# print(message) # No se puede acceder a mensaje porque tiene scope local

# message = 'adiós' # Scope global


# def otra_funcion(primero, segundo):
#     return primero + segundo

# otra_funcion(segundo=2, primero=1) # Una forma de pasar en desorden los parámetros


# # Argumentos de la función
# def mi_funcion_2(primero, opcional=20): # Los argumentos opcionales siempre van al final de los parámetros por posición
#     return primero + opcional


# mi_funcion_2(10, 30)  # 40
# mi_funcion_2(10)  # 10 + 20 = 30



# Argumentos arbitratios

def sumatoria(*numeros):  # La regla es que primero argumentos posicionales, luego opcionales y luego argitratios
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

sumatoria(1, 2, 3, 4, 5, 100, 200)

# Argumentos arbitrarios por llave (keyword arguments)

def crear_usuario(email, password, **parametros):
    user = {
        'email': email,
        'password': password
    }
    for key, value in parametros.items():
        user[key] = value
    return user


user = crear_usuario('mau@bedu.org', '12345', nombre='Mauricio')
print(user)


# Orden de argumentos

def funcion(posicional1, posicional2, opcional1=True, opcional2=20, *arbitrarios, **kwarbitrarios):
    return (posicional1, posicional2, opcional1, opcional2, arbitrarios, kwarbitrarios)
