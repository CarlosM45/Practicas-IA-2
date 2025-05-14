# Perceptron multicapa
# Importar las bibliotecas necesarias
import tensorflow as tf # TensorFlow es una biblioteca de código abierto para computación numérica y aprendizaje automático.
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos
from tensorflow.keras.models import Sequential # Importar la clase Sequential de Keras, que permite construir modelos de redes neuronales de forma secuencial
from tensorflow.keras.layers import Flatten # Importar la clase Flatten de Keras, que aplana la entrada
from tensorflow.keras.layers import Dense # Importar la clase Dense de Keras, que representa una capa densa (totalmente conectada) en la red neuronal
from tensorflow.keras.layers import Activation # Importar la clase Activation de Keras, que aplica una función de activación a la salida
import matplotlib.pyplot as plt # Matplotlib es una biblioteca de Python para crear gráficos y visualizaciones

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() # Cargar el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano
# x_train es la matriz de características de entrenamiento
# y_train es la matriz de etiquetas de entrenamiento

# Proyectar los datos de entrada a un rango de 0 a 1
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32') 

# Normalizar los datos dividiendo por el valor máximo de píxel (255)
gray_scale = 255
x_train /= gray_scale
x_test /= gray_scale

print("Feature matrix:", x_train.shape) # Imprime la forma de la matriz de características de entrenamiento 
print("Target matrix:", x_test.shape) # Imprime la forma de la matriz de características de prueba
print("Feature matrix:", y_train.shape) # Imprime la forma de la matriz de etiquetas de entrenamiento
print("Target matrix:", y_test.shape) # Imprime la forma de la matriz de etiquetas de prueba


fig, ax = plt.subplots(10, 10) 
k = 0
# Visualizar las primeras 100 imágenes del conjunto de entrenamiento
# Se crea una cuadrícula de 10x10 subgráficas
for i in range(10): 
    for j in range(10): 
        ax[i][j].imshow(x_train[k].reshape(28, 28),  
                        aspect='auto') 
        k += 1
plt.show() 

model = Sequential([ 
    
    # Aplanar la entrada de 28x28 a 784 (2D a 1D)
    Flatten(input_shape=(28, 28)), 
    
    # Capa densa 1
    Dense(256, activation='sigmoid'), # 256 neuronas y función de activación sigmoide
    
    # Capa densa 2 
    Dense(128, activation='sigmoid'), # 128 neuronas y función de activación sigmoide
    
    # Capa de salida 
    Dense(10, activation='sigmoid'), # 10 neuronas (una para cada dígito del 0 al 9)
]) 

model.compile(optimizer='adam', # Adam es un optimizador que utiliza el algoritmo de descenso de gradiente estocástico
            loss='sparse_categorical_crossentropy', # Función de pérdida para clasificación multiclase
            metrics=['accuracy']) # Métrica de evaluación del modelo

# Entrenar el modelo
model.fit(x_train, y_train, epochs=10, # Número de épocas (iteraciones sobre el conjunto de datos)
        batch_size=2000, # Tamaño del lote de 2000 muestras
        validation_split=0.2) # Dividir el conjunto de datos en entrenamiento y validación

# Evaluar el modelo en el conjunto de prueba
results = model.evaluate(x_test,  y_test, verbose = 0) # verbose=0 significa que no se mostrará información durante la evaluación
# Imprimir los resultados de la evaluación
print('test loss, test acc:', results)