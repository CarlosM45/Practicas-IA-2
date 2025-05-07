# Funcion de activacion
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Cargar el dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo secuencial
model = Sequential([
    Dense(10, activation='relu', input_shape=(4,)),  # Capa oculta con ReLU
    Dense(3, activation='softmax')                   # Capa de salida con Softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar la red neuronal
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")
