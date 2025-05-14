# Proceso de Decisión de Markov (MDP) en Python
from os import system

# Definimos los estados, acciones, transiciones y recompensas
states = ['A', 'B', 'C']
actions = {
    'A': ['go_to_B', 'go_to_C'],
    'B': ['go_to_A', 'go_to_C'],
    'C': ['go_to_A'],
}

# Funciones de transición y recompensas
transitions = {
    ('A', 'go_to_B'): ('B', 5),   # Va a B con recompensa 5
    ('A', 'go_to_C'): ('C', 10),  # Va a C con recompensa 10
    ('B', 'go_to_A'): ('A', 0),   # Va a A con recompensa 0
    ('B', 'go_to_C'): ('C', 2),    # Va a C con recompensa 2
    ('C', 'go_to_A'): ('A', 1),    # Va a A con recompensa 1
}

# Parámetros
gamma = 0.9  # Factor de descuento
max_iterations = 100

# Inicializamos la función de valor
V = {state: 0 for state in states}

# Iteración de valores
for iteration in range(max_iterations):
    delta = 0  # Cambio en los valores
    for state in states:
        v = V[state]  # Valor actual
        # Calcular el nuevo valor
        V[state] = max(
            [transitions[(state, action)][1] + 
             gamma * V[transitions[(state, action)][0]] for action in actions[state]]
        )
        delta = max(delta, abs(v - V[state]))  # Calcular cambio
    if delta < 1e-4:  # Umbral de convergencia
        print(f"Convergencia alcanzada en iteración {iteration + 1}")
        break

# Resultados
system('cls')
print("Valores de Estado Finales:")
for state, value in V.items():
    print(f"Valor de {state}: {value:.2f}")