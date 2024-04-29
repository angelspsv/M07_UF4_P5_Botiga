from rest_framework import serializers
from .models import Catalogo

# serializer de modelo Catalogo y
# maneja estos campos del Catalogo
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'id_seccion', 'precio', 'stock', 'peso']
