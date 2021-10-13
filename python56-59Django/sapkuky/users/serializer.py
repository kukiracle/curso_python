from rest_framework import serializers 
from users.models import User #importamos del app users models.py clase User
#este archivo dara serializara en formato objeto json el modelo indicado
class UserSerializer(serializers.ModelSerializer):
    #clase dentro de una clase 
    class Meta:     
        model=User #importamos el modelo clase User
        fields='__all__'#tupla que importara todo de golpe del modelo lo que quiero mostrar
        
    