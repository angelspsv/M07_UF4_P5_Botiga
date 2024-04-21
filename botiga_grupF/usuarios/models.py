from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom manager para el modelo de usuario
class UserManager(BaseUserManager):
    def create_user(self, email, nombre, primer_apellido, segundo_apellido, contrasena=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        if not contrasena:
            raise ValueError("El usuario debe tener una contraseña")

        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
        )
        user.set_password(contrasena)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, primer_apellido, segundo_apellido, contrasena):
        user = self.create_user(email, nombre, primer_apellido, segundo_apellido, contrasena)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Modelo de usuario personalizado
class Usuarios(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    primer_apellido = models.CharField(max_length=255, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_user_permissions',
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Usa el correo electrónico como nombre de usuario
    REQUIRED_FIELDS = ['nombre', 'primer_apellido', 'segundo_apellido']  # Campos requeridos para el superusuario

    def __str__(self):
        return f"{self.email}"
