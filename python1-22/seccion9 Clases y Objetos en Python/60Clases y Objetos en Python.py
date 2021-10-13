#definimos la clase
class Persona:
    def __init__(self): #funciones dunder __ __
        self.nombre='juan'
        self.apellido='perez'
        self.edad=28
    
    

#creando objeto

p1=Persona()
print(p1.nombre,p1.apellido,p1.edad)

