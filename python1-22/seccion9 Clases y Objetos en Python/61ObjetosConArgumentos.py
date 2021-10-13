#definimos la clase
class Persona:
    def __init__(self, nombre, apellido, edad): #funciones dunder __ __
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    

#creando objeto

p1=Persona('juan','perez',18)
print(p1.nombre,p1.apellido,p1.edad)

