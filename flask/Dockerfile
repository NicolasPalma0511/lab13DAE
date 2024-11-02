# Utiliza una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia y instala dependencias de Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copia el código de la aplicación y el archivo .env
COPY app.py /app/app.py
COPY .env /app/.env

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
