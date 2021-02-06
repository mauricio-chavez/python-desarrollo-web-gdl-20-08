class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def caminar(self):
        print('{} está caminando...'.format(self.nombre))

    def __str__(self):
        return self.nombre

    def __del__(self):
        print('Eliminando a {}'.format(self.nombre))

    def __bool__(self):
        return True

mau = Persona('Mauricio', 'Chávez')
mau.caminar()

# rodrigo = Persona('Rodrigo', 'Jiménez')
# rodrigo.caminar()

# monica = Persona('Mónica', 'Otero')
# monica.caminar()
