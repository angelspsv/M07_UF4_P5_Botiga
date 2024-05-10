from django.urls import path
from . import views


# conjunto de rutas URL con el nombre de las rutas, las vistas...
urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('update_pago_carrito/', views.update_pago_carrito, name='update_pago_carrito'),
]