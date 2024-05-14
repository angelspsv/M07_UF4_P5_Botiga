from rest_framework import serializers
from .models import Carrito
from cataleg.models import Catalogo
from usuarios.models import Usuarios

class CarritoSerializer(serializers.ModelSerializer):
        id_producto = serializers.PrimaryKeyRelatedField(queryset=Catalogo.objects.all())
        id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuarios.objects.all())

        class Meta:
            model = Carrito
            fields = ['id','id_carrito', 'id_producto', 'id_usuario', 'cantidad']
    


