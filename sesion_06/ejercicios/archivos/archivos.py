# def read_plain_text():
#     file = open('./ejemplo.txt')
#     contenido = ''
#     for line in file.readlines():
#         contenido += line
#     file.close()
#     return contenido


# def write_plain_text():
#     texto = input('Agregar texto: ')
#     file = open('./ejemplo.txt', 'a')
#     file.write(texto + '\n')
#     file.close()


# def overwrite_plain_text():
#     texto = input('Sobreescribir texto: ')
#     file = open('./ejemplo.txt', 'w')
#     file.write(texto + '\n')
#     file.close()


def read_plain_text():
    with open('./ejemplo.txt') as file:
        contenido = ''
        for line in file.readlines():
            contenido += line
        return contenido


def write_plain_text():
    texto = input('Agregar texto: ')
    with open('./ejemplo.txt', 'a') as file:
        file.write(texto + '\n')


def overwrite_plain_text():
    with open('./ejemplo.txt', 'w') as file:
        texto = input('Sobreescribir texto: ')
        file.write(texto + '\n')
