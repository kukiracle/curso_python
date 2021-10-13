# definimos la clase
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # sugerencia de encapsulado
        self.__apellido = apellido  # encapsulado total  nose puede cambiar
        self.edad = edad

    def mostrar_detalle(self):  # obligatorio colocar self=this
        print(self._nombre, self.__apellido, self.edad)

    @property  # permite decorar _nombre para solo llamar nombre
    def nombre(self):
        print('usando getnombre')
        return self._nombre

    @nombre.setter  # para usar desde los objetos el atributo feo __nombre por solo nombre
    def nombre(self, nombre):
        print('usando setnombre')
        self._nombre = nombre

    @property  # permite
    def apellido(self):
        print('usando getapellido')
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        print('usando setapellido')
        self.__apellido = apellido

# uno solo _ significa sugerencia que no accedas
# __ significa como private no te deja ni cambiar
# se ven feos __ estos encapsulamientos
# usaremos un decorador @property para decorar:v


p1 = Persona('juan', 'perez', 18)

p1.apellido = 'quispe'
print(p1.nombre, p1.apellido)
