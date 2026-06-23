# 📚 Catálogo y Reseñas

Sistema web desarrollado en **Django 5.2** que permite administrar un catálogo de productos y gestionar reseñas con calificaciones. Los usuarios pueden explorar productos, ver su puntuación promedio, escribir reseñas y consultar el ranking de los mejor valorados.

---

## 🚀 Tecnologías utilizadas

- **Python 3.13**
- **Django 5.2**
- **SQLite** (base de datos por defecto)
- **CSS personalizado** (sin framework externo)
- **HTML5 + JavaScript** (búsqueda en tiempo real)

## 📦 Instalación y ejecución

Sigue estos pasos para levantar el proyecto en tu computadora:

### 1️⃣ Clonar el repositorio

git clone https://github.com/777Mxrcos777/catalogo_resenas_django.git
cd catalogo_resenas_django

2️⃣ Crear y activar entorno virtual

python -m venv venv
venv\Scripts\actívate

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Aplicar migraciones

python manage.py migrate

5️⃣ Crear superusuario (admin)

python manage.py createsuperuser

6️⃣ Ejecutar el servidor

python manage.py runserver

🔐 Acceso al panel de administración
Usuario: admin

Contraseña: 1234
