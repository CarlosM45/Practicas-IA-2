from numpy import array
 
 
# Beta es ancho de haz y distancias son pesos
def beam_search(distances, beta):
    # Inicializar registro
    paths_so_far = [[list(), 0]]  
  
     
    # Moverse por los nodos fila por fila
    for idx, tier in enumerate(distances):
        if idx > 0:
            print(f'Paths kept after tier {idx-1}:')
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()
         
 
        for i in range(len(paths_so_far)):
            path, distance = paths_so_far[i]
             
            # Extender los caminos
            for j in range(len(tier)):
                path_extended = [path + [j], distance + tier[j]]
                paths_at_tier.append(path_extended)
                 
        paths_ordered = sorted(paths_at_tier, key=lambda element: element[1])
         
        # Guardar mejores caminos
        paths_so_far = paths_ordered[:beta]
        print(f'\nPaths reduced to after tier {idx}: ')
        print(*paths_ordered[beta:], sep='\n')
         
    return paths_so_far
 
 
# Matriz de distancia
dists = [[1, 4, 6, 8],
         [5, 2, 3, 4]]
dists = array(dists)
 
# Calcular mejores caminos
best_paths = beam_search(dists, 2)
print('\nThe best paths:')
for beta_path in best_paths:
    print(beta_path)