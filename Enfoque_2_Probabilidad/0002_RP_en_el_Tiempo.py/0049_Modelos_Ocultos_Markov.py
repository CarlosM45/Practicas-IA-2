# Modelo oculto de Markov en el aprendizaje automático
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hmmlearn import hmm

# Definir el espacio de estados ocultos, palabras no observables directamente
states = ["Silence", "Word1", "Word2", "Word3"]
n_states = len(states)

# Definir el espacio de observaciones, palabras observables
observations = ["Loud", "Soft"]
n_observations = len(observations)

# Definir la probabilidad inicial de los estados ocultos, probabilidad de que el modelo comience en un estado oculto
start_probability = np.array([0.8, 0.1, 0.1, 0.0])

# Definir las probabilidades de transición entre estados ocultos, probabilidad de pasar de un estado oculto a otro
transition_probability = np.array([[0.7, 0.2, 0.1, 0.0],
									[0.0, 0.6, 0.4, 0.0],
									[0.0, 0.0, 0.6, 0.4],
									[0.0, 0.0, 0.0, 1.0]])

# Definir la probabilidad de emisión, probabilidad de observar una palabra dada un estado oculto
emission_probability = np.array([[0.7, 0.3],
								[0.4, 0.6],
								[0.6, 0.4],
								[0.3, 0.7]])

# Crear el modelo HMM (modelo oculto de Markov)
model = hmm.CategoricalHMM(n_components=n_states)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# Definir la secuencia de observaciones, palabras observadas
observations_sequence = np.array([0, 1, 0, 0, 1, 1, 0, 1]).reshape(-1, 1)

# Predecir los estados ocultos más probables para la secuencia de observaciones
hidden_states = model.predict(observations_sequence)
print("Most likely hidden states:", hidden_states)

# Graficar los resultados
sns.set_style("darkgrid")
plt.plot(hidden_states, '-o', label="Hidden State")
plt.legend()
plt.show()