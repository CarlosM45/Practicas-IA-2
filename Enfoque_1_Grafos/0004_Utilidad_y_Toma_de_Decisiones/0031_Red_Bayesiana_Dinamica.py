import random
from os import system

# Definición de los estados
states = ['A', 'B']

# Probabilidades de transición
# Transiciones en formato: P(A_t | A_t-1, B_t-1)
transitions = {
    ('A', 'A'): 0.9,
    ('A', 'B'): 0.5,
    ('B', 'A'): 0.3,
    ('B', 'B'): 0.8,
}

# Probabilidades de observación
# Observaciones en formato: P(observación | estado)
observation_probs = {
    'A': {'near_A': 0.9, 'near_B': 0.1},
    'B': {'near_A': 0.2, 'near_B': 0.8},
}

# Inicialización de variables
current_state = 'A'  # Estado inicial del sistema
num_steps = 10  # Número de pasos a simular

# Simulación de la RBD
system('cls')
for step in range(num_steps):
    # Observación basada en el estado actual
    if current_state == 'A':
        observation = 'near_A' if random.random() < observation_probs[current_state]['near_A'] else 'near_B'
    else:
        observation = 'near_B' if random.random() < observation_probs[current_state]['near_B'] else 'near_A'

    # Transición al nuevo estado basado en el estado actual
    rand_value = random.random()
    if current_state == 'A':
        if rand_value < transitions[('A', 'A')]:
            new_state = 'A'
        else:
            new_state = 'B'
    else:
        if rand_value < transitions[('B', 'B')]:
            new_state = 'B'
        else:
            new_state = 'A'

    # Imprimir el resultado del paso
    print(f"Paso {step + 1}: Estado actual: {current_state}, Nueva observación: {observation}, Nuevo estado: {new_state}")

    # Actualizar el estado actual
    current_state = new_state