class EmptyStackError(Exception):
    pass


class Stack:
    """LIFO data structure"""
    stack = []

    def push(self, e):
        """Puts an element at the top of the stack"""
        self.stack.append(e)

    def pop(self):
        """Gets top element and removes it"""
        if not self.stack:
            raise EmptyStackError('La pila está vacía')
        return self.stack.pop()

    def peak(self):
        """Shows top element"""
        if not self.stack:
            raise EmptyStackError('La pila está vacía')
        return self.stack[-1]

    def __str__(self):
        """Returns a string representation of stack"""
        stack = ''
        for element in reversed(self.stack):
            stack += '{}\n'.format(element)

        stack += '-' * 10
        return stack


stack = Stack()

try:
    stack.push('elefante')
    elemento = stack.pop()
except EmptyStackError:
    print('El stack está vacío')
    elemento = None
except TypeError:
    print('Los argumentos no son válidos')
    elemento = None
except:
    print('Ha ocurrido un error')
    elemento = None
    
print('El elemento es', elemento)
