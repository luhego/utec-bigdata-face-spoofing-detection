# UTEC - Big Data  - Proyecto Final

## Instrucciones

### Pre-requisitos

Debe tener instalado Docker y Docker Compose.

Para poder correr el proyecto, se necesita obtener la credenciales de un AWS IAM user valido. Por razones de seguridad y dado que para el proyecto se utilizaron las credenciales de una cuenta personal, no se han incluido en el proyecto y necesitan ser configuradas de manera manual. Las instrucciones para configurar las variables de entorno en cada carpeta se incluyen a continuación:

- antispoofing-frontend

Crear un archivo `.env` en la siguiente ruta: `utec-bigdata-face-spoofing-detection/antispoofing-frontend/` con el siguiente contenido:

```
REACT_APP_AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
REACT_APP_AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESSS_KEY>
REACT_APP_AWS_STORAGE_BUCKET_NAME=<YOUR_AWS_S3_BUCKET_NAME>
REACT_APP_AWS_S3_REGION_NAME=<YOUR_AWS_S3_REGION>
```

- antispoofing-backend/

Crear un archivo `.env` en la siguiente ruta: `utec-bigdata-face-spoofing-detection/antispoofing-backend/` con el siguiente contenido:

```
DEBUG=1
SECRET_KEY=YOUR_SECRET_KEY
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_ENGINE=django.db.backends.postgresql
DB_NAME=antispoofing
DB_USER=backend
DB_PASSWORD=backend
DB_HOST=db
DB_PORT=5432
DATABASE=
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESSS_KEY>
AWS_STORAGE_BUCKET_NAME=<YOUR_AWS_S3_BUCKET_NAME>
AWS_S3_REGION_NAME=<YOUR_AWS_S3_REGION>
```

- antispoofing-backend/auth-service
Crear un archivo `.env` en la siguiente ruta: `utec-bigdata-face-spoofing-detection/antispoofing-backend/auth-service/utils/` con el siguiente contenido:

```
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESSS_KEY>
AWS_STORAGE_BUCKET_NAME=<YOUR_AWS_S3_BUCKET_NAME>
AWS_S3_REGION_NAME=<YOUR_AWS_S3_REGION>
```

- antispoofing-backend/streaming-fake-detector

Crear un archivo `.env` en la siguiente ruta: `utec-bigdata-face-spoofing-detection/antispoofing-backend/streaming-fake-detector/utils/` con el siguiente contenido:

```
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESSS_KEY>
AWS_STORAGE_BUCKET_NAME=<YOUR_AWS_S3_BUCKET_NAME>
AWS_S3_REGION_NAME=<YOUR_AWS_S3_REGION>
```

### Levantar y correr el backend
- Ubicarse en la carpeta `utec-bigdata-face-spoofing-detection/antispoofing-backend`.

- Construir las imagenes con Docker Compose:

```
docker-compose build
```

- Levantar los contenedores:

```
docker-compose up -d
```

- Revisar los logs:

```
docker-compose logs -f
```

- Abrir otra tab en el terminal y crear crear los topics:

```
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic loginattempt
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic filtered
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic checked
docker exec kafka1 kafka-topics --bootstrap-server kafka1:19092 --create --topic celery
```

- Verificar que los contenedores esten corriendo:

```
docker ps
```

### Levantar y correr el frontend

- Ubicarse en la carpeta `utec-bigdata-face-spoofing-detection/antispoofing-frontend`.

- Instalar las dependencias:

```
npm install
```

- Correr el proyecto

```
npm start
```

- Listo, la demo correrá en http://localhost:3000