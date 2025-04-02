# Importar las clases de la base
from grafos import Accion
from grafos import Sala
from grafos import Nodo
from grafos import Problema


# Función principal del algoritmo. Usa la sala inicial y objetivo para encontrar un camino en común entre ellas
def bidireccional(problema):
    raiz_i = crea_nodo_raiz(problema, problema.sala_inicial)
    raiz_f = crea_nodo_raiz(problema, problema.salas_objetivos[0])
    if problema.es_objetivo(raiz_i.sala):
        return (raiz_i, raiz_f)
    if problema.sala_inicial == raiz_f.sala:
        return (raiz_i, raiz_f)
    frontera_i = [raiz_i,]
    frontera_f = [raiz_f,]
    explorados_i = []
    explorados_f = []
    while True:
        if not frontera_i or not frontera_f:
            return (None, None)
        nodo_i = frontera_i.pop(0)
        nodo_f = frontera_f.pop(0)
        explorados_i.append(nodo_i)
        explorados_f.append(nodo_f)
        resultado_i = amplia_frontera(
            problema, nodo_i, problema.salas_objetivos[0], frontera_i, explorados_i)
        if resultado_i:
            return (resultado_i, None)
        resultado_f = amplia_frontera(
            problema, nodo_f, problema.sala_inicial, frontera_f, explorados_f)
        if resultado_f:
            return (None, resultado_f)
        salas_i = set(nodo.sala for nodo in frontera_i)
        salas_f = set(nodo.sala for nodo in frontera_f)
        salas_i = salas_i.union(set(nodo.sala for nodo in explorados_i))
        salas_f = salas_f.union(set(nodo.sala for nodo in explorados_f))
        comunes = salas_i.intersection(salas_f)
        if comunes:
            comun = comunes.pop()
            nodos_arbol_i = []
            nodos_arbol_f = []
            nodos_arbol_i.extend(frontera_i)
            nodos_arbol_f.extend(frontera_f)
            nodos_arbol_i.extend(explorados_i)
            nodos_arbol_f.extend(explorados_f)
            comun_i = [nodo for nodo in nodos_arbol_i if nodo.sala == comun][0]
            comun_f = [nodo for nodo in nodos_arbol_f if nodo.sala == comun][0]
            return (comun_i, comun_f)
        

# Función que crea un nodo de inicio o la sala raíz, revisando si se encuentra entre las claves definidas
def crea_nodo_raiz(problema, sala=None):
    sala_raiz = sala or problema.sala_inicial
    acciones_raiz = {}
    if sala_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[sala_raiz.nombre]
    raiz = Nodo(sala_raiz, acciones=acciones_raiz)
    raiz.coste = 0
    return raiz


# Función que crea los nodos hijo de la sala en la que nos encontremos y los asigna al padre
def crea_nodo_hijo(problema, padre, accion):
    nueva_sala = problema.resultado(padre.sala, accion)
    acciones_nuevo = {}
    if nueva_sala.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nueva_sala.nombre]
    hijo = Nodo(nueva_sala, accion, acciones_nuevo, padre)
    coste=padre.coste
    coste+=problema.coste_accion(padre.sala,accion)
    hijo.coste=coste
    padre.hijos.append(hijo)
    return hijo
    

# Función que amplia la frontera añadiendo un nuevo nodo hijo a la misma
def amplia_frontera(problema, nodo, objetivo, frontera, explorados):
    for nombre_accion in nodo.acciones.keys():
        accion = Accion(nombre_accion)
        hijo = crea_nodo_hijo(problema, nodo, accion)
        salas_frontera = [nodo.sala for nodo in frontera]
        salas_exploradas = [nodo.sala for nodo in explorados]
        if (hijo.sala not in salas_exploradas and hijo.sala not in salas_frontera):
            if objetivo == hijo.sala:
                return hijo
            frontera.append(hijo)
    return None


# Función para mostrar la solución
def muestra_solucion(objetivo=None, solucion=(None, None)):
    nodo_i = solucion[0]
    nodo_f = solucion[1]
    coste_i = nodo_i.coste if nodo_i else 0
    coste_f = nodo_f.coste if nodo_f else 0
    camino = []
    if nodo_i:
        while nodo_i:
            camino.insert(0, nodo_i)
            nodo_i = nodo_i.padre
    if nodo_f:
        nodo_f = nodo_f.padre
        while nodo_f:
            camino.append(nodo_f)
            nodo_f = nodo_f.padre
    if not camino:
        print("No hay solución")
        return
    for nodo in camino:
        msg = "Sala: {0}"
        print(msg.format(nodo.sala.nombre))
    msg = "Coste Total: {0}"
    print(msg.format(coste_i+coste_f))

# Declarar acciones
if __name__ == '__main__':
    accN = Accion('norte')
    accS = Accion('sur')
    accE = Accion('este')
    accO = Accion('oeste')

# Declarar salas que existen con sus posibles acciones
    reception = Sala('Recepción', [accN, accO])
    waiting = Sala('Sala de espera', [accS, accE])
    waiting_b = Sala('Sala de espera B', [accN, accE, accO])
    corridor_a = Sala('Pasillo sección A', [accN, accS, accO])
    corridor_b = Sala('Pasillo sección B', [accN, accS, accE, accO])
    corridor_c = Sala('Pasillo sección C', [accS, accO])
    storage_corridor = Sala('Pasillo de almacén', [accN, accE])
    storage = Sala('Almacén', [accN, accS, accE])
    exam1 = Sala('Sala de examen 1', [accS, accE])
    rehab_b = Sala('Rehabilitación B', [accN, accE, accO])
    exam2 = Sala('Sala de examen 2', [accE, accO])
    rehab = Sala('Rehabilitación', [accS, accE])
    office = Sala('Oficina', [accO])
    roof = Sala('Acceso a azotea', [accO])

# Declarar qué acciones llevan a qué salas
    acciones = {'Recepción': {'norte': waiting,
                                 'oeste': storage_corridor},
                   'Sala de espera': {'sur': reception,
                                      'este': waiting_b},
                   'Sala de espera B': {'norte': corridor_a,
                                        'este': roof,
                                        'oeste': waiting},
                   'Pasillo sección A': {'norte': corridor_b,
                                         'sur': waiting_b,
                                         'oeste': storage},
                   'Pasillo sección B': {'norte': corridor_c,
                                         'sur': corridor_a,
                                         'este': office,
                                         'oeste': exam2},
                   'Pasillo sección C': {'sur': corridor_b,
                                         'oeste': rehab},
                   'Pasillo de almacén': {'norte': storage,
                                          'este': reception},
                   'Almacén': {'norte': exam1,
                               'sur': storage_corridor,
                               'este': corridor_a},
                   'Sala de examen 1': {'sur': storage,
                                        'este': rehab_b},
                   'Rehabilitación B': {'norte': rehab,
                                        'este': exam2,
                                        'oeste': exam1},
                   'Sala de examen 2': {'este': corridor_b,
                                        'oeste': rehab_b},
                   'Rehabilitación': {'sur': rehab_b,
                                      'este': corridor_c},
                   'Oficina': {'oeste': corridor_b},
                   'Acceso a azotea': {'oeste': waiting_b}}
    
    costes = {'Recepción': {'norte': 5,
                         'oeste': 5},
           'Sala de espera': {'sur': 5,
                              'este': 10},
           'Sala de espera B': {'norte': 5,
                                'este': 5,
                                'oeste': 10},
           'Pasillo sección A': {'norte': 5,
                                 'sur': 5,
                                 'oeste': 15},
           'Pasillo sección B': {'norte': 5,
                                 'sur': 5,
                                 'este': 5,
                                 'oeste': 5},
           'Pasillo sección C': {'sur': 5,
                                 'oeste': 10},
           'Pasillo de almacén': {'norte': 10,
                                  'este': 5},
           'Almacén': {'norte': 5,
                       'sur': 10,
                       'este': 15},
           'Sala de examen 1': {'sur': 5,
                                'este': 5},
           'Rehabilitación B': {'norte': 5,
                                'este': 5,
                                'oeste': 5},
           'Sala de examen 2': {'este': 5,
                                'oeste': 5},
           'Rehabilitación': {'sur': 5,
                              'este': 10},
           'Oficina': {'oeste': 5},
           'Acceso a azotea': {'oeste': 5}}

# Crear problemas para probar el algoritmo, por ejemplo moverse desde la recepción hasta la oficina
objetivo_1 = [office]
problema_1 = Problema(reception, objetivo_1, acciones,costes)

objetivo_2 = [rehab_b]
problema_2 = Problema(reception, objetivo_2, acciones,costes)

objetivo_3 = [storage, exam2]
problema_3 = Problema(reception, objetivo_3, acciones,costes)

# Definir qué problema deseamos resolver
problema_resolver = problema_1

# Almacenar el resultado del algoritmo en una variable y mostrarla con nuestro formato
solucion = bidireccional(problema_resolver)
muestra_solucion(solucion=solucion)
