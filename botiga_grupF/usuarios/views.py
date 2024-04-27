from rest_framework import viewsets
from .models import Usuarios
from .serializers import UsuariosSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()  # El conjunto de datos sobre el cual se ejecutarán las operaciones
    serializer_class = UsuariosSerializer  # El serializer utilizado para transformar datos entre modelo y JSON
