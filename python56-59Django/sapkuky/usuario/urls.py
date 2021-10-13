from rest_framework.routers import SimpleRouter
from .viewset import UsuarioViewSet


route =SimpleRouter()

route.register('usuario',UsuarioViewSet)

urlpatterns=route.get_urls()