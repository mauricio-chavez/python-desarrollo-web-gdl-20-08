# PILARES DE LA ORIENTACION A OBJETOS: Abstracción, encapsulación, herencia y polimorfismo

# Abstracción: Generalizar comportamiento

# Encapsulación: Restringir el acceso a propiedades y métodos de un objeto
class Objeto:
    __privado = 'esto no debería ser accesado'

    def get_privado(self):
        return self.__privado.upper()

    def set_privado(self, cadena):
        self.__privado = cadena.lower()

obj = Objeto()
# print(obj.__privado) # ERROR
obj.set_privado('ASDGHAJSDASD')
print(obj.get_privado())


# Herencia: Copiar comportamiento de una clase padre
class Animal:
    pass

class Mascota(Animal):
    pass

# Polimorfismo: Dos objetos de diferente tipo de comportan igual al ser llamados con el mismo método
from datetime import datetime

mascota = Mascota()
hoy = datetime.now()

mascota.__str__()
hoy.__str__()
