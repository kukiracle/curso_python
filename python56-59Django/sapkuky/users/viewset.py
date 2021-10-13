from .serializer import UserSerializer
#importamos del archivo serializer la clase UserSerializer que tenia 2 clases des
from .models import User# clase modelo User
from rest_framework import viewsets 

#creamos la clase UserViewset del urls
class UserViewset(viewsets.ModelViewSet):#siempre tiene 2 atributos
    queryset = User.objects.all()  #trae todos los users de la base de datos
    serializer_class = UserSerializer#trae todos los datos del modelos de serializer
    
    #ahora si importa a URLS