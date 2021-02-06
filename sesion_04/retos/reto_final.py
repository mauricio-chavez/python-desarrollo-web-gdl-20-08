stack = Stack()

stack.push()  # Meter un elemento a la pila
deleted = stack.pop()  # Elimina el último elemento que entró y lo devuelve
stack.peak()  # Ve el último elemento que entró


# Esperado
stack.push('elefante')
stack.push('conejo')
stack.push('gato')


elemento = stack.pop()  # gato
otro_elemento = stack.peak()  # conejo
