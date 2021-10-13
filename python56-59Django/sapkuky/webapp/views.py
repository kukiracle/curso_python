from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola Mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde DJANGO con con formato html')

def contactar(request):
    return HttpResponse('nombre:Kuky cel:7456891')
    