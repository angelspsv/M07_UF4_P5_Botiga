from decimal import Decimal

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Catalogo, CatalogoSecciones
from .serializers import ProductoSerializer, CatalogoSeccionesSerializer


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
    #POST, para crear nuevo producto,
    # los datos se validan y guardan usando serializador
    # si tot es correcto respuesta 201 created
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    #GET, recupera todos los productos del catalogo y
    # se serializan para devolver una respuesta en forma de lista de productos
    elif request.method == 'GET':
        catalogo = Catalogo.objects.all()
        serializer = ProductoSerializer(catalogo, many=True)
        return Response(serializer.data)


# funcio que mostra tots els productes del cataleg sense anar-hi a create_product
@api_view(['GET'])
def products_cat(request):
    if request.method == 'GET':
        catalogo = Catalogo.objects.all()
        serializer = ProductoSerializer(catalogo, many=True)
        return Response(serializer.data)


# funcionalidad eliminar producto funciona por el id del producto
@api_view(['DELETE', 'GET'])
def delete_product(request, pk):
    # intenta recuperar el producto del catalogo por su id/pk, si no existe error 404
    try:
        product = Catalogo.objects.get(pk=pk)
    except Catalogo.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    # GET permite ver el producto a eliminar
    if request.method == 'GET':
        serializer = ProductoSerializer(product)
        return Response(serializer.data)

    # DELETE, elimina el producto y devuelve un mensaje de exito
    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": f"Product with ID {pk} deleted successfully"})


# funcionalidad eliminar seccion de producto. funciona por el id de la seccion
@api_view(['DELETE', 'GET'])
def delete_section(request, pk):
    # intenta recuperar la seccion por su id/pk
    try:
        section = CatalogoSecciones.objects.get(pk=pk)
    except CatalogoSecciones.DoesNotExist:
        return Response({"error": "Section not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CatalogoSeccionesSerializer(section)
        return Response(serializer.data)

    # DELETE, elimina el seccion y devuelve un mensaje de exito
    elif request.method == 'DELETE':
        section.delete()
        return Response({"message": f"Section with ID {pk} deleted successfully"})



# funcionalidad actualizar producto
# con GET primero recupero desde la bbdd el elemento con pk indicada en la url
# despues con PATCH o PUT actualizo datos del producto
# vuelvo a mostrar el producto actualizado

@api_view(['GET', 'PUT', 'PATCH'])
def update_product(request, pk):
    # GET, recupera el producto del catalogo por su ID y devuelve sus detalles
    if request.method == 'GET':
        product = Catalogo.objects.get(pk=pk)
        serializer = ProductoSerializer(product)
        return Response(serializer.data)

    #si fallan estos campos retorna mensaje de error codigo 400 (solicitud incorrecta)
    elif request.method == 'PUT' or request.method == 'PATCH':
        if not request.data or not 'nombre' in request.data or not 'precio' in request.data:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

        # comprueba si el producto existe
        product = Catalogo.objects.get(pk=pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        if 'id_seccion' in request.data:
            seccion = CatalogoSecciones.objects.get(pk=request.data['id_seccion'])
            product.id_seccion = seccion

        #PUT o PATCH, valida y actualiza los datos del producto
        product.nombre = request.data['nombre']
        product.descripcion = request.data.get('descripcion', product.descripcion)
        product.precio = request.data['precio']
        product.stock = request.data.get('stock', product.stock)
        product.peso = request.data.get('peso', product.peso)
        product.save()

        serializer = ProductoSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


# la funcion update_section actualiza las secciones ya existentes
@api_view(['GET', 'PUT', 'PATCH'])
def update_section(request, pk):
    if request.method == 'GET':
        section = CatalogoSecciones.objects.get(pk=pk)
        serializer = CatalogoSeccionesSerializer(section)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        if not request.data or not 'id_seccion' in request.data:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

        section = CatalogoSecciones.objects.get(pk=pk)
        if section is None:
            return Response({"error": "Section not found"}, status=status.HTTP_404_NOT_FOUND)

        section.id_seccion = request.data['id_seccion']
        section.nombre = request.data['nombre']
        section.save()

        serializer = CatalogoSeccionesSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)




#funcio per crear seccions per poder clasificar els productes (taula CatalogoSecciones)
@api_view(['GET', 'POST'])
def create_section(request):
    # POST, creamos una seccion nueva, si tot es correcto se guerda
    # Si la validación es exitosa, devuelve la seccion creada y el codigo 201 (creado)
    if request.method == 'POST':
        serializer = CatalogoSeccionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET, recupera todas las secciones del catálogo y
    # las devuelve como una lista de datos serializados
    elif request.method == 'GET':
        catalogosecciones = CatalogoSecciones.objects.all()
        serializer = CatalogoSeccionesSerializer(catalogosecciones, many=True)
        return Response(serializer.data)