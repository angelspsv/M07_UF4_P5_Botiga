from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_list, name='carrito-list'),  # Ruta para la lista y creación
    path('<int:id>/', views.carrito_detail, name='carrito-detail'),  # Manejo de detalle
]
