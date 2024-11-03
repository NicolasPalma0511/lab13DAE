# Utiliza una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema, incluidos gnupg y el controlador ODBC de SQL Server
RUN apt-get update && apt-get install -y \
    gnupg \
    curl \
    apt-transport-https \
    unixodbc-dev

# Agrega la clave pública del repositorio de Microsoft e instala el controlador ODBC
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Listar controladores ODBC instalados
RUN odbcinst -q -d

# Crear un nuevo usuario y grupo
RUN useradd -m flaskuser

# Cambiar a este nuevo usuario
USER flaskuser

# Crear el directorio de trabajo
WORKDIR /app

# Copia y instala dependencias de Python
COPY requirements.txt /app/requirements.txt
RUN pip install --user -r requirements.txt

# Copia el código de la aplicación
COPY --chown=flaskuser:flaskuser app.py /app/app.py

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
