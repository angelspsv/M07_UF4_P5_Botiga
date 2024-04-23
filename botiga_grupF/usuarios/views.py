from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import logging
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Declarar el logger al nivel del módulo para uso en todas las vistas
logger = logging.getLogger(__name__)

# Vista para el dashboard del usuario que requiere autenticación
@login_required
def dashboard_view(request):
    context = {'user': request.user}
    return render(request, 'user_dashboard.html', context)

# Vista para registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UsuarioForm()
    return render(request, 'register.html', {'form': form, 'is_register': True})

# Vista para inicio de sesión
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('password')

        logger.debug("Correo electrónico: %s, Contraseña: %s", email, contrasena)

        user = authenticate(request, username=email, password=contrasena)

        if user:
            login(request, user)
            logger.info("Inicio de sesión exitoso para: %s", email)
            return redirect('dashboard')
        else:
            logger.warning("Autenticación fallida para el usuario: %s", email)
            context = {'error': 'Credenciales incorrectas'}
            return render(request, 'login.html', context)

    return render(request, 'login.html',  {'is_login': True})

# Vista para modificar i eliminar usuario
@login_required
def modify_view(request):
    user = request.user

    if request.method == 'POST':
        if 'confirm' in request.POST and request.POST['confirm'] == 'yes':
            user_email = user.email 
            logout(request)
            user.delete()
            logger.info("Usuario eliminado: %s", user_email)
            messages.success(request, "Tu cuenta ha sido eliminada con éxito.")
            return redirect('usuarios:login')

        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save() 
            login(request, user) 
            messages.success(request, "Información actualizada con éxito.")
            return redirect('dashboard')
        else:
            messages.error(request, "Error al actualizar la información.")
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'modify_user.html', {'form': form, 'is_modify_view': True})