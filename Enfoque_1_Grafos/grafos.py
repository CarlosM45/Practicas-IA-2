# Clase para los nombres de las acciones
class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# Clase para los nombres de las salas
class Sala:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

    def __str__(self):
        return self.nombre


# Clase para definir las funciones del problema, en este caso regresar si se llegó al objetivo y las acciones resultado
class Problema:
    def __init__(self, sala_inicial, salas_objetivos, acciones, costes=None, heuristicas=None):
        self.sala_inicial = sala_inicial
        self.salas_objetivos = salas_objetivos
        self.acciones = acciones
        self.costes = costes
        self.infinito = 99999
        if not self.costes:
            self.costes = {}
            for sala in self.acciones.keys():
                self.costes[sala] = {}
                for accion in self.acciones[sala].keys():
                    self.costes[sala][accion] = 1

    def __str__(self):
        msg = "Sala Inicial: {0} -> Objetivos: {1}"
        return msg.format(self.sala_inicial.nombre, self.salas_objetivos)

    def es_objetivo(self, sala):
        return sala in self.salas_objetivos

    def resultado(self, sala, accion):
        if sala.nombre not in self.acciones.keys():
            return None
        acciones_sala = self.acciones[sala.nombre]
        if accion.nombre not in acciones_sala.keys():
            return None
        return acciones_sala[accion.nombre]
    
    def coste_accion(self, sala, accion):
        if sala.nombre not in self.costes.keys():
            return self.infinito
        costes_sala = self.costes[sala.nombre]
        if accion.nombre not in costes_sala.keys():
            return self.infinito
        return costes_sala[accion.nombre]
    
    def coste_camino(self, nodo):
        total = 0
        while nodo.padre:
            total += self.coste_accion(nodo.padre.sala, nodo.accion)
            nodo = nodo.padre
        return total


# Clase que inicializa los nodos, con la función para expandirlos cuando se exploran
class Nodo:
    def __init__(self, sala, accion=None, acciones=None, padre=None):
        self.sala = sala
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijos = []
        self.coste = 0

    def __str__(self):
        return self.sala.nombre

    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.sala.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones = problema.acciones[self.sala.nombre]
        for accion in self.acciones.keys():
            accion_hijo = Accion(accion)
            nueva_sala = problema.resultado(self.sala, accion_hijo)
            acciones_nuevo = {}
            if nueva_sala.nombre in problema.acciones.keys():
                acciones_nuevo = problema.acciones[nueva_sala.nombre]
            hijo = Nodo(nueva_sala, accion_hijo, acciones_nuevo, self)
            coste = self.padre.coste if self.padre else 0
            coste += problema.coste_accion(self.sala, accion_hijo)
            hijo.coste = coste
            self.hijos.append(hijo)
        return self.hijos
    
    def hijo_mejor(self, problema):
        if not self.hijos:
            return None
        mejor = self.hijos[0]
        for hijo in self.hijos:
            for objetivo in problema.salas_objetivos:
                coste_camino_hijo = problema.coste_camino(hijo)
                coste_camino_mejor = problema.coste_camino(mejor)
                if coste_camino_hijo < coste_camino_mejor:
                    mejor = hijo
        return mejor


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
    pending = 0

# Declarar qué movimientos llevan a qué salas
    movimientos = {'Recepción': {'norte': waiting,
                                 'oeste': storage_corridor},
                   'Sala de espera': {'sur': reception,
                                      'este': waiting_b},
                    'Sala de espera B':{'norte':corridor_a},
                   'Pasillo sección A': {'norte': pending,
                                         'sur': pending,
                                         'oeste': pending},
                   'Pasillo sección B': {'norte': pending,
                                         'sur': pending,
                                         'este': office,
                                         'oeste': exam2},
                   'Pasillo sección C': {'sur': pending,
                                         'oeste': rehab},
                   'Pasillo de almacén': {'norte': storage,
                                          'este': reception},
                   'Almacén': {'norte': exam1,
                               'sur': storage_corridor,
                               'este': pending},
                   'Sala de examen 1': {'sur': storage,
                                        'este': rehab_b},
                   'Rehabilitación B': {'norte': rehab,
                                        'este': exam2,
                                        'oeste': exam1},
                   'Sala de examen 2': {'este': pending,
                                        'oeste': rehab_b},
                   'Rehabilitación': {'sur': rehab_b,
                                      'este': pending},
                   'Oficina': {'oeste': pending},
                   'Acceso a azotea': {'oeste': waiting_b}}

# Coste en metros promedio que toma realizar los movimientos
    mts = {'Recepción': {'norte': 5,
                         'oeste': 10},
           'Sala de espera': {'norte': 10,
                              'sur': 5,
                              'este': 15},
           'Pasillo sección A': {'norte': 5,
                                 'sur': 10,
                                 'oeste': 5},
           'Pasillo sección B': {'norte': 5,
                                 'sur': 5,
                                 'este': 5,
                                 'oeste': 5},
           'Pasillo sección C': {'sur': 5,
                                 'oeste': 5},
           'Pasillo de almacén': {'norte': 10,
                                  'este': 10},
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
                              'este': 5},
           'Oficina': {'oeste': 5},
           'Acceso a azotea': {'oeste': 15}}

# Distancias de sala a sala medido en línea recta
    distancias = {'Recepción': {'Recepción': 0,
                                'Sala de espera': 5,
                                'Pasillo sección A': 15,
                                'Pasillo sección B': 20,
                                'Pasillo sección C': 25,
                                'Pasillo de almacén': 10,
                                'Almacén': 14.14,
                                'Sala de examen 1': 18.03,
                                'Rehabilitación B': 15.81,
                                'Sala de examen 2': 15,
                                'Rehabilitación': 20.62,
                                'Oficina': 20.62,
                                'Acceso a azotea': 15.81},
                  'Sala de espera': {'Recepción': 5,
                                     'Sala de espera': 0,
                                     'Pasillo sección A': 10,
                                     'Pasillo sección B': 15,
                                     'Pasillo sección C': 20,
                                     'Pasillo de almacén': 11.18,
                                     'Almacén': 11.18,
                                     'Sala de examen 1': 14.14,
                                     'Rehabilitación B': 11.18,
                                     'Sala de examen 2': 10,
                                     'Rehabilitación': 15.81,
                                     'Oficina': 15.81,
                                     'Acceso a azotea': 15},
                  'Pasillo sección A': {'Recepción': 15,
                                        'Sala de espera': 10,
                                        'Pasillo sección A': 0,
                                        'Pasillo sección B': 5,
                                        'Pasillo sección C': 10,
                                        'Pasillo de almacén': 18.03,
                                        'Almacén': 0,
                                        'Sala de examen 1': 0,
                                        'Rehabilitación B': 0,
                                        'Sala de examen 2': 0,
                                        'Rehabilitación': 0,
                                        'Oficina': 0,
                                        'Acceso a azotea': 0},
                  'Pasillo sección B': {'Recepción': 20,
                                        'Sala de espera': 15,
                                        'Pasillo sección A': 5,
                                        'Pasillo sección B': 0,
                                        'Pasillo sección C': 0,
                                        'Pasillo de almacén': 0,
                                        'Almacén': 0,
                                        'Sala de examen 1': 0,
                                        'Rehabilitación B': 0,
                                        'Sala de examen 2': 0,
                                        'Rehabilitación': 0,
                                        'Oficina': 0,
                                        'Acceso a azotea': 0},
                  'Pasillo sección C': {'Recepción': 25,
                                        'Sala de espera': 20,
                                        'Pasillo sección A': 10,
                                        'Pasillo sección B': 0,
                                        'Pasillo sección C': 0,
                                        'Pasillo de almacén': 0,
                                        'Almacén': 0,
                                        'Sala de examen 1': 0,
                                        'Rehabilitación B': 0,
                                        'Sala de examen 2': 0,
                                        'Rehabilitación': 0,
                                        'Oficina': 0,
                                        'Acceso a azotea': 0},
                  'Pasillo de almacén': {'Recepción': 10,
                                         'Sala de espera': 11.18,
                                         'Pasillo sección A': 0,
                                         'Pasillo sección B': 0,
                                         'Pasillo sección C': 0,
                                         'Pasillo de almacén': 0,
                                         'Almacén': 0,
                                         'Sala de examen 1': 0,
                                         'Rehabilitación B': 0,
                                         'Sala de examen 2': 0,
                                         'Rehabilitación': 0,
                                         'Oficina': 0,
                                         'Acceso a azotea': 0},
                  'Almacén': {'Recepción': 14.14,
                              'Sala de espera': 11.18,
                              'Pasillo sección A': 0,
                              'Pasillo sección B': 0,
                              'Pasillo sección C': 0,
                              'Pasillo de almacén': 0,
                              'Almacén': 0,
                              'Sala de examen 1': 0,
                              'Rehabilitación B': 0,
                              'Sala de examen 2': 0,
                              'Rehabilitación': 0,
                              'Oficina': 0,
                              'Acceso a azotea': 0},
                  'Sala de examen 1': {'Recepción': 18.03,
                                       'Sala de espera': 14.14,
                                       'Pasillo sección A': 0,
                                       'Pasillo sección B': 0,
                                       'Pasillo sección C': 0,
                                       'Pasillo de almacén': 0,
                                       'Almacén': 0,
                                       'Sala de examen 1': 0,
                                       'Rehabilitación B': 0,
                                       'Sala de examen 2': 0,
                                       'Rehabilitación': 0,
                                       'Oficina': 0,
                                       'Acceso a azotea': 0},
                  'Rehabilitación B': {'Recepción': 15.81,
                                       'Sala de espera': 11.18,
                                       'Pasillo sección A': 0,
                                       'Pasillo sección B': 0,
                                       'Pasillo sección C': 0,
                                       'Pasillo de almacén': 0,
                                       'Almacén': 0,
                                       'Sala de examen 1': 0,
                                       'Rehabilitación B': 0,
                                       'Sala de examen 2': 0,
                                       'Rehabilitación': 0,
                                       'Oficina': 0,
                                       'Acceso a azotea': 0},
                  'Sala de examen 2': {'Recepción': 15,
                                       'Sala de espera': 10,
                                       'Pasillo sección A': 0,
                                       'Pasillo sección B': 0,
                                       'Pasillo sección C': 0,
                                       'Pasillo de almacén': 0,
                                       'Almacén': 0,
                                       'Sala de examen 1': 0,
                                       'Rehabilitación B': 0,
                                       'Sala de examen 2': 0,
                                       'Rehabilitación': 0,
                                       'Oficina': 0,
                                       'Acceso a azotea': 0},
                  'Rehabilitación': {'Recepción': 20.62,
                                     'Sala de espera': 15.81,
                                     'Pasillo sección A': 0,
                                     'Pasillo sección B': 0,
                                     'Pasillo sección C': 0,
                                     'Pasillo de almacén': 0,
                                     'Almacén': 0,
                                     'Sala de examen 1': 0,
                                     'Rehabilitación B': 0,
                                     'Sala de examen 2': 0,
                                     'Rehabilitación': 0,
                                     'Oficina': 0,
                                     'Acceso a azotea': 0},
                  'Oficina': {'Recepción': 20.62,
                              'Sala de espera': 15.81,
                              'Pasillo sección A': 0,
                              'Pasillo sección B': 0,
                              'Pasillo sección C': 0,
                              'Pasillo de almacén': 0,
                              'Almacén': 0,
                              'Sala de examen 1': 0,
                              'Rehabilitación B': 0,
                              'Sala de examen 2': 0,
                              'Rehabilitación': 0,
                              'Oficina': 0,
                              'Acceso a azotea': 0},
                  'Acceso a azotea': {'Recepción': 15.81,
                                      'Sala de espera': 15,
                                      'Pasillo sección A': 0,
                                      'Pasillo sección B': 0,
                                      'Pasillo sección C': 0,
                                      'Pasillo de almacén': 0,
                                      'Almacén': 0,
                                      'Sala de examen 1': 0,
                                      'Rehabilitación B': 0,
                                      'Sala de examen 2': 0,
                                      'Rehabilitación': 0,
                                      'Oficina': 0,
                                      'Acceso a azotea': 0}}

# Creación de un problema (ir desde la recepción hasta la oficina)
problema_rec_off = Problema(reception, [office], movimientos, mts)
