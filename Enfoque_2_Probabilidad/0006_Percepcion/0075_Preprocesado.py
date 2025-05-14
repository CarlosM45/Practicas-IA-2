# Preprocesado: Filtros - Filtro Gaussiano
import cv2 # OpenCV es una biblioteca de visión por computadora
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos
import matplotlib.pyplot as plt # Matplotlib es una biblioteca de Python para crear gráficos y visualizaciones

# Cargar la imagen
image = cv2.imread("msc.png")

# Convertir la imagen de BGR a RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Aplicar el filtro Gaussiano
# (imagen, (ancho, alto del kernel), desviación estándar)
filtered_image = cv2.GaussianBlur(image, (5, 5), 0)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen con Filtro Gaussiano')
plt.imshow(filtered_image)
plt.axis('off')

plt.show()