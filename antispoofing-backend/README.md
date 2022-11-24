## Setup

- Para levantar el proyecto. Primero, build las imagenes:

```
docker-compose build
```

- Levantar los contenedores:

```
docker-compose up -d
```

- Correr migraciones

```
docker-compose exec web python manage.py migrate --noinput
```

- Collect archivos estaticos

```
docker-compose exec web python manage.py collectstatic --no-input --clear
```