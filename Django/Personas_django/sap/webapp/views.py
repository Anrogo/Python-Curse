from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def welcome(request):
    no_personas_var = Persona.objects.count()
    no_domicilios_var = Domicilio.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id','nombre')
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'welcome.html',{'no_personas': no_personas_var, 'list_personas': personas, 'no_domicilios': no_domicilios_var, 'list_domicilios': domicilios})


