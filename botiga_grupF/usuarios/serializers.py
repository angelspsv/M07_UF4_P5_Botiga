from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios  # Modelo asociado al serializer
        fields = ['id', 'email', 'nombre', 'primer_apellido', 'segundo_apellido', 'password']  # Campos a serializar