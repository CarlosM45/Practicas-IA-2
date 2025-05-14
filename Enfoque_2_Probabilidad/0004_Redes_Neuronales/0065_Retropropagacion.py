# Retropropagacion de error
import tensorflow as tf # TensorFlow es una biblioteca de código abierto para computación numérica y aprendizaje automático
from tensorflow.keras.models import Sequential # Importar la clase Sequential de Keras, que permite construir modelos de redes neuronales de forma secuencial
from tensorflow.keras.layers import Dense # Importar la clase Dense de Keras, que representa una capa densa (totalmente conectada) en la red neuronal

# Crear el modelo secuencial
model = Sequential()

# Añadir capas (3 neuronas en la capa de entrada, 5 en la oculta, y 1 en la salida)
model.add(Dense(5, input_dim=3, activation='relu'))  # Capa oculta
model.add(Dense(1, activation='sigmoid'))  # Capa de salida

# Compilar el modelo usando retropropagación (optimización con Adam)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Datos de ejemplo (3 características)
x = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
y = [0, 1, 1, 0]

# Entrenar el modelo (proceso de retropropagación)
model.fit(x, y, epochs=100, verbose=1)

# Evaluar el modelo
loss, accuracy = model.evaluate(x, y)
print(f"Pérdida: {loss}, Precisión: {accuracy * 100:.2f}%")
