# Procesos Estacionarios
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proceso
np.random.seed(42)  # Para reproducibilidad
n = 1000  # Número de muestras
media = 0  # Media del proceso
varianza = 1  # Varianza del proceso

# Generación del proceso estacionario (ruido blanco)
proceso = np.random.normal(media, np.sqrt(varianza), n)

# Graficamos el proceso
plt.figure(figsize=(10, 4))
plt.plot(proceso, label='Ruido Blanco')
plt.axhline(y=media, color='r', linestyle='--', label='Media')
plt.title('Proceso Estacionario: Ruido Blanco')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.show()
