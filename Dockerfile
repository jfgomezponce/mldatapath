# Usa una imagen base de Python
FROM python:3.9.13

# Copia el modelo y el script a la imagen
COPY ./src /src
# Establece el directorio de trabajo en /app
WORKDIR /src

#Permiso para ejecutar el archivo main
RUN chmod +x /src/main.py 

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
