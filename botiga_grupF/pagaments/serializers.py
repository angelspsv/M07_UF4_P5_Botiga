from rest_framework import serializers
from .models import Pagos


class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagos
        fields = ['id_pago', 'id_carrito', 'id_usuario']
