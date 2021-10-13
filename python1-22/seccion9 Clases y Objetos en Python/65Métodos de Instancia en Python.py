#definimos la clase
class Persona:
    def __init__(self, nombre, apellido, edad): #funciones dunder __ __
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def mostrar_detalle(self):  #obligatorio colocar self=this
        print(self.nombre, self.apellido, self.edad)
    

#creando objeto

p1=Persona('juan','perez',18)
p1.mostrar_detalle()

p2=Persona('karla','gomez','30')

p2.mostrar_detalle()