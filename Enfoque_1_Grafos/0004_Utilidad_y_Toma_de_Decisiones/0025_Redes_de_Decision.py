from os import system

# Definimos los resultados y sus respectivas probabilidades
inversiones = {
    'A': {'ganancia': 200, 'probabilidad_ganancia': 0.6, 'perdida': -100, 'probabilidad_perdida': 0.4},
    'B': {'ganancia': 150, 'probabilidad_ganancia': 0.7, 'perdida': -50, 'probabilidad_perdida': 0.3},
}

# Función para calcular la utilidad esperada
def calcular_utilidad_esperada(inversiones):
    utilidad_esperada = {}
    for inversion, datos in inversiones.items():
        utilidad_esperada[inversion] = (
            datos['probabilidad_ganancia'] * datos['ganancia'] +
            datos['probabilidad_perdida'] * datos['perdida']
        )
    return utilidad_esperada

# Calcular y mostrar la utilidad esperada
system('cls')
utilidad_esperada = calcular_utilidad_esperada(inversiones)
print("Utilidad Esperada de Inversiones:")
for inversion, utilidad in utilidad_esperada.items():
    print(f"{inversion}: {utilidad}")