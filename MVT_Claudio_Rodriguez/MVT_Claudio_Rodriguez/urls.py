
from django.contrib import admin
from django.urls import path, include
from Moto.views import nueva_moto, lista_motos
from MVT_Claudio_Rodriguez.views import saludo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name = 'saludo'),
    path('nueva_moto/', nueva_moto, name='nueva_moto'),
    path('lista_motos/', lista_motos, name='lista_motos'),
]
