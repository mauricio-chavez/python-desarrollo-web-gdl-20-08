lista = []
lista = list()

canciones = ['Wonderwall', 'Starlight',]

# Acceder a los elementos de la lista
primero = canciones[0]
segundo = canciones[1]
ultimo = canciones[-1]
penultimo = canciones[-2]

# Agregar datos a la lista
canciones.append('Jailhouse Rock')  # Agrega al final
canciones.insert(1, 'Bohemian Rhapsody')  # Agrega en la posición indicada, desplazando las demás
canciones[0] = 'Champagne Supernova' # Sustituye el valor original

# Slices (tomar una parte de la lista)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
otros_numeros = numeros[:]  # Hace copias exactas sin hacer referencia a la misma lista

del_5_al_9 = numeros[4:9]
del_1_al_6 = numeros[:6] # Shortcut
del_4_al_10 = numeros[3:] # Shortcut
todos_los_numeros = numeros[:]

# Los strings también pueden hacer slices 
mundo = 'Hola, mundo'[6:]

# Eliminar datos de la lista
peliculas = ['Django', 'Batman', 'La La Land']

del peliculas[1] # Elimina el segundo elemento (Batman)
batman = peliculas.pop(1) # Elimina en la posición indicada y lo regresa
la_la_land = peliculas.pop() # Elimina siempre la última posición

# Convertir a lista una cadena
cadena_lista = list('abc123')

# Métodos (o funciones) utilitarias
longitud = len(['Hola', 'mundo'])
maximo = max([23, 45, 67, 13, 1, 32])
minimo = min([23, 45, 67, 13, 1, 32])
al_reves = list(reversed([1, 2, 3, 4, 5]))

# List comprehension
cuadrados = [x**2 for x in range(1, 11)]

# Esto es igual a esto...

cuadrados = []
for x in range(1, 11):
    cuadrados.append(x**2)
