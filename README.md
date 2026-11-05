# Fundación Patrimonio Vivo

Aplicación web desarrollada con Python y Django para la visualización y administración de un catálogo digital de lugares patrimoniales.

Los visitantes pueden explorar los lugares registrados, consultar sus detalles y filtrar el catálogo por categorías. Los usuarios autenticados pueden acceder al área de administración, cuyas operaciones están restringidas según sus permisos.

## 1. Requisitos previos

Antes de ejecutar el proyecto, verificar que Python 3 esté instalado:

```cmd
python --version
```

Verificar que PIP esté instalado:

```cmd
py -m pip --version
```

Actualizar PIP:

```cmd
py -m pip install --upgrade pip
```

## 2. Descargar el proyecto

Clonar el repositorio desde GitHub:

```cmd
git clone [URL_DEL_REPOSITORIO](https://github.com/fsalgado-143/CER2-SALGADOFLORENCIA/tree/main)
```

Ingresar al directorio del proyecto:

```cmd
cd CER2-SALGADOFLORENCIA
```

También es posible descargar el proyecto desde GitHub como archivo ZIP y descomprimirlo.

## 3. Instalar Django y las dependencias

Instalar las dependencias necesarias:

```cmd
py -m pip install -r requirements.txt
```

Este archivo contiene Django y las demás librerías utilizadas por el proyecto.

Verificar la instalación de Django:

```cmd
py -m django --version
```

## 4. Configurar la base de datos

La configuración de la base de datos se encuentra en `settings.py`, dentro de la variable `DATABASES`.

Ejecutar las migraciones para preparar la base de datos:

```cmd
py manage.py migrate
```

Para crear un usuario administrador, ejecutar:

```cmd
py manage.py createsuperuser
```

## 5. Iniciar el servidor

Desde la terminal de Visual Studio Code, ubicarse en el directorio donde se encuentra `manage.py` y ejecutar:

```cmd
py manage.py runserver
```

El servidor de desarrollo estará disponible en:

http://127.0.0.1:8000/

Para acceder al panel de administración de Django:

http://127.0.0.1:8000/admin/

## 6. Funcionalidades principales

- Página de inicio con carrusel de imágenes.
- Catálogo dinámico de lugares patrimoniales.
- Visualización del detalle de cada lugar.
- Clasificación y filtrado por categorías.
- Inicio y cierre de sesión.
- Panel de administración personalizado.
- Creación, modificación y eliminación de lugares según los permisos del usuario.
- Administración de categorías y lugares mediante Django Admin.

## 7. Tecnologías utilizadas

- Python 3
- Django
- HTML
- CSS
- Bootstrap
- Base de datos configurada en Django.
