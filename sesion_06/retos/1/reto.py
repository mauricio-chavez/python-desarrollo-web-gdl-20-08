adding = True

while adding:
    name = input('Inserte nombre del auto: ')
    color = input('Inserte color: ')
    level = input('Inserte nivel de equipo: ')
    price = input('Inserte precio: ')
    with open('cars.txt', 'a') as file:
        row = '{}\t{}\t{}\t{}\n'.format(name, color, level, price)
        file.write(row)
    while True:
        must_continue = input('¿Agregar otro auto? [s/N] ')
        option = must_continue.lstrip().lower()
        if option.startswith('s'):
            break
        elif option.startswith('n'):
            adding = False
            break
        else:
            print('Respuesta no válida')
