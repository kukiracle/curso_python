"""sapkuky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from webapp.views import bienvenido,despedirse,contactar




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/',bienvenido) forma con URL bienvenido
    path('',bienvenido),#sin hacer nada aprecera la pagina hola mundo
    path('despedida.html',despedirse),#html igual funca o cualkierexten
    #, derecha es la funcion de view
    path('contactos.html',contactar),
    #path('api/v1/',include('usuario.urls'))
    path('api/v1/',include('users.urls'))
]
