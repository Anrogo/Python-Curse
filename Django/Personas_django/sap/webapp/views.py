from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def welcome(request):
    no_personas_var = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'welcome.html',{'no_personas': no_personas_var, 'list_personas': personas})

