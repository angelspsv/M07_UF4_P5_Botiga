from rest_framework import serializers
from .models import Catalogo, CatalogoSecciones

# serializer de modelo CatalogoSecciones que
# maneja estos campos del CatalogoSecciones
class CatalogoSeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoSecciones
        fields = ['id_seccion', 'nombre']


# serializer de modelo Catalogo y
# maneja estos campos del Catalogo
class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalogo
        fields = ['id_producto', 'nombre', 'descripcion', 'id_seccion', 'precio', 'stock', 'peso']

