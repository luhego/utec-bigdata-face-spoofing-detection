## Kakfa Service

Para levantar los contenedores de Docker, usar el siguiente comand:

```
docker-compose up -d
```

Para crear los topics:

```
docker exec kafka1 kafka-topics --bootstrap-server kafka1:9092 --create --topic loginattempt
docker exec kafka1 kafka-topics --bootstrap-server kafka1:9092 --create --topic filtered
docker exec kafka1 kafka-topics --bootstrap-server kafka1:9092 --create --topic checked
docker exec kafka1 kafka-topics --bootstrap-server kafka1:9092 --create --topic celery
```
