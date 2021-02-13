import csv
import datetime

adding = True

while adding:
    name = input('Inserte nombre del auto: ')
    color = input('Inserte color: ')
    level = input('Inserte nivel de equipo: ')
    price = input('Inserte precio: ')
    now = datetime.datetime.now()
    with open('cars.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, color, level, price, now])
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
