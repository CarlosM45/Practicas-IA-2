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
max_iterations = 100  # Número máximo de iteraciones

# Inicializar política y valores de estado
policy = {state: 'B' for state in states}  # Política inicial arbitraria
V = {state: 0 for state in states}  # Valores iniciales

# Iteración de políticas
for iteration in range(max_iterations):
    # Evaluación de políticas
    while True:
        delta = 0  # Cambio en los valores
        for state in states:
            v = V[state]  # Valor actual
            V[state] = sum(transitions[state].get(next_state, 0) * 
                            (rewards.get((state, policy[state]), 0) + 
                             gamma * V[next_state])
                            for next_state in states) 
            delta = max(delta, abs(v - V[state]))  # Calcular cambio
        if delta < 1e-4:  # Umbral de convergencia
            break

    # Mejora de políticas
    policy_stable = True
    for state in states:
        old_action = policy[state]
        # Seleccionar la acción que maximiza el valor esperado
        policy[state] = max(transitions[state], key=lambda a: sum(transitions[state].get(next_state, 0) * 
                                                                    (rewards.get((state, a), 0) + 
                                                                    gamma * V[next_state])
                                                                    for next_state in states))
        if old_action != policy[state]:
            policy_stable = False

    # Si la política no ha cambiado, hemos encontrado la política óptima
    if policy_stable:
        print(f"Convergencia alcanzada en iteración {iteration + 1}")
        break

# Resultados
system('cls')
print("Política Óptima:")
for state, action in policy.items():
    print(f"En {state} tomar acción: {action}")

print("\nValores de Estado Finales:")
for state, value in V.items():
    print(f"Valor de {state}: {value:.2f}")