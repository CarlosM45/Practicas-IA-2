# Monte Carlo para Cadenas de Markov
# code
# importing libraries
import random
import pandas as pd
import numpy as np

# Load the Iris dataset into pandas
df = pd.read_csv("Iris.csv", index_col=0)

# This dataframe contains the sepal length, sepal width and petal length features
data_pd = df.drop(["Species", "PetalWidthCm"], axis=1)
data = data_pd.to_numpy()


# Initial values for sepal length, sepal width and petal length
initial_x = random.uniform(min(data[:, 0]), max(data[:, 0]))
initial_y = random.uniform(min(data[:, 1]), max(data[:, 1]))
initial_z = random.uniform(min(data[:, 2]), max(data[:, 2]))

# Number of Gibbs sampling iterations
num_iterations = 20
samples = []

for _ in range(num_iterations):
	# Sample sepal length (x) from the conditional distribution P(x | y, z)
	x_mean = sum(data[:, 0]) - initial_x
	x = random.gauss(x_mean, 1)

	# Sample sepal width (y) from the conditional distribution P(y | x, z)
	y_mean = sum(data[:, 1]) - initial_y
	y = random.gauss(y_mean, 1)

	# Sample petal length (z) from the conditional distribution P(z | x, y)
	z_mean = sum(data[:, 2]) - initial_z
	z = random.gauss(z_mean, 1)

	samples.append((x, y, z))

# Printing the final samples
samples
