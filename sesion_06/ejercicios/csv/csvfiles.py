import csv

# Lectura
with open('ventas.csv') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)

# Escritura
with open('ventas.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([3000, 'Mundo', 'Mauricio', 'JavaScript'])

# Lectura (diccionarios)
with open('users.csv') as csvfile:
    rows = csv.DictReader(csvfile)

    for row in rows:
        message = 'El correo es ' + row['correo']
        print(message)


# Escritura (diccionarios)
with open('users.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, ['nombre', 'apellidos', 'correo', 'lenguaje'])
    writer.writeheader()
    writer.writerow({
        'nombre': 'Mauricio',
        'apellidos': 'Chávez Olea',
        'correo': 'mauricio@bedu.org',
        'lenguaje': 'Python'
    })
    writer.writerow({
        'nombre': 'Jorge',
        'apellidos': 'Olmos',
        'correo': 'jorge@bedu.org',
        'lenguaje': 'Elixir'
    })
    writer.writerow({
        'nombre': 'Laura',
        'apellidos': 'Ramos',
        'correo': 'laura@bedu.org',
        'lenguaje': 'JavaScript'
    })
    writer.writerow({
        'nombre': 'Ximena',
        'apellidos': 'Ortiz',
        'correo': 'ximena@bedu.org',
        'lenguaje': 'Kotlin'
    })
