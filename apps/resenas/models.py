from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Resena(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    id_resena = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reseña de {self.id_usuario.nombre} - {self.calificacion}★"

    class Meta:
        verbose_name_plural = "Reseñas"