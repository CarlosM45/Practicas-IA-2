# Separabilidad lineal
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# Crear un conjunto de datos linealmente separable
X = np.array([[2, 3], [3, 4], [4, 5], [6, 7], [1, 8], [7, 2], [8, 3], [9, 1]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])  # Etiquetas

# Crear y entrenar un perceptrón
model = Perceptron(max_iter=1000, random_state=42)
model.fit(X, y)

# Obtener los coeficientes del hiperplano (w1*x1 + w2*x2 + b = 0)
w = model.coef_[0]
b = model.intercept_

# Crear la línea de decisión
x_points = np.linspace(0, 10, 100)
y_points = -(w[0] * x_points + b) / w[1]

# Visualizar los puntos y la línea de separación
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
plt.plot(x_points, y_points, color='black', linestyle='--', label='Línea de separación')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Separabilidad Lineal con Perceptrón')
plt.legend()
plt.show()