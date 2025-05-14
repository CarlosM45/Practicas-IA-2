# Self Organizing Maps – Kohonen Maps
import math # Math es una biblioteca de Python que proporciona funciones matemáticas

class SOM:

	# Función que calcula el vector ganador por distancia euclidiana
	def winner(self, weights, sample):

		D0 = 0 # Distancia al primer cluster
		D1 = 0 # Distancia al segundo cluster

		# Iterando sobre los pesos de cada cluster y calculando la distancia euclidiana
		for i in range(len(sample)):

			D0 = D0 + math.pow((sample[i] - weights[0][i]), 2)
			D1 = D1 + math.pow((sample[i] - weights[1][i]), 2)

		# Seleccionar el cluster con la menor distancia como el ganador

		if D0 < D1:
			return 0
		else:
			return 1

	# Función que actualiza el vector ganador
	def update(self, weights, sample, J, alpha):
		# Iterando sobre los pesos del cluster ganador y actualizándolos
		for i in range(len(weights[0])):
			weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])

		return weights

# Código principal

def main():

	# Ejemplos de entrenamiento
	T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]

	m, n = len(T), len(T[0]) # número de muestras y número de características

	# Inicialización de pesos
	weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]

	# Entrenamiento
	ob = SOM()

	epochs = 3 # número de épocas
	alpha = 0.5 # tasa de aprendizaje

	for i in range(epochs):
		for j in range(m):

			# Muestra de entrenamiento
			sample = T[j]

			# Calcular el vector ganador
			J = ob.winner(weights, sample)

			# Actualizar el vector ganador
			weights = ob.update(weights, sample, J, alpha)

	# Clasificación de una nueva muestra
	s = [0, 0, 0, 1]
	J = ob.winner(weights, s)

	print("Test Sample s belongs to Cluster : ", J)
	print("Trained weights : ", weights)


if __name__ == "__main__":
	main()