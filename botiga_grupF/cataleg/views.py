from decimal import Decimal

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Catalogo
from .serializers import ProductoSerializer



# de prueba
@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)


# Llista tots els productes o crea un de nou.
# amb GET: retorna una llista amb tots els productes.
# amb POST: crea un nou producte.

@api_view(['GET', 'POST'])
def create_product(request):

    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        catalogo = Catalogo.objects.all()
        serializer = ProductoSerializer(catalogo, many=True)
        return Response(serializer.data)



# funcionalidad eliminar producto
@api_view(['DELETE'])
def delete_product(request, pk):

    product = Catalogo.objects.get(pk=pk)
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# funcionalidad actualizar producto
@api_view(['UPDATE'])
def update_product(request, pk):
    if not request.data or not 'nombre' in request.data or not 'precio' in request.data:
        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

    product = Catalogo.objects.get(pk=pk)
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.nombre = request.data['nombre']
    product.descripcion = request.data.get('descripcion', product.descripcion)
    product.id_seccion = request.data.get('id_seccion', product.id_seccion)
    product.precio = request.data['precio']
    product.stock = request.data.get('stock', product.stock)
    product.peso = request.data.get('peso', product.peso)
    product.save()

    serializer = ProductoSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)