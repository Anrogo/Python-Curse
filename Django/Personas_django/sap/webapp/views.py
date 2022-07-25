from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse('Hola mundo desde Django')

def goodbye(request):
    return HttpResponse('Despedida desde Django')

def contact(request):
    return HttpResponse('Contacto: 61234578 <br> antonio@email.es')