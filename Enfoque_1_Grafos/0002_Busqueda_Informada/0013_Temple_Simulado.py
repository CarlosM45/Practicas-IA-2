# Búsqueda de temple simulado para una función unidimensional
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

# Función objetivo
def objective(x):
	return x[0]**2.0

# Algoritmo de temple simulado
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
	# Generar un punto inicial
	best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# Evaluar el punto inicial
	best_eval = objective(best)
	# Solución funcional actual
	curr, curr_eval = best, best_eval
	# Correr el algoritmo
	for i in range(n_iterations):
		# Tomar un paso
		candidate = curr + randn(len(bounds)) * step_size
		# Evaluar punto candidato
		candidate_eval = objective(candidate)
		# Revisar nueva mejor solución
		if candidate_eval < best_eval:
			# Guardar nuevo mejor punto
			best, best_eval = candidate, candidate_eval
			# Reportar progreso
			print('>%d f(%s) = %.5f' % (i, best, best_eval))
		# Diferencia entre candidato y punto de evaluación actual
		diff = candidate_eval - curr_eval
		# Calcular temperatura para cada iteración
		t = temp / float(i + 1)
		# Calcular criterio de metrópolis
		metropolis = exp(-diff / t)
		# Revisar si deberíamos mantener el punto actual
		if diff < 0 or rand() < metropolis:
			# Guardar el nuevo punto actual
			curr, curr_eval = candidate, candidate_eval
	return [best, best_eval]

# Semilla para el generador random
seed(1)
# Definir rango para input
bounds = asarray([[-5.0, 5.0]])
# Definir total de iteraciones
n_iterations = 1000
# Definir máximo tamaño de paso
step_size = 0.1
# Temperatura inicial
temp = 10
# Realizar la búsqueda de temple simulado
best, score = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Done!')
print('f(%s) = %f' % (best, score))