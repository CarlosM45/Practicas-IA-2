# Regla de la Cadena
# Definimos las probabilidades individuales y condicionadas
P_A = 0.3  # Probabilidad de que llueva
P_B_given_A = 0.9  # Probabilidad de llevar paraguas si llueve
P_C_given_B = 0.7  # Probabilidad de tráfico lento si lleva paraguas

# Aplicando la Regla de la Cadena: P(A, B, C) = P(A) * P(B | A) * P(C | B)
P_ABC = P_A * P_B_given_A * P_C_given_B

print(f"La probabilidad conjunta P(A, B, C) es: {P_ABC:.4f}")