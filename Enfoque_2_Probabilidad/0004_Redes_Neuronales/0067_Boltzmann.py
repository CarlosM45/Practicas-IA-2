# Boltzmann Machines
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos

# Clase para la Máquina de Boltzmann Restringida (RBM)
class RBM:
	def __init__(self, n_visible, n_hidden):
		self.weights = np.random.randn(n_visible, n_hidden) * 0.1
		self.hidden_bias = np.random.randn(n_hidden) * 0.1
		self.visible_bias = np.random.randn(n_visible) * 0.1

	# Función de muestreo de la capa oculta
	# Esta función toma una capa visible y devuelve una capa oculta muestreada
	def sample_hidden(self, visible):
		activation = np.dot(visible, self.weights) + self.hidden_bias
		probabilities = 1 / (1 + np.exp(-activation))
		return np.random.binomial(1, probabilities)

	# Función de muestreo de la capa visible
	# Esta función toma una capa oculta y devuelve una capa visible muestreada
	def sample_visible(self, hidden):
		activation = np.dot(hidden, self.weights.T) + self.visible_bias
		probabilities = 1 / (1 + np.exp(-activation))
		return np.random.binomial(1, probabilities)

	# Función de entrenamiento de la RBM
	# Esta función toma los datos de entrada, la tasa de aprendizaje y el número de épocas
	def train(self, data, learning_rate, epochs):
		for epoch in range(epochs):
			v0 = data
			h0 = self.sample_hidden(v0)
			v1 = self.sample_visible(h0)
			h1 = self.sample_hidden(v1)

			self.weights += learning_rate * (np.dot(v0.T, h0) - np.dot(v1.T, h1))
			self.visible_bias += learning_rate * np.mean(v0 - v1, axis=0)
			self.hidden_bias += learning_rate * np.mean(h0 - h1, axis=0)

# Clase para la Máquina de Boltzmann Profunda (DBM)
# La DBM consiste en múltiples capas de RBMs apiladas
class DBM:
	def __init__(self, layer_sizes):
		self.rbms = [RBM(layer_sizes[i], layer_sizes[i + 1]) for i in range(len(layer_sizes) - 1)]

	# Preentrenamiento de las capas RBM
	# Esta función toma los datos de entrada, la tasa de aprendizaje y el número de épocas
	def pretrain_layers(self, data, learning_rate, epochs):
		for i, rbm in enumerate(self.rbms):
			print(f"Pretraining RBM Layer {i+1}/{len(self.rbms)}")
			rbm.train(data, learning_rate, epochs)
			data = rbm.sample_hidden(data)

	# Ajuste fino de la DBM
	# Esta función toma los datos de entrada, la tasa de aprendizaje y el número de épocas
	def finetune(self, data, learning_rate, epochs):
		for epoch in range(epochs):
			# Pase hacia adelante
			# Se realiza un pase hacia adelante a través de la DBM para obtener las activaciones de la capa oculta
			up_data = data
			up_pass_data = [data] # Almacena las activaciones de cada capa

			for rbm in self.rbms:
				up_data = rbm.sample_hidden(up_data)
				up_pass_data.append(up_data)

			# Pase hacia atrás
			# Se realiza un pase hacia atrás a través de la DBM para ajustar los pesos
			down_data = up_data
			for i, rbm in enumerate(reversed(self.rbms)):
				down_data = rbm.sample_visible(down_data)
				if i < len(self.rbms) - 1: # No actualizar la capa visible para la última RBM
					# Actualizar los pesos de la RBM
					self.rbms[-i-1].train(up_pass_data[-i-2], learning_rate, 1)

			print(f"Finetuning Epoch {epoch+1}/{epochs}") # Progreso del ajuste fino
	
	
	# Pase hacia adelante a través de la DBM
	# Esta función toma los datos visibles y devuelve las activaciones de la capa oculta
	# Se utiliza para obtener las activaciones de la capa oculta después del preentrenamiento
	def forward_pass(self, visible):
		hidden_data = visible
		for rbm in self.rbms:
			hidden_data = rbm.sample_hidden(hidden_data)
		return hidden_data

# Ejemplo de uso
# Crear una instancia de la DBM con 3 capas (100, 256, 512)
dbm = DBM([100, 256, 512])

# Crear datos de ejemplo (10 muestras, 100 características)
dummy_data = np.random.binomial(1, 0.5, (10, 100))

# Preentrenar las capas de la DBM y ajuste fino
dbm.pretrain_layers(dummy_data, learning_rate=0.01, epochs=5)
dbm.finetune(dummy_data, learning_rate=0.01, epochs=5)

# Paso hacia adelante a través de la DBM
output = dbm.forward_pass(dummy_data)
print("Output from DBM forward pass:\n", output)