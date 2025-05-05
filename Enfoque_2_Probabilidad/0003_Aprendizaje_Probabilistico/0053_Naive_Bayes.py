# Bayes ingenuos
# Cargar el conjunto de datos Iris
from sklearn.datasets import load_iris
iris = load_iris()

# Almacenar la matriz de características (X) y el vector de respuesta (y)
X = iris.data
y = iris.target

# Dividir X e y en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# Entrenar el modelo en el conjunto de entrenamiento
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = gnb.predict(X_test)

# Comparar los valores reales (y_test) con los valores predichos (y_pred)
from sklearn import metrics
accuracy = metrics.accuracy_score(y_test, y_pred) * 100

print(f"Gaussian Naive Bayes model accuracy (in %): {accuracy:.2f}")
