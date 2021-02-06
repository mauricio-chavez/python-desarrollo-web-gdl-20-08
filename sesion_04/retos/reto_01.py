"""Reto 01"""


class Mascota:
    """Crea una mascota con nombre, tipo y 10 de energía"""
    energia = 10

    def __init__(self, nombre, tipo):
        """Instancia una nueva mascota"""
        self.nombre = nombre
        self.tipo = tipo

    def mover(self):
        """Mueve a la mascota y consume 1 de energía, si ya no tiene energía no podrá moverse"""
        if self.energia > 0:
            print('*{} se está moviendo*'.format(self.nombre))
            self.energia = self.energia - 1
        else:
            print('*{} ya no tiene energía, aliméntalo*'.format(self.nombre))

    def comer(self, comida):
        """Come la comida especificada. Si tiene 10 de energía ya no podrá comer"""
        if (self.energia < 10):
            print('*{} está comiendo {}*'.format(self.nombre, comida))
            self.energia = self.energia + 1
        else:
            print('*{} ya no puede comer*'.format(self.nombre))

    def sonar(self):
        """Hace un sonido dependiendo de el tipo de mascota"""
        if self.tipo == 'gato':
            print('Miaww')
        elif self.tipo == 'perro':
            print('Guau!')
        elif self.tipo == 'pez':
            print('blu blu')
        elif self.tipo == 'serpiente':
            print('ssss....')

    def __str__(self):
        return self.nombre


gato = Mascota('Garfield', 'gato')
perro = Mascota('Pluto', 'perro')
pez = Mascota('Nemo', 'pez')


for _ in range(11):
    gato.mover()

for _ in range(11):
    gato.comer('lasagna')

