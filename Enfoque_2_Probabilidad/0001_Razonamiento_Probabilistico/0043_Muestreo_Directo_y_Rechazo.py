# Muestreo Directo y por Rechazo
import random

# Probabilidades iniciales
P_A = 0.2  # P(A=True)
P_B_given_A = 0.9  # P(B=True | A=True)
P_B_given_not_A = 0.1  # P(B=True | A=False)

def muestreo_directo(num_muestras):
    """Genera muestras aleatorias para A y B."""
    muestras = []
    for _ in range(num_muestras):
        A = random.random() < P_A  # Muestreamos A
        B = random.random() < (P_B_given_A if A else P_B_given_not_A)  # Muestreamos B dado A
        muestras.append((A, B))
    return muestras

def muestreo_por_rechazo(muestras, evidencia):
    """Filtra las muestras que cumplen con la evidencia."""
    muestras_aceptadas = [A for A, B in muestras if B == evidencia]
    if len(muestras_aceptadas) == 0:
        return 0  # Evitamos división por cero si no hay muestras aceptadas
    # Calculamos P(A | B=True) como la proporción de veces que A fue True
    prob_A_given_B = sum(muestras_aceptadas) / len(muestras_aceptadas)
    return prob_A_given_B

# Generamos 1000 muestras con muestreo directo
muestras = muestreo_directo(1000)

# Aplicamos muestreo por rechazo con evidencia B=True
probabilidad_condicional = muestreo_por_rechazo(muestras, evidencia=True)

print(f"P(A | B=True) ≈ {probabilidad_condicional:.4f}")