from rest_framework import serializers
from .models import Catalogo


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['nombre', 'descripcion', 'id_seccion', 'precio', 'stock', 'peso']
