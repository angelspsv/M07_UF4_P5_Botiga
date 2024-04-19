from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world_view(request):
    message = "Hello, world!"
    return Response({"message": message}, status=status.HTTP_200_OK)