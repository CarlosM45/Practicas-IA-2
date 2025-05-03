from os import system

# Definimos los resultados y sus respectivas utilidades y probabilidades
resultados = {
    'A': {'utilidad': 80, 'probabilidad': 0.5},
    'B': {'utilidad': 50, 'probabilidad': 0.3},
    'C': {'utilidad': 20, 'probabilidad': 0.2},
}

# Función para calcular la utilidad esperada
def calcular_utilidad_esperada(resultados):
    utilidad_esperada = 0
    for resultado, datos in resultados.items():
        utilidad_esperada += datos['probabilidad'] * datos['utilidad']
    return utilidad_esperada

# Calcular y mostrar la utilidad esperada
system('cls')
utilidad_esperada = calcular_utilidad_esperada(resultados)
print(f"Utilidad Esperada: {utilidad_esperada}")