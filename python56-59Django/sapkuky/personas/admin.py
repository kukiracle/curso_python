from django.contrib import admin
from personas.models import Persona,Domicilio  #importamos de app personas models.py la clase modelo Persona
# Register your models here.

admin.site.register(Persona) #registramos el modelo clase Persona
#y luego revisamos en la pagina admin que ya esta par crear objetos
admin.site.register(Domicilio)#otro registracion xd para la otra clase