from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('modules.usuarios.urls'))

]
