"""Herencia"""

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

    def __str__(self):
        return self.nombre


class Perro(Mascota):
    """Mascota de tipo perro"""

    def __init__(self, nombre):
        """Sobreescritura de métodos"""
        super().__init__(nombre, 'perro')

    def cavar(self):
        """Sobrecarga de métodos"""
        print('*{} está cavando un hoyo*'.format(self.nombre))

    def sonar(self):
        """Ladra"""
        print('Guau!')


pluto = Perro('Pluto')

pluto.cavar()
pluto.mover()
pluto.comer('carne')
pluto.sonar()


# Requisito: 2 mascotas nuevas, sobreescribir __init__ y poner el método sonar
