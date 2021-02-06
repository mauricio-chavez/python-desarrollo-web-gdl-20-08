def producto(*factores):
    resultado = 1
    for factor in factores:
        resultado = resultado * factor
    return resultado


def directorio(**contactos):
    contactos_ordenados = sorted(contactos)
    for contacto in contactos_ordenados:
        print(contacto + ' - ' + contactos[contacto])


directorio(Mau='11223344', Jorge='55443322', Paulina='123123')