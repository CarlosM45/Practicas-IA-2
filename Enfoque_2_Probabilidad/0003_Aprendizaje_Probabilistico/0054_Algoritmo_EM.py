# Algortimo EM
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

# Generar datos simulados para agrupamiento
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=0)

# Crear un modelo de mezcla gaussiana con 3 componentes
gmm = GaussianMixture(n_components=3, max_iter=100, random_state=0)

# Ajustar el modelo a los datos con EM
gmm.fit(X)

# Predecir los clústeres para cada punto
labels = gmm.predict(X)

# Imprimir los parámetros del modelo (medias de los componentes)
print("Medias de los componentes:\n", gmm.means_)

# Ver la probabilidad de pertenencia de cada punto a un componente
probas = gmm.predict_proba(X)
print("Probabilidades (primeros 5 puntos):\n", probas[:5])
