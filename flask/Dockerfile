# Utiliza una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema y el controlador ODBC de SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    unixodbc-dev

# Agrega la clave pública del repositorio de Microsoft e instala el controlador ODBC
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copia y instala dependencias de Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copia el código de la aplicación
COPY app.py /app/app.py

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
