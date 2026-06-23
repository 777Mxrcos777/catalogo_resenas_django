from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from apps.resenas.forms import ResenaForm
from apps.resenas.models import Resena
from apps.usuarios.models import Usuario

def home(request):
    return render(request, 'home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    print(f"📦 Productos encontrados: {productos.count()}")  
    for producto in productos:
        producto.promedio_calificaciones = producto.promedio_calificaciones()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.promedio_calificaciones = producto.promedio_calificaciones()
    
    # Obtener reseñas aprobadas
    resenas = producto.resena_set.filter(estado='aprobada')
    
    return render(request, 'productos/detalle_producto.html', {
        'producto': producto,
        'resenas': resenas,
    })

def ranking(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.promedio = producto.promedio_calificaciones()
    productos_top = sorted(productos, key=lambda p: p.promedio, reverse=True)[:5]
    return render(request, 'ranking.html', {'productos_top': productos_top})

def crear_resena(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            usuario, created = Usuario.objects.get_or_create(
                email=email,
                defaults={'nombre': nombre, 'contrasena': 'temp123'}
            )
            resena = form.save(commit=False)
            resena.id_producto = producto
            resena.id_usuario = usuario
            resena.estado = 'aprobada'
            resena.save()
            return redirect('detalle_producto', pk=pk)
    else:
        form = ResenaForm()
    return render(request, 'productos/crear_resena.html', {'form': form, 'producto': producto})