from django.shortcuts import render

from .models import Categoria, Juego, Pedido

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'lista_juegos.html', {'juegos': juegos})
def catalogo(request):
    juegos = Juego.objects.filter(disponible=True, stock__gt=0)
    return render(request, 'catalogo.html', {'juegos': juegos})