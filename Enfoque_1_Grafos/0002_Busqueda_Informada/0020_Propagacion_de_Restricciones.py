import matplotlib.pyplot as plt
import networkx as nx

class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables  # Lista de variables para ser restringidas
        self.domains = domains  # Diccionario de dominios para cada variable
        self.neighbors = neighbors  # Diccionario de vecinos para cada variable
        self.constraints = constraints  # Función que retorna True si la restricción se cumple

    def is_consistent(self, var, assignment):
        """Verificar si una asignación es consistente verificando todas las restricciones."""
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and not self.constraints(var, assignment[var], neighbor, assignment[neighbor]):
                return False
        return True

    def ac3(self):
        """Algoritmo para propagación de restricciones AC-3."""
        queue = [(xi, xj) for xi in self.variables for xj in self.neighbors[xi]]
        
        while queue:
            (xi, xj) = queue.pop(0)
            if self.revise(xi, xj):
                if len(self.domains[xi]) == 0:
                    return False
                for xk in self.neighbors[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self, xi, xj):
        """Revisar el dominio de xi para satisfacer las restricciones entre xi y xj."""
        revised = False
        for x in set(self.domains[xi]):
            if not any(self.constraints(xi, x, xj, y) for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        return revised

    def backtracking_search(self, assignment={}):
        """Búsqueda Backtracking para encontrar una solución."""
        # Si la asignación es completa, devolverla
        if len(assignment) == len(self.variables):
            return assignment
        
        # Seleccionar una variable no asignada
        var = self.select_unassigned_variable(assignment)
        
        # Intentar cada valor en el dominio de la variable seleccionada
        for value in self.domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.is_consistent(var, new_assignment):
                result = self.backtracking_search(new_assignment)
                if result:
                    return result
        
        return None

    def select_unassigned_variable(self, assignment):
        """Seleccionar una variable no asignada."""
        for var in self.variables:
            if var not in assignment:
                return var
        return None

def constraint(var1, val1, var2, val2):
    """Función de restricción: Ningún nodo vecino puede compartir el mismo color."""
    return val1 != val2

def visualize_solution(solution, neighbors):
    """Visualizar la solución usando matplotlib y networkx."""
    G = nx.Graph()
    for var in solution:
        G.add_node(var, color=solution[var])
    for var, neighs in neighbors.items():
        for neigh in neighs:
            G.add_edge(var, neigh)
    
    colors = [G.nodes[node]['color'] for node in G.nodes]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, font_size=16, font_color='white', font_weight='bold')
    plt.show()

# Variables
variables = ['A', 'B', 'C', 'D', "E"]

# Dominios
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue'],
    'D': ['Red', 'Green', 'Blue'],
    'E': ['Red', 'Green', 'Blue']
}

# Vecinos
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
    'E': ['A', 'B']
}

# Crear el CSP
csp = CSP(variables, domains, neighbors, constraint)

# Aplicar AC-3 para reducir los dominios
if csp.ac3():
    # Usar backtracking para encontrar una solución
    solution = csp.backtracking_search()
    if solution:
        print("Solution found:")
        for var in variables:
            print(f"{var}: {solution[var]}")
        visualize_solution(solution, neighbors)
    else:
        print("No solution found")
else:
    print("No solution found")