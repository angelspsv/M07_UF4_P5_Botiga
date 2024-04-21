from django import forms
from .models import Usuarios
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')  # Campo de contraseña seguro
    
    class Meta:
        model = Usuarios
        fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'email', 'password']
    
    # Sobrescribir el método save para encriptar la contraseña antes de guardar el usuario
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Encriptar contraseña
        if commit:
            user.save()
        return user
