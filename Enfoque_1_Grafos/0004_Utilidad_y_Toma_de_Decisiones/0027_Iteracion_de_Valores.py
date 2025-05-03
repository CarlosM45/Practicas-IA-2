from os import system

# Definimos los estados y las recompensas
states = ['A', 'B']
rewards = {
    ('A', 'B'): 10,
    ('B', 'A'): 0,
    ('B', 'B'): 5
}

# Probabilidades de transición
# P(s'|s,a) para cada acción
transitions = {
    'A': {'B': 1.0},
    'B': {'A': 0.5, 'B': 0.5}
}

# Parámetros
gamma = 0.9  # Factor de descuento
threshold = 1e-4  # Umbral de convergencia
max_iterations = 100  # Número máximo de iteraciones

# Inicializar valores de estado
V = {state: 0 for state in states}

# Iteración de valores
for iteration in range(max_iterations):
    delta = 0  # Cambio en los valores
    for state in states:
        v = V[state]  # Valor actual
        # Actualizar el valor utilizando la ecuación de Bellman
        V[state] = max(sum(transitions[state].get(next_state, 0) * 
                            (rewards.get((state, action), 0) + 
                             gamma * V[next_state])
                            for next_state in states) 
                            for action in transitions[state])
        delta = max(delta, abs(v - V[state]))  # Calcular cambio
    # Verificar convergencia
    if delta < threshold:
        print(f"Convergencia alcanzada en iteración {iteration + 1}")
        break

# Resultados
system('cls')
print("Valores de Estado Finales:")
for state, value in V.items():
    print(f"Valor de {state}: {value:.2f}")