import os

files = os.listdir('./ejemplo')
print(files)


size = os.path.getsize('./ejemplo/archivo.txt')
print('Tamaño en bytes:', size)


print(os.name)

# Formas de importar
import os
import os.path
from os.path import getsize
from os.path import getsize as obtener_bytes  # Alias

size = obtener_bytes('./ejemplo/archivo.txt')
print('Tamaño en bytes:', size)
