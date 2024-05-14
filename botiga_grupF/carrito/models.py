from django.db import models
from cataleg.models import Catalogo
from usuarios.models import Usuarios

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Catalogo, on_delete=models.CASCADE)  # Producto en el carrito
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)  # Usuario que tiene el carrito
    id_carrito = models.IntegerField()  # Campo personalizado, no auto-generado
    cantidad = models.PositiveIntegerField(default=1)  # Campo para la cantidad de productos, por defecto 1
    finalizado = models.BooleanField(default=False)  # Indica si el carrito está finalizado

    def __str__(self):
        return f"Carrito {self.id_carrito} para Usuario {self.id_usuario} con {self.cantidad} productos"
