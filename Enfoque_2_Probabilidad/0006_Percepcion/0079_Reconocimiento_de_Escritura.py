# Reconocimient de dígitos escritos a mano con OpenCV
import cv2 # OpenCV es una biblioteca de visión por computadora
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos
from keras.datasets import mnist # MNIST es un conjunto de datos de dígitos escritos a mano
from keras.models import Sequential # Sequential es un modelo de Keras para construir redes neuronales
from keras.layers import Dense, Flatten # Dense y Flatten son capas de Keras
from keras.utils import to_categorical # to_categorical es una función de Keras para convertir etiquetas a formato one-hot

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar las imágenes
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Redimensionar las imágenes para que tengan un canal adicional (grayscale)
train_images = np.expand_dims(train_images, axis=-1)
test_images = np.expand_dims(test_images, axis=-1)

# Codificar las etiquetas a formato one-hot
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Construir el modelo
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))