from django.contrib import admin
from django.urls import path, include


# rutes url del projecte/aplicació Cataleg
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cataleg/', include('cataleg.urls')),
    path('usuarios/', include('usuarios.urls')), 
    path('carrito/', include('carrito.urls')),
    path('comanda/', include('comandes.urls')),
    path('pagaments/', include('pagaments.urls')),

]