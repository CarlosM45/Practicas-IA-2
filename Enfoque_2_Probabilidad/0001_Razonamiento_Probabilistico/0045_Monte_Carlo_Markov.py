# Monte Carlo para Cadenas de Markov
# Importar librerías
import random
import pandas as pd # Librería para manipulación de datos
import numpy as np

# Cargar el conjunto de datos Iris a Pandas
df = pd.read_csv("Iris.csv", index_col=0)

# Este dataframe contiene las columnas longitud y ancho del sépalo y del pétalo, así como la especie de la flor
data_pd = df.drop(["Species", "PetalWidthCm"], axis=1)
data = data_pd.to_numpy()


# Valores iniciales para longitud y ancho del sépalo (x, y) y longitud del pétalo (z)
initial_x = random.uniform(min(data[:, 0]), max(data[:, 0]))
initial_y = random.uniform(min(data[:, 1]), max(data[:, 1]))
initial_z = random.uniform(min(data[:, 2]), max(data[:, 2]))

# Número de iteraciones para el muestreo
num_iterations = 20
samples = []

for _ in range(num_iterations):
	# Muestra la longitud del sépalo (x) de la distribución condicional P(x | y, z)
	x_mean = sum(data[:, 0]) - initial_x
	x = random.gauss(x_mean, 1)

	# Muestrea el ancho del sépalo (y) de la distribución condicional P(y | x, z)
	y_mean = sum(data[:, 1]) - initial_y
	y = random.gauss(y_mean, 1)

	# Muestrea la longitud del pétalo (z) de la distribución condicional P(z | x, y)
	z_mean = sum(data[:, 2]) - initial_z
	z = random.gauss(z_mean, 1)

	samples.append((x, y, z))

# Imprimir los resultados del muestreo de Monte Carlo
samples
