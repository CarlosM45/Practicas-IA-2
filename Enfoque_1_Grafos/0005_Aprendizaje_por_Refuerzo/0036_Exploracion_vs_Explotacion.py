import numpy as np
import random
import matplotlib.pyplot as plt
from os import system

# Parámetros
num_actions = 3  # Número de acciones disponibles
num_episodes = 1000  # Número de episodios
epsilon = 0.1  # Probabilidad de explorar
learning_rate = 0.1  # Tasa de aprendizaje

# Recompensas verdaderas de cada acción (desconocidas para el agente)
true_rewards = [1, 2, 3]  # Recompensas esperadas de las acciones
estimated_rewards = np.zeros(num_actions)  # Estimación de las recompensas
action_counts = np.zeros(num_actions)  # Contador de acciones tomadas

# Registro de recompensas
total_rewards = []

# Proceso de aprendizaje
for episode in range(num_episodes):
    # Decidir entre exploración y explotación
    if random.random() < epsilon:
        action = random.choice(range(num_actions))  # Exploración
    else:
        action = np.argmax(estimated_rewards)  # Explotación

    # Simular la recompensa (en un entorno real, se obtendría del entorno)
    reward = np.random.normal(true_rewards[action], 0.1)  # Recompensa con un poco de ruido

    # Actualizar el contador de acciones
    action_counts[action] += 1

    # Actualizar la estimación de recompensa
    estimated_rewards[action] += learning_rate * (reward - estimated_rewards[action])

    # Almacenar la recompensa total
    total_rewards.append(reward)

# Resultados
system('cls')
print("Estimaciones finales de recompensas:", estimated_rewards)
print("Acciones tomadas:", action_counts)

# Graficar las recompensas totales
plt.plot(total_rewards)
plt.title('Recompensas Totales por Episodio')
plt.xlabel('Episodio')
plt.ylabel('Recompensa')
plt.show()