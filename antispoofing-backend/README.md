## Setup

- Para levantar el proyecto. Primero, build las imagenes:

```
docker-compose build
```

- Levantar los contenedores:

```
docker-compose up -d
```

### Backend

- Correr migraciones

```
docker-compose exec web python manage.py migrate --noinput
```

- Collect archivos estaticos

```
docker-compose exec web python manage.py collectstatic --no-input --clear
```

### Kafka

- Para crear los topics:

```
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic loginattempt
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic filtered
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic checked
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic celery
```
