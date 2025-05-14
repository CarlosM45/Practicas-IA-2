from os import system # Limpiar la consola

# Definimos el problema de coloreo de mapas con 3 colores
variables = ['A', 'B', 'C', 'D', 'E']
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul'],
    'E': ['Rojo', 'Verde', 'Azul']
}

# Restricciones: las regiones adyacentes no pueden tener el mismo color
adyacencias = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Función que verifica si una asignación es consistente con las restricciones
def es_consistente(variable, valor, asignacion):
    for vecino in adyacencias[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Función principal para resolver el CSP usando salto atrás dirigido por conflictos
def salto_atras_dirigido_por_conflictos(asignacion, variables, dominios, adyacencias, nivel, conflictos):
    # Si todas las variables están asignadas, devolver la asignación
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionar la próxima variable no asignada
    variable = variables[nivel]

    # Probar cada valor en el dominio de la variable
    for valor in dominios[variable]:
        if es_consistente(variable, valor, asignacion):
            # Asignar el valor si es consistente
            asignacion[variable] = valor

            # Recursión: intentar asignar el resto de las variables
            resultado = salto_atras_dirigido_por_conflictos(asignacion, variables, dominios, adyacencias, nivel + 1, conflictos)

            # Si se encontró una solución, devolverla
            if resultado:
                return resultado

            # Si se detecta un conflicto, guardar el conflicto en el nivel actual
            conflictos[nivel] = conflictos.get(nivel, set()).union(conflictos.get(nivel + 1, set()))

        # Si hay un conflicto, saltar atrás al nivel relevante
        if nivel in conflictos:
            for conf_nivel in conflictos[nivel]:
                if conf_nivel < nivel:
                    return salto_atras_dirigido_por_conflictos(asignacion, variables, dominios, adyacencias, conf_nivel, conflictos)

    # Si no hay más valores posibles, quitar la asignación y devolver None
    if variable in asignacion:
        del asignacion[variable]
    
    return None

# Resolver el problema
asignacion = {}
conflictos = {}
solucion = salto_atras_dirigido_por_conflictos(asignacion, variables, dominios, adyacencias, 0, conflictos)

# Mostrar la solución si se encuentra
system('cls')
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")