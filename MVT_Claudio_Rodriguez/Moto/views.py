from django.shortcuts import render,redirect
from Moto.models import Moto
from datetime import datetime

def nueva_moto(request):
    nueva_moto = Moto.objects.create(marca = "Yamaha", modelo = "MT03", cilindrada = 320, precio = 2896500, fecha_de_creacion = datetime.today())
    context = {
        'nueva_moto': nueva_moto
    }
    return render(request, 'nueva_moto.html', context=context)


def lista_motos(request):
    motos = Moto.objects.all() 
    context = {
        'motos':motos
    }
    return render(request, 'lista_motos.html', context=context)
    

