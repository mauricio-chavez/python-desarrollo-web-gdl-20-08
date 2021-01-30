conjunto = set()
conjunto = {1, 2, 3, 4, 5, 'pizza'}
no_conjunto = {}  # esto es un diccionario


conjunto.add(2)
conjunto.add(2) # Solo entra una vez

conjunto.remove('pizza') # Se pasa el valor que se quiere eliminar

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Union
print(conjunto1 | conjunto2) 
print(conjunto1.union(conjunto2))  


# Interseccion
print(conjunto1 & conjunto2) 
print(conjunto1.intersection(conjunto2))  
