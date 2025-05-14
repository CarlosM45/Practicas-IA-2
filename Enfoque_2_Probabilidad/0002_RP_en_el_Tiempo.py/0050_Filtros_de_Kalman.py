# Filtro de Kalman

# Función de actualización
def update(mean1, var1, mean2, var2):
	new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
	new_var = 1./(1./var1 + 1./var2)
	return [new_mean, new_var]

# Función de predicción, que es la misma que la de actualización pero sin la varianza y media
def predict(mean1, var1, mean2, var2):
	new_mean = mean1 + mean2
	new_var = var1 + var2
	return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000

# Imprimir solo los resultados finales
for measurement, motion in zip(measurements, motion):
	mu, sig = update(measurement, measurement_sig, mu, sig)
	mu, sig = predict(motion, motion_sig, mu, sig)
print([mu, sig])