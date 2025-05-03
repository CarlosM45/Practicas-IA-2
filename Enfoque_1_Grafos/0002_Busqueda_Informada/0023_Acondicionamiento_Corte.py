import random
from os import system

# Definimos el problema de coloreo de mapas con 3 colores
variables = ['A', 'B', 'C', 'D', 'E']
dominios = ['Rojo', 'Verde', 'Azul']

# Restricciones: las regiones adyacentes no pueden tener el mismo color
adyacencias = {
    'A': ['B'],
    'B': ['A', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Función para contar conflictos en una asignación
def contar_conflictos(asignacion):
    conflictos = 0
    for variable, valor in asignacion.items():
        for vecino in adyacencias[variable]:
            if vecino in asignacion and asignacion[vecino] == valor:
                conflictos += 1
    return conflictos

# Función para aplicar acondicionamiento del corte
def acondicionamiento_del_corte(asignacion):
    for variable in asignacion:
        for color in dominios:
            # Verificar si este color genera conflictos
            asignacion[variable] = color
            if contar_conflictos(asignacion) == 0:
                continue  # Este color no genera conflictos
            # Si genera conflictos, eliminar el color del dominio
            else:
                dominios.remove(color)

# Algoritmo de Mínimos Conflictos con Acondicionamiento del Corte
def min_conflicts_con_cortes(variables, dominios, adyacencias, max_intentos=200):
    # Inicializar asignación aleatoria
    asignacion = {variable: random.choice(dominios) for variable in variables}
    
    # Aplicar acondicionamiento del corte
    acondicionamiento_del_corte(asignacion)

    for _ in range(max_intentos):
        conflictos = contar_conflictos(asignacion)
        if conflictos == 0:
            return asignacion  # Solución encontrada
        
        # Elegir una variable con conflictos
        variables_conflictivas = [var for var in asignacion if contar_conflictos({var: asignacion[var]}) > 0]

        if not variables_conflictivas:
            break  # Si no hay variables conflictivas, salir del bucle

        variable_conflicto = random.choice(variables_conflictivas)

        # Encontrar el color que minimiza los conflictos
        mejor_color = None
        min_conflictos = float('inf')

        for color in dominios:
            asignacion[variable_conflicto] = color
            num_conflictos = contar_conflictos(asignacion)
            if num_conflictos < min_conflictos:
                min_conflictos = num_conflictos
                mejor_color = color

        # Asignar el mejor color
        asignacion[variable_conflicto] = mejor_color

    return None  # No se encontró solución en el número máximo de intentos

# Resolver el problema
solucion = min_conflicts_con_cortes(variables, dominios, adyacencias)

# Mostrar la solución si se encuentra
system('cls')
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")