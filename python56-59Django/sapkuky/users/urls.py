from rest_framework.routers import SimpleRouter
from .viewset import UserViewset

route=SimpleRouter()#definimos router

route.register('users',UserViewset) #ruta registrada

urlpatterns=route.get_urls()#con esto mandamos a la ruta padre de URLS es un export

#con esta ruta buscara por GET PUT POST DELETE y esas cosas :V

