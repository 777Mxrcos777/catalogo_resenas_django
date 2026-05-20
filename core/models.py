from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name_plural = "Productos"

    def promedio_calificaciones(self):
        resenas_aprobadas = self.resena_set.filter(estado='aprobada')
        if resenas_aprobadas.exists():
            return round(resenas_aprobadas.aggregate(models.Avg('calificacion'))['calificacion__avg'], 2)
        return 0


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


class Resena(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    id_resena = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenas')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='resenas')
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reseña de {self.id_usuario.nombre} a {self.id_producto.nombre} - {self.calificacion}★"

    class Meta:
        verbose_name_plural = "Reseñas"
        unique_together = ['id_producto', 'id_usuario']


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
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    id_usuario_vendedor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='ventas_registradas')
    fecha_venta = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activa')

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.id_cliente.nombre}"

    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles_venta')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Detalle: {self.cantidad}x {self.id_producto.nombre}"

    class Meta:
        verbose_name_plural = "Detalles de Venta"


class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_usuario_generador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='reportes')
    tipo_reporte = models.CharField(max_length=100)
    fecha_generacion = models.DateTimeField(default=timezone.now)
    datos_resumen = models.TextField(blank=True, null=True)
    archivo_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_reporte} - {self.fecha_generacion}"

    class Meta:
        verbose_name_plural = "Reportes"