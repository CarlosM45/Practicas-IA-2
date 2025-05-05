# Inferencia por Enumeracion
# Definimos las probabilidades
P_A = 0.2  # Probabilidad de que la alarma se active
P_not_A = 1 - P_A  # Probabilidad de que no se active

P_B_given_A = 0.9  # Probabilidad de llamada si hay alarma
P_B_given_not_A = 0.1  # Probabilidad de llamada sin alarma

# Inferencia por enumeración: P(A | B) = α * P(A) * P(B | A)
def enumeracion_inferencia(P_A, P_B_given_A, P_B_given_not_A):
    # Calculamos las probabilidades conjuntas
    P_AB = P_A * P_B_given_A
    P_not_AB = (1 - P_A) * P_B_given_not_A

    # Normalizamos para que las probabilidades sumen 1
    alpha = 1 / (P_AB + P_not_AB)
    P_A_given_B = alpha * P_AB

    return P_A_given_B

# Llamamos a la función
probabilidad_alarma = enumeracion_inferencia(P_A, P_B_given_A, P_B_given_not_A)
print(f"La probabilidad de que haya habido una alarma, dado que hubo una llamada, es: {probabilidad_alarma:.4f}")
