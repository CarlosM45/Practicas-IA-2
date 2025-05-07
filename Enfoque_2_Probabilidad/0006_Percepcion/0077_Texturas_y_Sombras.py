# Texturas y Sombras
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("zenless.png")

# Convertir la imagen a espacio de color HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir los límites para la detección de sombras en el canal V
lower_shadow = np.array([0, 0, 0])
upper_shadow = np.array([180, 255, 50])

# Crear una máscara para detectar sombras
mask = cv2.inRange(hsv_image, lower_shadow, upper_shadow)

# Mostrar la imagen original y la máscara de sombras
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Máscara de Sombras')
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.show()