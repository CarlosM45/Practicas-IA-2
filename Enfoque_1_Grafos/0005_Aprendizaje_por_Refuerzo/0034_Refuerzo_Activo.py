import numpy as np
import random
from os import system

# Definimos el entorno
states = [0, 1, 2, 3, 4]  # Estados
actions = [0, 1]  # 0: izquierda, 1: derecha
rewards = [0, 0, 0, 0, 1]  # Recompensas (solo en el estado 4)
num_episodes = 1000  # Número de episodios

# Inicializamos la tabla Q
Q = np.zeros((len(states), len(actions)))

# Parámetros
learning_rate = 0.1  # Tasa de aprendizaje
discount_factor = 0.9  # Factor de descuento
exploration_prob = 0.1  # Probabilidad de explorar

# Q-Learning
for episode in range(num_episodes):
    state = 0  # Comenzar en el estado inicial

    while state != 4:  # Hasta que se alcance el estado 4
        if random.uniform(0, 1) < exploration_prob:  # Exploración
            action = random.choice(actions)
        else:  # Explotación
            action = np.argmax(Q[state])  # Seleccionar la mejor acción conocida

        # Tomar acción y recibir recompensa
        next_state = state + (1 if action == 1 else -1)  # Moverse a la derecha o izquierda
        next_state = max(0, min(next_state, 4))  # Asegurarse de que el estado esté dentro de límites
        reward = rewards[next_state]  # Obtener la recompensa

        # Actualizar la tabla Q
        Q[state, action] += learning_rate * (reward + discount_factor * np.max(Q[next_state]) - Q[state, action])
        state = next_state  # Mover al siguiente estado

# Mostrar la tabla Q
system('cls')
print("Tabla Q final:")
print(Q)

# Mostrar la política aprendida
policy = np.argmax(Q, axis=1)
for state in states:
    print(f"Mejor acción para el estado {state}: {'Derecha' if policy[state] == 1 else 'Izquierda'}")