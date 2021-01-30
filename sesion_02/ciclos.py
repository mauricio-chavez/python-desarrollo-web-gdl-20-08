age = 12

while age < 18:
    print('No puedes entrar, tienes {} años'.format(age))
    age = age + 1

# Para salir de un ciclo infinito, es CONTROL-C
print('Ya puedes entrar')


count = 1

while True:
    print(count)
    if count == 10:
        break # Termina el ciclo
    count += 1 # Atajo para count = count + 1


count = 0

while count <= 10:
    count += 1

    if count % 2 == 0: # Es un par
        continue # Continua la iteración

    print('Cuenta:', count)

peliculas = ['django', 'pulp fiction', 'inglorious basterds']

for pl in peliculas:
    message = 'La pelicula es {}'.format(pl.title())
    print(message)


# # 0, 1, 2, 3, 4
for i in range(5):  # Fin (exclusivo)
    print(i)


# # 5, 6, 7, 8, 9, 10
for i in range(5, 11):  # Inicio (inclusivo), fin (exclusivo)
    print(i)

# 2, 4, 6, 8, 10
for i in range(2, 11, 2): # Inicio (inclusivo), fin (exclusivo), paso (cuantos va a saltar)
    print(i)


user = {
    'full_name': 'Mauricio Chávez Olea',
    'email': 'mauricio@bedu.org',
    'password': '12345'
}

for key in user:
    message = 'Llave: {} Valor: {}'.format(key, user[key])
    print(message)

for key, value in user.items():
    message = 'Llave: {} Valor: {}'.format(key, value)
    print(message)
