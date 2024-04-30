from django.urls import path
from . import views


# conjunto de rutas URL con el nombre de las rutas, las vistas...
urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('confirm_credit_card/', views.confirm_credit_card, name='confirm_credit_card'),
]