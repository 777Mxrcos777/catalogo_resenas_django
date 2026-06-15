from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    return render(request, 'home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.promedio_calificaciones = producto.promedio_calificaciones()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.promedio_calificaciones = producto.promedio_calificaciones()
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def ranking(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.promedio = producto.promedio_calificaciones()
    productos_top = sorted(productos, key=lambda p: p.promedio, reverse=True)[:5]
    return render(request, 'ranking.html', {'productos_top': productos_top})