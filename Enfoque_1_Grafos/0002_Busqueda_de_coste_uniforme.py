# Importar las clases de la base
from grafos import Accion
from grafos import Sala
from grafos import Nodo
from grafos import Problema


# Función principal del algoritmo, mediante una prioridad de menor coste va creando los nodos similar a anchura, consumiendo tiempo y espacio exponenciales
def coste_uniforme(problema):
    raiz = crea_nodo_raiz(problema)
    frontera = [raiz,]
    explorados = set()
    while True:
        if not frontera:
            return None
        nodo = frontera.pop(0)
        if problema.es_objetivo(nodo.sala):
            return nodo
        explorados.add(nodo.sala)
        if not nodo.acciones:
            continue
        for nombre_accion in nodo.acciones.keys():
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            salas_frontera = [nodo.sala for nodo in frontera]
            if (hijo.sala not in explorados and hijo.sala not in salas_frontera):
                frontera.append(hijo)
            else:
                buscar = [nodo for nodo in frontera if nodo.sala == hijo.sala]
                if buscar:
                    if hijo.coste < buscar[0].coste:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.coste)

# Función que crea un nodo de inicio o la sala raíz, revisando si se encuentra entre las claves definidas. Define el coste 0 pues es la primera sala
def crea_nodo_raiz(problema):
    sala_raiz = problema.sala_inicial
    acciones_raiz = {}
    if sala_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[sala_raiz.nombre]
    raiz = Nodo(sala_raiz, None, acciones_raiz, None)
    raiz.coste = 0
    return raiz


# Función que crea los nodos hijo de la sala en la que nos encontremos y los asigna al padre. Además va añadiendo el coste
def crea_nodo_hijo(problema, padre, accion):
    nueva_sala = problema.resultado(padre.sala, accion)
    acciones_nuevo = {}
    if nueva_sala.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nueva_sala.nombre]
        hijo = Nodo(nueva_sala, accion, acciones_nuevo, padre)
        coste = padre.coste
        coste += problema.coste_accion(padre.sala, accion)
        hijo.coste = coste
        padre.hijos.append(hijo)
        return hijo
    

# Función para mostrar la solución, con el formato estructurado para mostrar la sala actual, el movimiento que se tomó para continuar y el coste total hasta esa acción
def muestra_solucion(objetivo=None):
    if not objetivo:
        print("No hay solución")
        return
    nodo = objetivo
    while nodo:
        msg = "Sala: {0}, Coste Total: {1}"
        sala = nodo.sala.nombre
        coste_total = nodo.coste
        print(msg.format(sala, coste_total))
        if nodo.accion:
            accion = nodo.accion.nombre
            padre = nodo.padre.sala
            coste = problema_resolver.coste_accion(padre, nodo.accion)
            msg = "<--- {0} [{1}] ---"
            print(msg.format(accion, coste))
        nodo = nodo.padre

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
    # Coste en metros promedio que toma realizar los movimientos
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
problema_1 = Problema(reception, objetivo_1, acciones, costes)

objetivo_2 = [rehab_b]
problema_2 = Problema(reception, objetivo_2, acciones, costes)

objetivo_3 = [storage, exam2]
problema_3 = Problema(reception, objetivo_3, acciones, costes)

# Definir qué problema deseamos resolver
problema_resolver = problema_1

# Almacenar el resultado del algoritmo en una variable y mostrarla con nuestro formato
solucion = coste_uniforme(problema_resolver)
muestra_solucion(solucion)
