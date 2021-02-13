class Vector:
    """Vector simple para sumar"""

    def __init__(self, x, y):
        """Constructor que acepta X y Y como parámetros"""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Suma dos vectores"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __str__(self):
        """Regresa una representación en cadena de el vector"""
        return '<{}, {}>'.format(self.x, self.y)

vector1 = Vector(5, 4)
vector2 = Vector(3, 8)

vector3 = vector1 + vector2

print(vector3)

"""
<5, 4> + <3, 8> = <5 + 3, 4 + 8> = <8, 12>
"""
