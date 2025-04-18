# Importar las clases de la base
from grafos import Accion
from grafos import Sala
from grafos import Nodo
from grafos import Problema


# Búsqueda en profundidad recursiva
def profundidad_recursiva(problema, limite=99999):
    raiz = crea_nodo_raiz(problema)
    explorados = set()
    return __bpp_recursiva(raiz, problema, limite, explorados)


# Función para la búsqueda en profundidad recursiva
def __bpp_recursiva(nodo, problema, limite, explorados):
    if problema.es_objetivo(nodo.sala):
        return nodo
    if limite == 0:
        return None
    explorados.add(nodo.sala)
    if not nodo.acciones:
        return None
    for nombre_accion in nodo.acciones.keys():
        accion = Accion(nombre_accion)
        hijo = crea_nodo_hijo(problema, nodo, accion)
        if hijo.sala not in explorados:
            resultado = __bpp_recursiva(
                hijo, problema, limite-1, explorados.copy())
            if resultado:
                return resultado
    return None


# Función para profundidad iterativa, que va aumentando el límite de búsqueda hasta hallar la solución o llegar al límite establecido
def profundidad_iterativa(problema, limite):
    if limite is None:
        return profundidad_recursiva(problema)
    for i in range(1, limite+1):
        resultado = profundidad_recursiva(problema, i)
        if resultado:
            return resultado
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
solucion = profundidad_recursiva(problema_resolver, 10)
muestra_solucion(solucion)
