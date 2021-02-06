def get_name():
    return 'Mauricio'

def get_language():
    return 'Python'

def get_message():
    language = get_language()
    return 'Hola, mi nombre es {} y mi lenguaje favorito es {}'.format(get_name(), language)


message = get_message()
print(message)


def sumar(a, b):
    return a + b


print(sumar(4, 5))
