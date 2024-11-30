# Backend de NutriRec

El backend de NutriRec es la base de una plataforma diseñada para la gestión de usuarios, ingredientes, recetas y preferencias alimentarias, ofreciendo funcionalidades como recomendaciones personalizadas y guardado de recetas favoritas. Este proyecto está desarrollado con Django y Django REST Framework.

## Tecnologías Utilizadas

- **Django**: Framework de Python para desarrollo web.
- **Django REST Framework**: Herramienta para construir APIs robustas con Django.
- **PostgreSQL**: Base de datos relacional.
- **JWT**: Autenticación basada en JSON Web Tokens con `djangorestframework-simplejwt`.
- **CORS**: Middleware para manejar CORS con `django-cors-headers`.
- **Gunicorn**: Servidor HTTP para despliegue en producción.

## Endpoints Principales

### Autenticación
- **POST** `/api/auth/register/`: Registrar un nuevo usuario.
- **POST** `/api/auth/login/`: Iniciar sesión.
- **GET** `/api/auth/user/`: Ver información del usuario autenticado.

### Usuarios
- **GET** `/api/auth/user/`: Consultar información del usuario.
- **PUT** `/api/auth/user/`: Actualizar información del usuario.

### Ingredientes
- **GET** `/api/ingredientes/`: Listar todos los ingredientes disponibles.

### Recetas
- **GET** `/api/recetas/`: Consultar todas las recetas.
- **GET** `/api/recetas/{id}/`: Ver detalles de una receta específica.
- **POST** `/api/recetas/recomendaciones/`: Generar recomendaciones basadas en ingredientes seleccionados.

### Recetas Guardadas
- **POST** `/api/recetas-guardadas/`: Guardar una receta.
- **GET** `/api/recetas-guardadas/`: Listar recetas guardadas del usuario.
- **GET** `/api/recetas-guardadas/mas-guardadas/`: Consultar recetas más guardadas en un rango de fechas.

## Configuración de Base de Datos

La aplicación utiliza PostgreSQL como base de datos, configurada en el archivo `settings.py` de Django. Ejemplo de configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nutrirec_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Estructura de Carpetas

- **nutri_backend**: Configuración global de Django, incluye `settings.py`, `urls.py` y `wsgi.py`.
- **apps**:
  - **usuarios**: Gestión de usuarios y autenticación.
  - **ingredientes**: CRUD de ingredientes.
  - **recetas**: Gestión de recetas y recomendaciones.
  - **recetas_guardadas**: Sistema para guardar recetas favoritas.
  - **preferencias**: Gestión de preferencias alimentarias.

---

# Características Principales

- **Autenticación JWT**: Seguridad en las sesiones de usuario.
- **Recomendaciones Personalizadas**: Basadas en ingredientes seleccionados.
- **Gestión de Preferencias**: Filtrado de recetas según preferencias alimentarias.
- **Recetas Favoritas**: Guardado de recetas y consulta de las más populares.

---

# Despliegue

El despliegue del backend se realiza configurando las variables de entorno, utilizando **Gunicorn** como servidor de aplicaciones, y configurando un servidor web como **Nginx** para servir la aplicación en producción junto con una base de datos **PostgreSQL**.
