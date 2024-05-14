from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Pagos
from .serializers import PagoSerializer
from carrito.models import Carrito
from usuarios.models import Usuarios
from carrito.serializers import CarritoSerializer
from rest_framework.views import APIView


# funció per fer proves
@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)


# se escribe la ruta /pagar_carrito/id/ donde la 'id' es la id_carrito
# al hacer PUT se actualiza el campo historico de carrito de false a true
# muestra un mensaje de "Carrito updated successfully"

@api_view(['PUT'])
def pago_carrito(request, pk):
    if request.method == 'PUT':
        try:
            carrito = Carrito.objects.get(id_carrito=pk)
        except Carrito.DoesNotExist:
            return Response({'error': 'Carrito not found'}, status=status.HTTP_404_NOT_FOUND)

        carrito.finalizado = True
        carrito.save()

        return Response({'message': 'Carrito updated successfully'}, status=status.HTTP_200_OK)
