# Importar las clases de la base
from grafos import Accion
from grafos import Sala
from grafos import Nodo
from grafos import Problema


def a_estrella(problema):
    raiz = crea_nodo_raiz(problema)
    frontera = [raiz, ]
    explorados = set()
    while True:
        if not frontera:
            return None
        nodo = sacar_siguiente(
            frontera, 'valor', objetivos=problema.salas_objetivos)
        if problema.es_objetivo(nodo.sala):
            return nodo
        explorados.add(nodo.sala)
        if not nodo.acciones:
            continue
        for nombre_accion in nodo.acciones.keys():
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            salas_frontera = [nodo.sala for nodo in frontera]
            if hijo.sala in explorados or hijo.sala in salas_frontera:
                buscar = [nodo for nodo in frontera
                          if nodo.sala == hijo.sala]
                if buscar:
                    valores_hijo = [hijo.valores[objetivo.nombre]
                                    for objetivo in problema.salas_objetivos]
                    valores_buscar = [buscar[0].valores[objetivo.nombre]
                                      for objetivo in problema.salas_objetivos]
                    minimo_hijo = min(valores_hijo)
                    minimo_buscar = min(valores_buscar)
                    if minimo_hijo < minimo_buscar:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            else:
                frontera.append(hijo)


def crea_nodo_raiz(problema):
    sala_raiz = problema.sala_inicial
    acciones_raiz = {}
    if sala_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[sala_raiz.nombre]
    raiz = Nodo(sala_raiz, acciones=acciones_raiz)
    raiz.coste = 0
    raiz.heuristicas = problema.heuristicas[sala_raiz.nombre]
    raiz.valores = dict(raiz.heuristicas.items())
    return raiz


def crea_nodo_hijo(problema, padre, accion, agregar=True):
    nueva_sala = problema.resultado(padre.sala, accion)
    acciones_nuevo = {}
    if nueva_sala.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nueva_sala.nombre]
    hijo = Nodo(nueva_sala, accion, acciones_nuevo)
    coste = padre.coste
    coste += problema.coste_accion(padre.sala, accion)
    hijo.coste = coste
    hijo.heuristicas = problema.heuristicas[hijo.sala.nombre]
    hijo.valores = {sala: heuristica + hijo.coste
                    for sala, heuristica
                    in hijo.heuristicas.items()}
    if agregar:
        hijo.padre = padre
        padre.hijos.append(hijo)
    return hijo


def sacar_siguiente(frontera, metrica='valor', criterio='menor', objetivos=None):
    if not frontera:
        return None
    mejor = frontera[0]
    for nodo in frontera[1:]:
        for objetivo in objetivos:
            if metrica == 'valor':
                valor_nodo = nodo.valores[objetivo.nombre]
                valor_mejor = mejor.valores[objetivo.nombre]
                if (criterio == 'menor' and
                   valor_nodo < valor_mejor):
                    mejor = nodo
                elif (criterio == 'mayor' and
                      valor_nodo > valor_mejor):
                    mejor = nodo
            elif metrica == 'heuristica':
                heuristica_nodo = nodo.heuristicas[objetivo.nombre]
                heuristica_mejor = mejor.heuristicas[objetivo.nombre]
                if (criterio == 'menor' and
                   heuristica_nodo < heuristica_mejor):
                    mejor = nodo
                elif (criterio == 'mayor' and
                      heuristica_nodo > heuristica_mejor):
                    mejor = nodo
            elif metrica == 'coste':
                if (criterio == 'menor' and
                   nodo.coste_camino < mejor.coste_camino):
                    mejor = nodo
                elif (criterio == 'mayor' and
                      nodo.coste_camino > mejor.coste_camino):
                    mejor = nodo
    frontera.remove(mejor)
    return mejor


def muestra_solucion(objetivo=None):
    if not objetivo:
        print("No hay solución")
        return
    nodo = objetivo
    while nodo:
        msg = "Sala {0}, Valor {1}"
        sala = nodo.sala.nombre
        valores = [nodo.valores[objetivo.nombre]
                   for objetivo
                   in problema_resolver.salas_objetivos]
        valor = min(valores)
        print(msg.format(sala, valor))
        msg = "  Coste: {0}"
        coste_total = nodo.coste
        print(msg.format(coste_total))
        msg = "  Heurística: {0}"
        heuristicas_objetivos = [nodo.heuristicas[objetivo.nombre]
                                 for objetivo
                                 in problema_resolver.salas_objetivos]
        heuristica = min(heuristicas_objetivos)
        print(msg.format(heuristica))
        if nodo.accion:
            accion = nodo.accion.nombre
            padre = nodo.padre.sala
            coste = problema_resolver.coste_accion(padre, nodo.accion)
            if accion:
                msg = "<--- {0} [{1}] ---"
                print(msg.format(accion, coste))
        nodo = nodo.padre

# Declaraciones, comenzando con las acciones
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

# Declarar qué movimientos llevan a qué salas
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

# Distancias de sala a sala medido en línea recta
    heuristicas = {'Recepción': {'Recepción': 0,
                                'Sala de espera': 5,
                                'Sala de espera B': 11.18,
                                'Pasillo sección A': 14.14,
                                'Pasillo sección B': 18.03,
                                'Pasillo sección C': 22.36,
                                'Pasillo de almacén': 5,
                                'Almacén': 11.18,
                                'Sala de examen 1': 15.81,
                                'Rehabilitación B': 15,
                                'Sala de examen 2': 15.81,
                                'Rehabilitación': 20,
                                'Oficina': 21.21,
                                'Acceso a azotea': 15.81},
                  'Sala de espera': {'Recepción': 5,
                                     'Sala de espera': 0,
                                     'Sala de espera B': 10,
                                     'Pasillo sección A': 11.18,
                                     'Pasillo sección B': 14.14,
                                     'Pasillo sección C': 18.03,
                                     'Pasillo de almacén': 7.07,
                                     'Almacén': 7.07,
                                     'Sala de examen 1': 11.18,
                                     'Rehabilitación B': 10,
                                     'Sala de examen 2': 11.18,
                                     'Rehabilitación': 15,
                                     'Oficina': 18.03,
                                     'Acceso a azotea': 15},
                  'Sala de espera B': {'Recepción': 11.18,
                                       'Sala de espera': 10,
                                       'Sala de espera B': 0,
                                       'Pasillo sección A': 5,
                                       'Pasillo sección B': 10,
                                       'Pasillo sección C': 15,
                                       'Pasillo de almacén': 15.81,
                                       'Almacén': 15.81,
                                       'Sala de examen 1': 18.03,
                                       'Rehabilitación B': 14.14,
                                       'Sala de examen 2': 11.18,
                                       'Rehabilitación': 18.03,
                                       'Oficina': 11.18,
                                       'Acceso a azotea': 5},
                  'Pasillo sección A': {'Recepción': 14.14,
                                        'Sala de espera': 11.18,
                                        'Sala de espera B': 5,
                                        'Pasillo sección A': 0,
                                        'Pasillo sección B': 5,
                                        'Pasillo sección C': 10,
                                        'Pasillo de almacén': 18.03,
                                        'Almacén': 15,
                                        'Sala de examen 1': 15.81,
                                        'Rehabilitación B': 11.18,
                                        'Sala de examen 2': 7.07,
                                        'Rehabilitación': 14.14,
                                        'Oficina': 7.07,
                                        'Acceso a azotea': 7.07},
                  'Pasillo sección B': {'Recepción': 18.03,
                                        'Sala de espera': 14.14,
                                        'Sala de espera B': 10,
                                        'Pasillo sección A': 5,
                                        'Pasillo sección B': 0,
                                        'Pasillo sección C': 5,
                                        'Pasillo de almacén': 21.21,
                                        'Almacén': 15.81,
                                        'Sala de examen 1': 15,
                                        'Rehabilitación B': 10,
                                        'Sala de examen 2': 5,
                                        'Rehabilitación': 11.18,
                                        'Oficina': 5,
                                        'Acceso a azotea': 11.18},
                  'Pasillo sección C': {'Recepción': 22.36,
                                        'Sala de espera': 18.03,
                                        'Sala de espera B': 15,
                                        'Pasillo sección A': 10,
                                        'Pasillo sección B': 5,
                                        'Pasillo sección C': 0,
                                        'Pasillo de almacén': 25,
                                        'Almacén': 18.03,
                                        'Sala de examen 1': 15.81,
                                        'Rehabilitación B': 11.18,
                                        'Sala de examen 2': 7.07,
                                        'Rehabilitación': 5,
                                        'Oficina': 7.07,
                                        'Acceso a azotea': 15.81},
                  'Pasillo de almacén': {'Recepción': 5,
                                         'Sala de espera': 7.07,
                                         'Sala de espera B': 15.81,
                                         'Pasillo sección A': 18.03,
                                         'Pasillo sección B': 21.21,
                                         'Pasillo sección C': 25,
                                         'Pasillo de almacén': 0,
                                         'Almacén': 10,
                                         'Sala de examen 1': 15,
                                         'Rehabilitación B': 15.81,
                                         'Sala de examen 2': 18.03,
                                         'Rehabilitación': 20.62,
                                         'Oficina': 25,
                                         'Acceso a azotea': 20.62},
                  'Almacén': {'Recepción': 11.18,
                              'Sala de espera': 7.07,
                              'Sala de espera B': 15.81,
                              'Pasillo sección A': 15,
                              'Pasillo sección B': 15.81,
                              'Pasillo sección C': 18.03,
                              'Pasillo de almacén': 10,
                              'Almacén': 0,
                              'Sala de examen 1': 5,
                              'Rehabilitación B': 7.07,
                              'Sala de examen 2': 11.18,
                              'Rehabilitación': 11.18,
                              'Oficina': 22.36,
                              'Acceso a azotea': 20.62},
                  'Sala de examen 1': {'Recepción': 15.81,
                                       'Sala de espera': 11.18,
                                       'Sala de espera B': 18.03,
                                       'Pasillo sección A': 15.81,
                                       'Pasillo sección B': 15,
                                       'Pasillo sección C': 15.81,
                                       'Pasillo de almacén': 15,
                                       'Almacén': 5,
                                       'Sala de examen 1': 0,
                                       'Rehabilitación B': 5,
                                       'Sala de examen 2': 10,
                                       'Rehabilitación': 7.07,
                                       'Oficina': 20,
                                       'Acceso a azotea': 22.36},
                  'Rehabilitación B': {'Recepción': 15,
                                       'Sala de espera': 10,
                                       'Sala de espera B': 14.14,
                                       'Pasillo sección A': 11.18,
                                       'Pasillo sección B': 10,
                                       'Pasillo sección C': 11.18,
                                       'Pasillo de almacén': 15.81,
                                       'Almacén': 7.07,
                                       'Sala de examen 1': 5,
                                       'Rehabilitación B': 0,
                                       'Sala de examen 2': 5,
                                       'Rehabilitación': 5,
                                       'Oficina': 15,
                                       'Acceso a azotea': 18.03},
                  'Sala de examen 2': {'Recepción': 15.81,
                                       'Sala de espera': 11.18,
                                       'Sala de espera B': 11.18,
                                       'Pasillo sección A': 7.07,
                                       'Pasillo sección B': 5,
                                       'Pasillo sección C': 7.07,
                                       'Pasillo de almacén': 18.03,
                                       'Almacén': 11.18,
                                       'Sala de examen 1': 10,
                                       'Rehabilitación B': 5,
                                       'Sala de examen 2': 0,
                                       'Rehabilitación': 7.07,
                                       'Oficina': 10,
                                       'Acceso a azotea': 14.14},
                  'Rehabilitación': {'Recepción': 20,
                                     'Sala de espera': 15,
                                     'Sala de espera B': 18.03,
                                     'Pasillo sección A': 14.14,
                                     'Pasillo sección B': 11.18,
                                     'Pasillo sección C': 5,
                                     'Pasillo de almacén': 20.62,
                                     'Almacén': 11.18,
                                     'Sala de examen 1': 7.07,
                                     'Rehabilitación B': 5,
                                     'Sala de examen 2': 7.07,
                                     'Rehabilitación': 0,
                                     'Oficina': 7.07,
                                     'Acceso a azotea': 18.03},
                  'Oficina': {'Recepción': 21.21,
                              'Sala de espera': 18.03,
                              'Sala de espera B': 11.18,
                              'Pasillo sección A': 7.07,
                              'Pasillo sección B': 5,
                              'Pasillo sección C': 7.07,
                              'Pasillo de almacén': 25,
                              'Almacén': 22.36,
                              'Sala de examen 1': 20,
                              'Rehabilitación B': 15,
                              'Sala de examen 2': 10,
                              'Rehabilitación': 7.07,
                              'Oficina': 0,
                              'Acceso a azotea': 10},
                  'Acceso a azotea': {'Recepción': 15.81,
                                      'Sala de espera': 15,
                                      'Sala de espera B': 5,
                                      'Pasillo sección A': 7.07,
                                      'Pasillo sección B': 11.18,
                                      'Pasillo sección C': 15.81,
                                      'Pasillo de almacén': 20.62,
                                      'Almacén': 20.62,
                                      'Sala de examen 1': 22.36,
                                      'Rehabilitación B': 18.03,
                                      'Sala de examen 2': 14.14,
                                      'Rehabilitación': 18.03,
                                      'Oficina': 7.07,
                                      'Acceso a azotea': 0}}

# Crear problemas para probar el algoritmo, por ejemplo moverse desde la recepción hasta la oficina
objetivo_1 = [office]
problema_1 = Problema(reception, objetivo_1, acciones, costes, heuristicas)

objetivo_2 = [rehab_b]
problema_2 = Problema(reception, objetivo_2, acciones, costes, heuristicas)

objetivo_3 = [storage, exam2]
problema_3 = Problema(reception, objetivo_3, acciones, costes, heuristicas)

# Definir qué problema deseamos resolver
problema_resolver = problema_1

# Realizar la solución y mostrarla
solucion = a_estrella(problema_resolver)
muestra_solucion(solucion)
