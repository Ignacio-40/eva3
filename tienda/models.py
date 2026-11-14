from django.db import models
import uuid


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="juegos")
    imagen = models.ImageField(upload_to="juegos/", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    jugadores = models.PositiveIntegerField(default=1)
    edadmin = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
class Pedido(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="pedidos")
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return f"pedido {self.codigo} - {self.nombre_cliente}"
    