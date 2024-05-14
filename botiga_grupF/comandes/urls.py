from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_carrito>/', views.comanda_result, name='comanda-result'),  # Manejo de detalle
]
