from django.urls import path
from . import views

# rutes URL de l'aplicació Cataleg amb el seu nom
# per crear, modificar o esborrar producte o seccio
urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),
    path('products_cat/', views.products_cat, name='products_cat'),
    path('create_section/', views.create_section, name='create_section'),
    path('delete_section/<str:pk>/', views.delete_section, name='delete_section'),
    path('update_section/<str:pk>/', views.update_section, name='update_section'),
]
