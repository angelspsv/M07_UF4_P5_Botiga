from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Pagos
from .serializers import CarritoSerializer


# linies comentades per poder executar i provar el funcionament de la ruta confirm_card...
# from.models import UsuariosTarjetas
# from.serializers import UsuariosTarjetasSerializer



# funció per fer proves
@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)


# cogemos y accedemos a todos los carritos mediante
# id_carritos (GET) y leugo, mediante el serializer
# mostramos/modificamos el campo de carrito.finalizado de false a true (PUT)

@api_view(['GET', 'PUT'])
def update_pago_carrito(request):
    if request.method == 'GET':
        carrito = Pagos.objects.get(pk=pk)
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    if request.method == 'PUT':