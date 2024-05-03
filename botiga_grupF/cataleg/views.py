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


# funcionalidad crear producto
@api_view(['GET','POST'])
def create_product(request):
    if request.method == 'POST':
        # validamos request
        if not request.data or not 'nombre' in request.data or not 'precio' in request.data:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

        # crear objeto para bbdd
        catalogo = Catalogo.objects.create(
            id_producto=request.data['id_producto'],
            nombre=request.data['nombre'],
            descripcion=request.data.get('descripcion', ''),
            precio=request.data['precio'],
            stock=request.data.get('stock', 0),
            peso=request.data.get('peso', 0)
        )

        # enviar datos bbdd usando serializer
        serializer = ProductoSerializer(catalogo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        # muestra todos los productos de la bbdd
        catalogo = Catalogo.objects.all()

        # usando serializer para ver los productos de la query a json
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