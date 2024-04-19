from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
]
