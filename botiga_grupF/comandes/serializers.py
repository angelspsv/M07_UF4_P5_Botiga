from rest_framework import serializers
from carrito.models import Carrito
from cataleg.models import Catalogo
from usuarios.models import Usuarios
from cataleg.serializers import ProductoSerializer
from usuarios.serializers import UsuariosSerializer

class ComandaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source='id_producto')  # Especifica el nombre del campo en el modelo Carrito
    usuario = UsuariosSerializer(source='id_usuario')  # Especifica el nombre del campo en el modelo Carrito

    class Meta:
        model = Carrito
        fields = ['id_carrito', 'producto', 'usuario', 'cantidad', 'finalizado']
