# Procesos de Markov
# Importar librerías
import scipy.linalg # Librería para álgebra lineal
import numpy as np


# Definir la matriz de transición de la cadena de Markov, una matriz cuadrada
state = ["A", "E"]

# Asignando la matriz de transición
MyMatrix = np.array([[0.6, 0.4], [0.7, 0.3]])

# Simulando un proceso de Markov de 20 pasos
n = 20

# Definir el estado inicial
StartingState = 0
CurrentState = StartingState

# Imprimir el estado actual usando el diccionario
print(state[CurrentState], "--->", end=" ")

while n-1:
	# Decidir el siguiente estado usando una decisión aleatoria usando la matriz de transición (se elije de acuerdo a probabilidad)
	CurrentState = np.random.choice([0, 1], p=MyMatrix[CurrentState])
	
	# Imprimir camino del proceso
	print(state[CurrentState], "--->", end=" ")
	n -= 1
print("stop")

# Encontrar los vectores eigen
MyValues, left = scipy.linalg.eig(MyMatrix, right=False, left=True) # Los vectores eigen son vectores que no cambian de dirección al ser multiplicados por la matriz
# left es el vector propio izquierdo y right es el vector propio derecho

print("left eigen vectors = \n", left, "\n")
print("eigen values = \n", MyValues)

# Pi es una ditribución de probabilidad, por lo que la suma de sus elementos debe ser 1. Normalizamos pi
pi = left[:, 0]
pi_normalized = [(x/np.sum(pi)).real for x in pi]
pi_normalized
