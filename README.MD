# Iniciar el Proyecto

Este proyecto es una api en python con djangorestframework usando una base de datos en postgres en contenedores independientes

## Requisitos

- Python
- Docker y Docker Compose (Docker Desktop)

## Configuracion Del Proyecto

### Clonar Repositorio

Primero clonaremos el repositorio del proyecto

```sh
git clone https://github.com/jhonatanp21b/proyecto-u-docker.git proyecto-u
cd proyecto-u
```

### Ejecutar con Docker

1. Asegúrate de que Docker y Docker Compose estén instalados y en funcionamiento.

2. Construye los contenedores de Docker:

   ```sh
   docker-compose build
   ```

3. Inicia los contenedores de Docker:

   ```sh
   docker-compose up
   ```

4. Aplica las migraciones y crea un superusuario:

   ```sh
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

5. La aplicación debería estar disponible en `http://localhost:8000` en esta ruta inicial no veremos nada ya que debemos probar los endpoints reales por ejemplo `http://localhost:8000/api/v1/categories/`.

6. Pueden abrir el archivo proyecto-u.postman_collection en postman para probar e insertar nuevos elementos
