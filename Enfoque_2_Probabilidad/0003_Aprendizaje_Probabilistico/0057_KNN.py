# k-NN, k-Medias y Clustering
# Programa para implementar el algoritmo de k-NN con pesos y vecinos cercanos

import math # math es una biblioteca de Python que proporciona acceso a funciones matemáticas

def weightedkNN(points,p,k=3): 
	''' 
	Esta función encuentra la clasificación de p utilizando
	el algoritmo de k vecinos más cercanos ponderados. Asume solo dos
	clases y devuelve 0 si p pertenece a la clase 0, de lo contrario
	1 (pertenece a la clase 1).
	
	Parámetros -
		points : Diccionario de puntos de entrenamiento que tiene dos claves - 0 y 1 
			Cada clave tiene una lista de puntos de entrenamiento que pertenecen a esa clase

		p : Una tupla, punto de datos de prueba de la forma (x,y)

		k : número de vecinos más cercanos a considerar, por defecto es 3 
	'''

	# Lista para almacenar la distancia y el grupo de cada punto de entrenamiento
	distance=[] 
	for group in points: 
		for feature in points[group]: 

			# Calcular la distancia euclidiana entre el punto de prueba y el punto de entrenamiento 
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 

			# Añadir la distancia y el grupo a la lista de distancias 
			distance.append((euclidean_distance,group)) 

	# Organizar la lista de distancias en orden ascendente 
	# Y seleccionar los k puntos más cercanos
	# 'sorted' ordena la lista de distancias y '[:k]' selecciona los primeros k elementos
	distance = sorted(distance)[:k] 

	freq1 = 0 # Suma ponderada del grupo 0
	freq2 = 0 # Suma ponderada del grupo 1

	# Calcular la suma ponderada de las distancias para cada grupo
	for d in distance: 
		if d[1] == 0: 
			freq1 += (1 / d[0]) 
			
		elif d[1] == 1: 
			freq2 += (1 /d[0]) 
			

	return 0 if freq1>freq2 else 1

# Función principal
def main(): 

	# Diccionario de puntos de entrenamiento tiene dos claves - 0 y 1 
	# Clave 0 tiene puntos que pertenecen a la clase 0
	# Clave 1 tiene puntos que pertenecen a la clase 1

	points = {0:[(0, 4),(1, 4.9),(1.6, 5.4),(2.2, 6),(2.8, 7),(3.2, 8),(3.4, 9)], 
			1:[(1.8, 1),(2.2, 3),(3, 4),(4, 4.5),(5, 5),(6, 5.5)]} 

	# Punto de prueba
	p = (2, 4) 

	# Número de vecinos más cercanos a considerar 
	k = 5

	print("The value classified to query point is: {}".format(weightedkNN(points,p,k))) # Imprimir el resultado de pertenencia a la clase 

if __name__ == '__main__':
	main()