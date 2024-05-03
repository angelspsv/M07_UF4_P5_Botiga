from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios_list, name='usuarios-list'),          # Ruta para la lista y creación
    path('<int:pk>/', views.usuarios_detail, name='usuarios-detail'),  # Ruta para detalle, actualización y eliminación
]
