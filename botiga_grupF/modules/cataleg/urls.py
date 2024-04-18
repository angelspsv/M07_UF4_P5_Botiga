from django.urls import path
from botiga_grupF.modules.cataleg import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]
