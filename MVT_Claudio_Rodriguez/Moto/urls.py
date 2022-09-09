from django.urls import path
from Moto.views import nueva_moto, lista_motos


urlpatterns = [
    path('lista-motos/', lista_motos, name='lista_motos'),
    path('nueva_moto/', nueva_moto, name='nueva_moto'),
]