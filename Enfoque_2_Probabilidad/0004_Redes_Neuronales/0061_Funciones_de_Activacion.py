# Funcion de activacion
import tensorflow as tf # Importar TensorFlow
from tensorflow.keras.models import Sequential # Importar el modelo secuencial, que es una pila lineal de capas
from tensorflow.keras.layers import Dense # Importar la capa densa, que es una capa completamente conectada
from sklearn.datasets import load_iris # Importar el conjunto de datos Iris
from sklearn.model_selection import train_test_split # Importar la función train_test_split de sklearn.model_selection, que divide los datos en conjuntos de entrenamiento y prueba

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
model.compile(optimizer='adam', # Adam es un optimizador que utiliza el algoritmo de descenso de gradiente estocástico
              loss='sparse_categorical_crossentropy', # Función de pérdida para clasificación multiclase
                # sparse_categorical_crossentropy se utiliza cuando las etiquetas son enteros
              metrics=['accuracy']) # Métrica de evaluación del modelo

# Entrenar la red neuronal
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1) # epochs es el número de veces que el modelo verá todo el conjunto de datos
# batch_size es el número de muestras que se procesan antes de actualizar el modelo
# verbose=1 muestra el progreso del entrenamiento

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")
