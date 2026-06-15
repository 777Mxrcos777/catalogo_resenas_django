from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    ROLES = [
        ('user', 'Usuario'),
        ('admin', 'Administrador'),
    ]
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=ROLES, default='user')
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} ({self.email})"

    class Meta:
        verbose_name_plural = "Usuarios"