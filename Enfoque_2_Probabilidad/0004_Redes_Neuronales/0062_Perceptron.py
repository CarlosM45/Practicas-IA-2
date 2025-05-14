# Perceptron, ADALINE y MADALINE
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos
from sklearn.datasets import load_iris # Importar el conjunto de datos Iris, que es un conjunto de datos clásico con muestras de flores
from sklearn.model_selection import train_test_split # Importar la función train_test_split de sklearn.model_selection, que divide los datos en conjuntos de entrenamiento y prueba
from sklearn.linear_model import Perceptron # Importar el modelo Perceptrón de sklearn.linear_model, que es un algoritmo de aprendizaje supervisado
from sklearn.metrics import accuracy_score # Importar la función accuracy_score de sklearn.metrics, que calcula la precisión del modelo

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Convertir el problema a clasificación binaria (0 vs 1)
# Usaremos solo las clases 0 y 1 para simplicidad
X_binary = X[y != 2]
y_binary = y[y != 2]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.3, random_state=42)

# Crear y entrenar el modelo Perceptrón
model = Perceptron(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo Perceptrón: {accuracy * 100:.2f}%")