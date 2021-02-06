class Persona:
    __energia = 10

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def caminar(self):
        self.__energia -= 1
        print('{} está caminando...'.format(self.nombre))

    def comer(self):
        self.__energia += 1
        print('{} está comiendo...'.format(self.nombre))

    def __str__(self):
        return self.nombre


mau = Persona('Mauricio', 'Chavez')
mau.caminar()
mau.caminar()
mau.caminar()
