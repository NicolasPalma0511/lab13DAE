# Utiliza una imagen base de Python
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unixodbc unixodbc-dev libodbc1 odbcinst apt-transport-https gnupg && \
    # Add the Microsoft repository key and list
    curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc && \
    curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    # Install the Microsoft ODBC Driver for SQL Server
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 && \
    rm -rf /var/lib/apt/lists/*

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
