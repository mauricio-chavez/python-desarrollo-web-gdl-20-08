import json

user = {
    'email': 'mauricio@bedu.org',
    'first_name': 'Mauricio',
    'last_name': 'Chávez Olea',
    'is_active': True
}

# Escritura (cadena de texto)
resultado = json.dumps(user)
print(resultado)

# Lectura (cadena de texto)
raw_json = '{"email": "mauricio@bedu.org", "first_name": "Mauricio", "last_name": "Ch\u00e1vez Olea", "is_active": true}'
my_user = json.loads(raw_json)
print(my_user)


user = {
    'email': 'mauricio@bedu.org',
    'first_name': 'Mauricio',
    'last_name': 'Chávez Olea',
    'is_active': True
}

# Escritura
with open('user.json', 'w') as jsonfile:
    resultado = json.dump(user, jsonfile, indent=2)

# Lectura
with open('user.json', 'r') as jsonfile:
    my_user = json.load(jsonfile)
    print(my_user)
