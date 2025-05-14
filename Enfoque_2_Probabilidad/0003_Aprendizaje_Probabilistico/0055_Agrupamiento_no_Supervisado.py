# Agrupamiento No Supervisado
# Importar dependencias
import numpy as np
import pandas as pd # Pandas es una biblioteca de Python para la manipulación y análisis de datos
import matplotlib.pyplot as plt # Matplotlib es una biblioteca de Python para crear gráficos
import sys # sys es un módulo que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python

# Crear datos sintéticos
# Generar datos aleatorios de 4 distribuciones gaussianas
mean_01 = np.array([0.0, 0.0]) # Arreglo de medias para la primera distribución
cov_01 = np.array([[1, 0.3], [0.3, 1]]) # Matriz de covarianza para la primera distribución
dist_01 = np.random.multivariate_normal(mean_01, cov_01, 100) # Generar 100 puntos aleatorios de la distribución normal multivariada

mean_02 = np.array([6.0, 7.0])
cov_02 = np.array([[1.5, 0.3], [0.3, 1]])
dist_02 = np.random.multivariate_normal(mean_02, cov_02, 100)

mean_03 = np.array([7.0, -5.0])
cov_03 = np.array([[1.2, 0.5], 
                   [0.5, 1]]) 
dist_03 = np.random.multivariate_normal(mean_03, cov_01, 100)

mean_04 = np.array([2.0, -7.0])
cov_04 = np.array([[1.2, 0.5], [0.5, 1.3]])
dist_04 = np.random.multivariate_normal(mean_04, cov_01, 100)

data = np.vstack((dist_01, dist_02, dist_03, dist_04)) # Apilar las distribuciones en una sola matriz
np.random.shuffle(data) # Mezclar los datos para que no estén ordenados

# Función para graficar los datos y los centroides
def plot(data, centroids):
    plt.scatter(data[:, 0], data[:, 1], marker='.',
                color='gray', label='data points')
    plt.scatter(centroids[:-1, 0], centroids[:-1, 1],
                color='black', label='previously selected centroids')
    plt.scatter(centroids[-1, 0], centroids[-1, 1],
                color='red', label='next centroid')
    plt.title('Select % d th centroid' % (centroids.shape[0]))

    plt.legend()
    plt.xlim(-5, 12)
    plt.ylim(-10, 15)
    plt.show()

# Función para calcular la distancia euclidiana
def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2)**2))

# Algoitmo de inicialización de K-means++
# K-means++ es un algoritmo de inicialización para el algoritmo K-means
def initialize(data, k):
    '''
    Inicializa los centroides para el algoritmo K-means++
    inputs:
        data - arreglo numpy con datos de los puntos (200, 2)
        k - número de clusters
    '''
    # Inicializa el primer centroide aleatoriamente y agrega a la lista de centroides
    # 'data.shape[0]' devuelve el número de filas en la matriz de datos
    centroids = []
    centroids.append(data[np.random.randint(
        data.shape[0]), :])
    plot(data, np.array(centroids))

    # Calcular los centroides restantes
    # 'k-1' porque ya hemos seleccionado un centroide
    for c_id in range(k - 1):

        # Inicializa una lista para almacenar la distancia mínima de cada punto a los centroides
        dist = []
        for i in range(data.shape[0]):
            point = data[i, :]
            d = sys.maxsize # 'sys.maxsize' devuelve el valor máximo de un entero en Python

            # Calcular la distancia mínima de cada punto a los centroides existentes y guardarla en la lista
            # 'len(centroids)' devuelve el número de centroides seleccionados hasta ahora
            for j in range(len(centroids)):
                temp_dist = distance(point, centroids[j])
                d = min(d, temp_dist)
            dist.append(d)

        # Seleccionar el siguiente centroide en base a la máxima distancia
        # 'np.array(dist)' convierte la lista de distancias en un arreglo numpy
        dist = np.array(dist)
        next_centroid = data[np.argmax(dist), :] # 'np.argmax(dist)' devuelve el índice del valor máximo en la lista de distancias
        centroids.append(next_centroid)
        dist = []
        plot(data, np.array(centroids))
    return centroids


# Llamar la función de inicialización para obtener los centroides
centroids = initialize(data, k=4)
