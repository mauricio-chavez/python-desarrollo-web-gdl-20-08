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

    def clear(self):
        """Clears stack"""
        return self.stack.clear()

    def __len__(self):
        """Returns stack size"""
        return len(self.stack)
