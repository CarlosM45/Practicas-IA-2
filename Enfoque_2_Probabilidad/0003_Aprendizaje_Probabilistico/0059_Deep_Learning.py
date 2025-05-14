# Aprendizaje Profundo
import tensorflow as tf # TensorFlow es una biblioteca de código abierto para computación numérica y aprendizaje automático.
from tensorflow.keras.models import Sequential # Importar la clase Sequential de Keras, que permite construir modelos de redes neuronales de forma secuencial
from tensorflow.keras.layers import Dense # Importar la clase Dense de Keras, que representa una capa densa (totalmente conectada) en la red neuronal

# Crear la red neuronal con 3 capas
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # Capa de entrada (4 neuronas)
    Dense(32, activation='relu'),                    # Capa oculta
    Dense(3, activation='softmax')                   # Capa de salida (3 clases)
])

# Compilar el modelo
model.compile(optimizer='adam', # Adam es un optimizador que utiliza el algoritmo de descenso de gradiente estocástico
              loss='sparse_categorical_crossentropy', # Función de pérdida para clasificación multiclase
              # sparse_categorical_crossentropy se utiliza cuando las etiquetas son enteros
              metrics=['accuracy']) # Métrica de evaluación del modelo

# Cargar el dataset Iris
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split # Importar la función train_test_split de sklearn.model_selection, que divide los datos en conjuntos de entrenamiento y prueba

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42) # Dividir el conjunto de datos en entrenamiento y prueba
# X_train es la matriz de características de entrenamiento

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1) # epochs es el número de veces que el modelo verá todo el conjunto de datos
# batch_size es el número de muestras que se procesan antes de actualizar el modelo
# verbose=1 muestra el progreso del entrenamiento

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")
