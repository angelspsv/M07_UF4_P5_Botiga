from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Pagos
from .serializers import ProductoSerializer
# linies comentades per poder executar i provar el funcionament de la ruta confirm_card...
# from.models import UsuariosTarjetas
# from.serializers import UsuariosTarjetasSerializer



# funció per fer proves
@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)


# funció que varifica les dades de la tarjeta de pagament
@api_view(['POST'])
def confirm_credit_card(request):
    if not request.data or not 'id_tarjeta' in request.data or not 'CVC' in request.data:
        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        tarjeta = UsuariosTarjetas.objects.get(id_tarjeta=request.data['id_tarjeta'])
    except UsuariosTarjetas.DoesNotExist:
        return Response({"error": "Credit card not found"}, status=status.HTTP_404_NOT_FOUND)

    if tarjeta.CVC!= request.data['CVC']:
        return Response({"error": "Invalid CVC"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({"message": "Credit card details confirmed successfully"}, status=status.HTTP_200_OK)
