class Stack:
    """LIFO data structure"""
    stack = []

    def push(self, e):
        """Puts an element at the top of the stack"""
        self.stack.append(e)

    def pop(self):
        """Gets top element and removes it"""        
        return self.stack.pop()

    def peak(self):
        """Shows top element"""
        return self.stack[-1]

    def __str__(self):
        """Returns a string representation of stack"""
        stack = ''
        for element in reversed(self.stack):
            stack += '{}\n'.format(element)
        
        stack += '-' * 10
        return stack


stack = Stack()

# Esperado
stack.push('elefante')
stack.push('conejo')
stack.push('gato')

elemento = stack.pop()  # gato
print('Es gato:', elemento == 'gato')

otro_elemento = stack.peak()  # conejo
print('Es conejo:', otro_elemento == 'conejo')

print('Stack:', stack)
