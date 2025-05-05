# Manto de Markov
# Red básica de relaciones: A → B → C
graph = {
    'A': [],
    'B': ['A'],  # B depende de A
    'C': ['B']   # C depende de B
}

# Función para encontrar el Manto de Markov de un nodo
def markov_blanket(node, graph):
    parents = [n for n, children in graph.items() if node in children]
    children = graph[node]
    co_parents = [p for c in children for p in graph if c in graph[p] and p != node]

    return set(parents + children + co_parents)

# Ejemplo: Encontramos el Manto de Markov del nodo 'B'
manto_de_b = markov_blanket('B', graph)
print(f"El Manto de Markov del nodo 'B' es: {manto_de_b}")
