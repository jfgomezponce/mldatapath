# mldatapath Tarea 1

## Jose Gomez

En este README, se proporcionan instrucciones claras sobre cómo construir la imagen Docker, ejecutar el contenedor Docker y dónde encontrar el archivo python.

### Para construir la imagen se debe considerar dentro de la carpeta src/ los archivos model.pkl y normalizador.pkl (No fueron cargador debido a que se solicitó que el gitignore los discriminara), usar el siguiente comando:

```
docker build -t mletarea1 .
```

# Enviar los parametros a la imagen por variable de entorno ejemplo:

```
docker run -e values='-0.234571412,19.11042633,74.24222492' mletarea1
docker run -e values='1.547196967,61.71901588,3.662680136' mletarea1
```

[Archivo Jupyter Notebook](https://colab.research.google.com/drive/1N-iraB2fmvwtxRx70oA4CjFjJES4AVxQ?usp=sharing).
