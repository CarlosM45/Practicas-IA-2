# Importar las clases de la base
from grafos import Accion
from grafos import Sala
from grafos import Nodo
from grafos import Problema


# Función principal del algoritmo, busca en todos los hijos de un nodo antes de pasar al siguiente. Ahora incorpora un límite de expansión para cada nodo
def profundidad_limitada(problema, limite):
    raiz = crea_nodo_raiz(problema)
    if problema.es_objetivo(raiz.sala):
        return raiz
    frontera = [(raiz, 0)]
    explorados = set()
    while frontera:
        nodo, profundidad = frontera.pop()
        explorados.add(nodo.sala)
        if profundidad < limite:
            if not nodo.acciones:
                continue
            for nombre_accion in nodo.acciones.keys():
                accion = Accion(nombre_accion)
                hijo = crea_nodo_hijo(problema, nodo, accion)
                salas_frontera = [nodo.sala for nodo, _ in frontera]
                if hijo.sala not in explorados and hijo.sala not in salas_frontera:
                    if problema.es_objetivo(hijo.sala):
                        return hijo
                    frontera.append((hijo, profundidad + 1))
    return None




# Función que crea un nodo de inicio o la sala raíz, revisando si se encuentra entre las claves definidas
def crea_nodo_raiz(problema):
    sala_raiz = problema.sala_inicial
    acciones_raiz = {}
    if sala_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[sala_raiz.nombre]
    raiz = Nodo(sala_raiz, None, acciones_raiz, None)
    return raiz


# Función que crea los nodos hijo de la sala en la que nos encontremos y los asigna al padre
def crea_nodo_hijo(problema, padre, accion):
    nueva_sala = problema.resultado(padre.sala, accion)
    acciones_nuevo = {}
    if nueva_sala.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nueva_sala.nombre]
        hijo = Nodo(nueva_sala, accion, acciones_nuevo, padre)
        padre.hijos.append(hijo)
        return hijo
    

# Función para mostrar la solución, con el formato estructurado para mostrar la sala actual y la acción que se tomó para continuar. También imprime si la solución no existe
def muestra_solucion(objetivo=None):
    if not objetivo:
        print("No hay solución")
        return
    nodo = objetivo
    while nodo:
        msg = "Sala: {0}"
        print(msg.format(nodo.sala.nombre))
        if nodo.accion:
            msg = "<--- {0} ---"
            print(msg.format(nodo.accion.nombre))
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

# Crear problemas para probar el algoritmo, por ejemplo moverse desde la recepción hasta la oficina
objetivo_1 = [office]
problema_1 = Problema(reception, objetivo_1, acciones)

objetivo_2 = [rehab_b]
problema_2 = Problema(reception, objetivo_2, acciones)

objetivo_3 = [storage, exam2]
problema_3 = Problema(reception, objetivo_3, acciones)

# Definir qué problema deseamos resolver
problema_resolver = problema_1

# Almacenar el resultado del algoritmo en una variable y mostrarla con nuestro formato
solucion = profundidad_limitada(problema_resolver, 14)
muestra_solucion(solucion)
