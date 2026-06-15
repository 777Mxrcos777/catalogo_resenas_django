from django.contrib import admin
from django.urls import path, include
from apps.productos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('ranking/', views.ranking, name='ranking'),
    path('admin/', admin.site.urls),
]
