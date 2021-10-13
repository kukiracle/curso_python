from .serialiser import UsuarioSerializer
from .models import Usuario
from rest_framework import viewsets 

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class=UsuarioSerializer
    