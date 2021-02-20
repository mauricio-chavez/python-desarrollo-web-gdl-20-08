from stack import Stack

def test_push():
    """Tests that pushing to a stack is correct"""
    stack = Stack()
    assert len(stack) == 0

    stack.push('elefante')
    assert stack.peak() == 'elefante'
    assert len(stack) == 1
    stack.clear()

def test_pop():
    """tests pop"""
    stack = Stack()
    stack.push('leon')
    assert len(stack) == 1

    popped_item = stack.pop()
    assert popped_item == 'leon'
    assert len(stack) == 0
    stack.clear()

def test_peak():
    """tests pop"""
    stack = Stack()
    stack.push('jirafa')
    assert len(stack) == 1

    peaked_item = stack.peak()
    assert peaked_item == 'jirafa'
    assert len(stack) == 1
    stack.clear()
