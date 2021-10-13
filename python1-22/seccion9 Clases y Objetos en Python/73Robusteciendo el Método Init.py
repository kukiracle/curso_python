#definimos la clase
class Persona:
    def __init__(self, nombre, apellido, edad,*tupla,**diccionario): #args=tuplas **kwargs diccionario
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.tupla=tupla
        self.diccionario=diccionario
        
    def mostrar_detalle(self):  #obligatorio colocar self=this
        print(self.nombre, self.apellido, self.edad, self.tupla, self.diccionario)
    

#en python se puede agregar atributos nuevos
# a un objeto al vuelo xd :V
#este atributo nose comparte con los demas objetos ni con la clase





p1=Persona('juan','perez',18,'444432423423',2,3,5,IDE='IntegratedDevelopment',OOP='opppppp')
#al fusionar siempre respetando el orden de las tuplas y diccionarios para

p1.mostrar_detalle()
#las tulplas salen en () y el diccionario en {}

