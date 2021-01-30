diccionario = {}
user = {
    'email': 'mauricio@bedu.org',
    'usuario': 'mauricio',
    'contraseña': '12345',
    'año de unión': 2006
}

# Leer datos
email = user['email']

# Agregar datos
user['nombre'] = 'Mauricio' # Se agrega si no existe, si no se actualiza

# Actualizar datos
user['nombre'] = 'Miguel'

# Eliminar datos
del user['nombre']
nombre = user.pop('nombre')
