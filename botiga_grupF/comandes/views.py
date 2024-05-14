from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from carrito.models import Carrito
from .serializers import ComandaSerializer
from django.http import Http404

# Vista para detalle de la comanda y su lista de productos finalizados
@api_view(['GET'])
def comanda_result(request, id_carrito): 
    try:
        carritos = Carrito.objects.filter(id_carrito=id_carrito, finalizado=True)
        if not carritos.exists():
            raise Http404("Carrito no encontrado")
    except Carrito.DoesNotExist:
        raise Http404("Carrito no encontrado")

    if request.method == 'GET':
        serializer = ComandaSerializer(carritos, many=True)  
        return Response(serializer.data)
