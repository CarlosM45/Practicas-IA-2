# Eliminacion de Variables
# Definimos las probabilidades
P_A = 0.2  # Probabilidad de que la alarma se active
P_C = 0.3  # Probabilidad de corte de energía

# Condicionales
P_B_given_A = 0.9  # Probabilidad de llamada si hay alarma
P_B_given_not_A = 0.1  # Probabilidad de llamada sin alarma
P_A_given_C = 0.5  # Probabilidad de alarma con corte de energía
P_A_given_not_C = 0.2  # Probabilidad de alarma sin corte

# Suma marginal para eliminar variables (B y C)
def eliminacion_variables(P_A, P_B_given_A, P_B_given_not_A, P_C, P_A_given_C, P_A_given_not_C):
    # Calculamos P(A) sumando sobre las combinaciones posibles de C
    P_A_given_C_combined = P_C * P_A_given_C + (1 - P_C) * P_A_given_not_C
    
    # Normalizamos (opcional si queremos una distribución que sume 1)
    alpha = 1 / (P_A_given_C_combined)
    P_A_marginal = alpha * P_A_given_C_combined

    return P_A_marginal

# Ejecutamos la función
probabilidad_alarma = eliminacion_variables(P_A, P_B_given_A, P_B_given_not_A, P_C, P_A_given_C, P_A_given_not_C)
print(f"La probabilidad marginal de que haya alarma es: {probabilidad_alarma:.4f}")
