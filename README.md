# Sistema de Catálogo y Reseñas

Proyecto Django para administrar un catálogo de productos y permitir a usuarios registrar reseñas con calificación.  
Incluye promedio por producto y ranking simple.

## Requisitos

- Python 3.12 o superior
- Django 5.2

## Instalación y ejecución

Sigue estos pasos en tu terminal:

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate      # En Windows
# source venv/bin/activate # En Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate

# 4. Crear superusuario (admin)
python manage.py createsuperuser

# 5. Ejecutar el servidor
python manage.py runserver
