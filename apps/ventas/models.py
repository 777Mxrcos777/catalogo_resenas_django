from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Clientes"


class Venta(models.Model):
    ESTADOS = [
        ('activa', 'Activa'),
        ('anulada', 'Anulada'),
        ('completada', 'Completada'),
    ]
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_usuario_vendedor = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True)
    fecha_venta = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activa')

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.id_cliente.nombre}"

    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Detalle: {self.cantidad}x {self.id_producto.nombre}"

    class Meta:
        verbose_name_plural = "Detalles de Venta"