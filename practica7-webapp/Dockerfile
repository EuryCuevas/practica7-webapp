# Imagen base con Python ya instalado
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Primero se copian y se instalan las dependencias.
# Se hace por separado para que Docker reutilice esta capa en caché
# cuando solo cambie el código y no las librerías.
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Después se copia el código de la aplicación
COPY src/ .

EXPOSE 5000

# host=0.0.0.0 es obligatorio: sin eso Flask solo escucha dentro del contenedor
# y no se puede acceder desde el navegador del PC
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]