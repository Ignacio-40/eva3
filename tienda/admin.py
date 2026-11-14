from django.contrib import admin
from .models import Categoria, Juego, Pedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'disponible', 'stock', 'precio_clp')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)

    @admin.display(description='Precio', ordering='precio')
    def precio_clp(self, obj):
        monto = int(round(obj.precio))
        return f"${monto:,}".replace(",", ".")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'juego', 'nombre_cliente', 'cantidad', 'fecha_hora')
    list_filter = ('juego',)
    search_fields = ('nombre_cliente', 'correo')
