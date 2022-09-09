
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola")

def home(request):
    context = {
        'name':'Claudio',
        'last_name':'Rodriguez',
    }
    return render(request, 'Base.html', context=context)

