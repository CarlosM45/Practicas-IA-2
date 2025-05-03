import numpy as np
from os import system

# Definimos los estados, acciones y observaciones
states = ['A', 'B']
actions = ['move_to_A', 'move_to_B']
observations = ['near_A', 'near_B']

# Funciones de transición
transitions = {
    ('A', 'move_to_A'): ('A', 5),
    ('A', 'move_to_B'): ('B', 0),
    ('B', 'move_to_A'): ('A', 0),
    ('B', 'move_to_B'): ('B', 2),
}

# Funciones de observación
observations_func = {
    ('A', 'move_to_A'): 'near_A',
    ('A', 'move_to_B'): 'near_B',
    ('B', 'move_to_A'): 'near_A',
    ('B', 'move_to_B'): 'near_B',
}

# Probabilidad de observar dado el estado
observation_probs = {
    'near_A': {'A': 0.9, 'B': 0.1},
    'near_B': {'A': 0.1, 'B': 0.9},
}

# Parámetros
gamma = 0.9  # Factor de descuento
belief = {'A': 0.5, 'B': 0.5}  # Creencia inicial
current_state = 'A'  # Estado inicial del agente

# Simulación de un POMDP
num_steps = 10
for step in range(num_steps):
    # Elegir una acción (por simplicidad, aleatoria)
    action = np.random.choice(actions)

    # Determinar el nuevo estado y la recompensa basado en el estado actual y la acción
    new_state, reward = transitions[(current_state, action)]

    # Obtener observación basada en el nuevo estado y la acción
    observation = observations_func[(new_state, action)]

    # Actualizar la creencia
    new_belief = {}
    for state in states:
        new_belief[state] = belief[state] * observation_probs[observation][state]
    
    # Normalizar la creencia
    total = sum(new_belief.values())
    for state in states:
        new_belief[state] /= total
    
    # Actualizar la creencia y el estado actual
    belief = new_belief
    current_state = new_state  # Actualizar al nuevo estado real

    # Imprimir resultados
    print(f"Paso {step + 1}: Acción: {action}, Estado: {new_state}, Observación: {observation}, Creencia: {belief}")

# Resultados finales
system('cls')
print("Creencia Final:")
print(belief)