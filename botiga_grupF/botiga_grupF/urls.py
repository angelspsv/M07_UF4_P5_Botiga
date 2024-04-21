from django.contrib import admin
from django.urls import path, include
from usuarios.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')), 
    path('dashboard/', dashboard_view, name='dashboard'),
]
