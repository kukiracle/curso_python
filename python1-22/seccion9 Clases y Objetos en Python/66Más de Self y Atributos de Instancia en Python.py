#definimos la clase
class Persona:
    def __init__(self, nombre, apellido, edad): #funciones dunder __ __
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def mostrar_detalle(self):  #obligatorio colocar self=this
        print(self.nombre, self.apellido, self.edad)
    

#en python se puede agregar atributos nuevos
# a un objeto al vuelo xd :V
#este atributo nose comparte con los demas objetos ni con la clase




p1=Persona('juan','perez',18)
p1.telefono='772456123'
p1.mostrar_detalle()
print(p1.telefono)

p2=Persona('karla','gomez','30')

Persona.mostrar_detalle(p2)
