from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('modify/', views.modify_view, name='modify'),
    path('logout/', auth_views.LogoutView.as_view(next_page='usuarios:login'), name='logout'),

]
