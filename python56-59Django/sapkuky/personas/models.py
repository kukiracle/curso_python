from django.db import models

# Create your models here.
#creamos clase de modelo Persona 
#y extendemos de una clase padre llamada models.Model para que ORM django
# se de cuenta que es una clase de modelo que afectara en la persistencia
# en la base de datos
class Domicilio(models.Model):
    calle=models.CharField(max_length=255)
    no_calle=models.IntegerField()
    pais=models.CharField(max_length=255)
    
    def __str__(self):
        return f'Domicilio#:{self.id}:{self.calle}:#{self.no_calle}:{self.pais}'
class Persona(models.Model):#models.Model es usado por el ORM para la bd
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    domicilio=models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
           #con todo esto django crea una tabla #personas_persona 
                                                #APP    nombre_clase   
                          
    def __str__(self):#para personalizar listado en la consola de administracion
        return f'Persona#: {self.id} :{self.nombre}: {self.apellido}: {self.email}'