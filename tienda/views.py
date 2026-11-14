from django.shortcuts import render

from .models import Categoria, Juego, Pedido

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'lista_juegos.html', {'juegos': juegos})