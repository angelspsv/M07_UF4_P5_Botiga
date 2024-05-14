from rest_framework import serializers
from .models import Pagos

# serializer de modelo Pagos
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = ['id_pago', 'id_carrito', 'id_usuario']
