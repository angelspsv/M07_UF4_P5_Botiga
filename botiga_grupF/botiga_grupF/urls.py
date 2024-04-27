from django.contrib import admin
from django.urls import path, include
from usuarios.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(router.urls)),
]
