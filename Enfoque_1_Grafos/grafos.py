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
    def __init__(self, sala_inicial, salas_objetivos, acciones, costes=None):
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
    waiting = Sala('Sala de espera', [accN, accS, accE])
    waiting_a = Sala('Pasillo sección A', [accN, accS, accO])
    waiting_b = Sala('Pasillo sección B', [accN, accS, accE, accO])
    waiting_c = Sala('Pasillo sección C', [accS, accO])
    storage_corridor = Sala('Pasillo de almacén', [accN, accE])
    storage = Sala('Almacén', [accN, accS, accE])
    exam1 = Sala('Sala de examen 1', [accS, accE])
    rehab_b = Sala('Rehabilitación B', [accN, accE, accO])
    exam2 = Sala('Sala de examen 2', [accE, accO])
    rehab = Sala('Rehabilitación', [accS, accE])
    office = Sala('Oficina', [accO])
    roof = Sala('Acceso a azotea', [accO])

# Declarar qué movimientos llevan a qué salas
    movimientos = {'Recepción': {'norte': waiting,
                                 'oeste': storage_corridor},
                   'Sala de espera': {'norte': waiting_a,
                                      'sur': reception,
                                      'este': roof},
                   'Pasillo sección A': {'norte': waiting_b,
                                         'sur': waiting,
                                         'oeste': storage},
                   'Pasillo sección B': {'norte': waiting_c,
                                         'sur': waiting_a,
                                         'este': office,
                                         'oeste': exam2},
                   'Pasillo sección C': {'sur': waiting_b,
                                         'oeste': rehab},
                   'Pasillo de almacén': {'norte': storage,
                                          'este': reception},
                   'Almacén': {'norte': exam1,
                               'sur': storage_corridor,
                               'este': waiting_a},
                   'Sala de examen 1': {'sur': storage,
                                        'este': rehab_b},
                   'Rehabilitación B': {'norte': rehab,
                                        'este': exam2,
                                        'oeste': exam1},
                   'Sala de examen 2': {'este': waiting_b,
                                        'oeste': rehab_b},
                   'Rehabilitación': {'sur': rehab_b,
                                      'este': waiting_c},
                   'Oficina': {'oeste': waiting_b},
                   'Acceso a azotea': {'oeste': waiting}}

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

# Creación de un problema (ir desde la recepción hasta la oficina)
problema_rec_off = Problema(reception, [office], movimientos, mts)
