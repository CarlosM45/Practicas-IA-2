# Boltzmann Machines
import numpy as np

class RBM:
	def __init__(self, n_visible, n_hidden):
		self.weights = np.random.randn(n_visible, n_hidden) * 0.1
		self.hidden_bias = np.random.randn(n_hidden) * 0.1
		self.visible_bias = np.random.randn(n_visible) * 0.1

	def sample_hidden(self, visible):
		activation = np.dot(visible, self.weights) + self.hidden_bias
		probabilities = 1 / (1 + np.exp(-activation))
		return np.random.binomial(1, probabilities)

	def sample_visible(self, hidden):
		activation = np.dot(hidden, self.weights.T) + self.visible_bias
		probabilities = 1 / (1 + np.exp(-activation))
		return np.random.binomial(1, probabilities)

	def train(self, data, learning_rate, epochs):
		for epoch in range(epochs):
			v0 = data
			h0 = self.sample_hidden(v0)
			v1 = self.sample_visible(h0)
			h1 = self.sample_hidden(v1)

			self.weights += learning_rate * (np.dot(v0.T, h0) - np.dot(v1.T, h1))
			self.visible_bias += learning_rate * np.mean(v0 - v1, axis=0)
			self.hidden_bias += learning_rate * np.mean(h0 - h1, axis=0)


class DBM:
	def __init__(self, layer_sizes):
		self.rbms = [RBM(layer_sizes[i], layer_sizes[i + 1]) for i in range(len(layer_sizes) - 1)]

	def pretrain_layers(self, data, learning_rate, epochs):
		for i, rbm in enumerate(self.rbms):
			print(f"Pretraining RBM Layer {i+1}/{len(self.rbms)}")
			rbm.train(data, learning_rate, epochs)
			data = rbm.sample_hidden(data)

	def finetune(self, data, learning_rate, epochs):
		for epoch in range(epochs):
			# Bottom-up pass
			up_data = data
			up_pass_data = [data] # Store the activation at each layer

			for rbm in self.rbms:
				up_data = rbm.sample_hidden(up_data)
				up_pass_data.append(up_data)

			# Top-down pass
			down_data = up_data
			for i, rbm in enumerate(reversed(self.rbms)):
				down_data = rbm.sample_visible(down_data)
				if i < len(self.rbms) - 1: # Do not update the visible layer of the first RBM
					# Update the corresponding RBM with the data from the layer above
					self.rbms[-i-1].train(up_pass_data[-i-2], learning_rate, 1)

			print(f"Finetuning Epoch {epoch+1}/{epochs}")
	

	def forward_pass(self, visible):
		hidden_data = visible
		for rbm in self.rbms:
			hidden_data = rbm.sample_hidden(hidden_data)
		return hidden_data

# Example usage
dbm = DBM([100, 256, 512]) # Example layer sizes

# Create some dummy data
dummy_data = np.random.binomial(1, 0.5, (10, 100))

# Pretrain and finetune the DBM
dbm.pretrain_layers(dummy_data, learning_rate=0.01, epochs=5)
dbm.finetune(dummy_data, learning_rate=0.01, epochs=5)

# Forward pass through the DBM
output = dbm.forward_pass(dummy_data)
print("Output from DBM forward pass:\n", output)