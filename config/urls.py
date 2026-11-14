from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda.views import catalogo  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalogo, name='catalogo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
