# Usar una imagen oficial de Python como imagen padre
FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el archivo de requisitos y instalar las dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
