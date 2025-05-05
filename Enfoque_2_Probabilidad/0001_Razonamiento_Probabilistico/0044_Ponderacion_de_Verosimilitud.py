# Ponderacion de verosimilitud
import random

# Probabilidades iniciales
P_A = 0.2  # P(A=True)
P_B_given_A = 0.9  # P(B=True | A=True)
P_B_given_not_A = 0.1  # P(B=True | A=False)

def ponderacion_verosimilitud(num_muestras):
    """Genera muestras con ponderación de verosimilitud."""
    suma_pesos = 0  # Suma total de pesos
    suma_pesos_A_true = 0  # Suma de pesos donde A=True

    for _ in range(num_muestras):
        # Generamos A de forma aleatoria
        A = random.random() < P_A
        
        # Fijamos B como True (evidencia) y calculamos su peso
        peso = P_B_given_A if A else P_B_given_not_A

        # Acumulamos los pesos
        suma_pesos += peso
        if A:
            suma_pesos_A_true += peso

    # Calculamos P(A | B=True) usando los pesos acumulados
    prob_A_given_B = suma_pesos_A_true / suma_pesos if suma_pesos != 0 else 0
    return prob_A_given_B

# Ejecutamos el algoritmo con 1000 muestras
probabilidad = ponderacion_verosimilitud(1000)
print(f"P(A | B=True) ≈ {probabilidad:.4f}")