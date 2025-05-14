# Máquinas de vectores soporte (Núcleo)
# Importar las bibliotecas necesarias
from sklearn import svm # Importar la biblioteca de máquinas de soporte vectorial
from sklearn import datasets # Importar la biblioteca de conjuntos de datos de sklearn

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()
# Solo tomamos las dos primeras características para la visualización
X = iris.data[:, :2]
y = iris.target

# Entrenar el modelo SVM
# Crear un clasificador SVM con un núcleo lineal
model = svm.SVC(kernel='linear')
model.fit(X, y)
 
# Predecir usando el modelo
predictions = model.predict(X)
 
# Evaluar las predicciones
accuracy = model.score(X, y)
print("Accuracy of SVM:", accuracy)