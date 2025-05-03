import numpy as np
from os import system

# Definimos el entorno
num_states = 5  # Número de estados
num_actions = 2  # Número de acciones (0: izquierda, 1: derecha)
goal_state = num_states - 1  # Estado objetivo

# Inicialización de la política (probabilidades)
policy = np.full((num_states, num_actions), 0.5)  # Política inicial (uniforme)

# Parámetros
num_episodes = 300  # Número de episodios
learning_rate = 0.1  # Tasa de aprendizaje
discount_factor = 0.9  # Factor de descuento

# Función de entrenamiento
def train_policy():
    global policy
    for episode in range(num_episodes):
        state = 0  # Comenzar en el estado inicial
        trajectory = []  # Registro de la trayectoria

        # Generar una trayectoria
        while state != goal_state:
            # Elegir acción según la política
            action = np.random.choice(num_actions, p=policy[state])
            next_state = state + (1 if action == 1 else -1)  # Moverse a la derecha o izquierda
            next_state = max(0, min(next_state, goal_state))  # Asegurarse de que el estado esté dentro de límites
            reward = 1 if next_state == goal_state else 0  # Recompensa si se alcanza el estado objetivo

            trajectory.append((state, action, reward))  # Guardar la transición
            state = next_state  # Actualizar el estado

        # Actualizar la política
        for state, action, reward in trajectory:
            # Actualizar la política utilizando el gradiente de la recompensa
            advantage = reward - np.sum(policy[state] * np.array([1 if a == action else 0 for a in range(num_actions)]))
            policy[state][action] += learning_rate * advantage

            # Normalizar la política para asegurarse de que las probabilidades sumen 1
            policy[state] = np.exp(policy[state])  # Aplicar la función exponencial para aumentar la probabilidad
            policy[state] /= np.sum(policy[state])  # Normalizar las probabilidades

# Entrenar la política
train_policy()

# Mostrar la política aprendida
system('cls')
print("Política aprendida (probabilidades de acción):")
print(policy,"\n")

# Mostrar la acción más probable para cada estado
for state in range(num_states):
    action = np.argmax(policy[state])
    print(f"Mejor acción para el estado {state}: {'Derecha' if action == 1 else 'Izquierda'}")