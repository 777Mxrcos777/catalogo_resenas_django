from django.contrib import admin
from .models import (
    Categoria, Producto, Usuario, Resena, 
    Cliente, Venta, DetalleVenta, Reporte
)

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Resena)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Reporte)
