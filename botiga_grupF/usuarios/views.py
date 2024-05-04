from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuarios
from .serializers import UsuariosSerializer
from django.http import Http404

# Maneja la lista y creación de usuarios
@api_view(['GET', 'POST'])
def usuarios_list(request):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Maneja el detalle, actualización y eliminación de usuarios
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def usuarios_detail(request, pk):
    try:
        usuario = Usuarios.objects.get(pk=pk)
    except Usuarios.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = UsuariosSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = UsuariosSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
