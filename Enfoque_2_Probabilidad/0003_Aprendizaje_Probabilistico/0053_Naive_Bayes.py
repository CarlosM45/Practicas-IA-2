# Bayes ingenuos
# Cargar el conjunto de datos Iris
from sklearn.datasets import load_iris # Sklearn es una biblioteca de recursos de aprendizaje automático
iris = load_iris() # Iris es un conjunto de datos clásico para clasificación con muestras de flores

# Almacenar la matriz de características (X) y el vector de respuesta (y)
X = iris.data
y = iris.target

# Dividir X e y en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split # train_test_split es una función que divide los datos en conjuntos de entrenamiento y prueba
# test_size=0.4 significa que el 40% de los datos se utilizarán para la prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) # random_state=1 asegura que la división sea reproducible

# Entrenar el modelo en el conjunto de entrenamiento
from sklearn.naive_bayes import GaussianNB # Importar la clase GaussianNB de sklearn.naive_bayes, que implementa el clasificador Naive Bayes
# GaussianNB es un clasificador Naive Bayes que asume que las características siguen una distribución normal
gnb = GaussianNB()
gnb.fit(X_train, y_train) # Ajustar el modelo a los datos de entrenamiento

# Realizar predicciones en el conjunto de prueba
y_pred = gnb.predict(X_test)

# Comparar los valores reales (y_test) con los valores predichos (y_pred)
from sklearn import metrics # Importar la biblioteca de métricas de sklearn para evaluar el rendimiento del modelo
# accuracy_score calcula la precisión del modelo comparando las etiquetas verdaderas con las predicciones
accuracy = metrics.accuracy_score(y_test, y_pred) * 100

print(f"Gaussian Naive Bayes model accuracy (in %): {accuracy:.2f}")
