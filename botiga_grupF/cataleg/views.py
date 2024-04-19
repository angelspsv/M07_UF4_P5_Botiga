from decimal import Decimal

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Catalogo
from .serializers import ProductoSerializer


@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):

    # validamos request
    if not request.data or not 'nombre' in request.data or not 'precio' in request.data:
        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

    # crear objeto para bbdd
    catalogo = Catalogo.objects.create(
        nombre=request.data['nombre'],
        descripcion=request.data.get('descripcion', ''),
        id_seccion=request.data.get('id_seccion', 0),
        precio=request.data['precio'],
        stock=request.data.get('stock', 0),
        peso=request.data.get('peso', 0)
    )

    # enviar datos bbdd usando serializer
    serializer = ProductoSerializer(catalogo)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_product(request, pk):

    product = Catalogo.objects.get(pk=pk)
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

