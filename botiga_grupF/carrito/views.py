from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carrito
from .serializers import CarritoSerializer
from django.http import Http404

# Maneja la lista y creación de carritos
@api_view(['GET', 'POST'])
def carrito_list(request):
    if request.method == 'GET':
        carrito = Carrito.objects.all()
        serializer = CarritoSerializer(carrito, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Vista para detalle, actualización y eliminación del carrito
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def carrito_detail(request, id):
    try:
        carrito = Carrito.objects.get(id=id)
    except Carrito.DoesNotExist:
        raise Http404("Carrito no encontrado")

    if request.method == 'GET':
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarritoSerializer(carrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = CarritoSerializer(carrito, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)