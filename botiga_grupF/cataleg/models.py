from django.db import models

# tabla de secciones de productos
class CatalogoSecciones(models.Model):
    id_seccion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


# tabla de productos
class Catalogo(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    id_seccion = models.ForeignKey(CatalogoSecciones, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    peso = models.IntegerField()

