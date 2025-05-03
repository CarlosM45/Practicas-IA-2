import numpy as np
from os import system

# Definimos los estados y las recompensas
states = [0, 1, 2, 3, 4]  # Estados
rewards = [0, 0, 0, 0, 1]  # Recompensa en cada estado (solo en el estado 4)

# Definimos la política (fija en este caso)
policy = {0: 1, 1: 2, 2: 3, 3: 4, 4: 4}  # El agente se mueve siempre a la derecha

# Número de episodios para simular
num_episodes = 100
value_estimates = np.zeros(len(states))  # Estimaciones del valor de cada estado
returns_count = np.zeros(len(states))  # Contador de retornos para promediar

# Simulación de episodios
for episode in range(num_episodes):
    state = 0  # Comenzar en el estado inicial
    episode_reward = 0  # Recompensa total para el episodio

    while state != 4:  # Continuar hasta que se alcance el estado 4
        episode_reward += rewards[state]  # Sumar la recompensa del estado actual
        state = policy[state]  # Movimiento basado en la política

    episode_reward += rewards[4]  # Agregar la recompensa final del último estado
    value_estimates[0] += episode_reward  # Solo se actualiza el estado 0

    # Contar el retorno para calcular el promedio
    returns_count[0] += 1  # Incrementar el contador de retornos para el estado 0

# Calcular el valor promedio
for i in range(len(states)):
    if returns_count[i] > 0:
        value_estimates[i] /= returns_count[i]

# Mostrar resultados
system('cls')
for state in states:
    print(f"Valor estimado para el estado {state}: {value_estimates[state]:.2f}")