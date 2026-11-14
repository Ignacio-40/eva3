from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Reemplaza 'tu_app' por el nombre real de la carpeta de tu aplicación
from tienda.views import lista_juegos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_juegos, name='inicio'),  # <--- Ruta principal
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
