from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen_url = models.URLField(max_length=500, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def promedio_calificaciones(self):
        from apps.resenas.models import Resena
        from django.db.models import Avg
        resenas_aprobadas = Resena.objects.filter(id_producto=self, estado='aprobada')
        if resenas_aprobadas.exists():
            return round(resenas_aprobadas.aggregate(Avg('calificacion'))['calificacion__avg'], 2)
        return 0

    class Meta:
        verbose_name_plural = "Productos"