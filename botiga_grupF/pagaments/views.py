from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Pagos
from .serializers import PagoSerializer


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
def pago_carrito(request):
    #validamos metodo
    if request.method != 'POST':
        return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)
    #validamos obj recibido
    serializer = PagoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)
    # validamos carrito existe
    carrito = get_object_or_404(Carrito, pk=serializer.id_carrito)

    #validamos existe usuario
    usuario = get_object_or_404(Usuarios, pk=serializer.id_usuario)

    #creamos pago
    serializer.save()

    #actualizamos carrito_finalizado (hist)
    carrito.finalizado = True
    carrito.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

