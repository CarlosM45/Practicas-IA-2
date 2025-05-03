from os import system

# Definimos los resultados y sus respectivas probabilidades
resultados = {
    'Resultado 1': {'ganancia': 100, 'probabilidad': 0.7},
    'Resultado 2': {'perdida': -50, 'probabilidad': 0.3},
}

# Función para calcular la utilidad esperada sin información
def utilidad_sin_informacion(resultados):
    utilidad_esperada = 0
    for resultado, datos in resultados.items():
        if 'ganancia' in datos:
            utilidad_esperada += datos['probabilidad'] * datos['ganancia']
        elif 'perdida' in datos:
            utilidad_esperada += datos['probabilidad'] * datos['perdida']
    return utilidad_esperada

# Función para calcular la utilidad esperada con información perfecta
def utilidad_con_informacion(ganancia):
    return ganancia  # Ya que se conoce con certeza el resultado

# Cálculo de la utilidad esperada sin información
U_sin_info = utilidad_sin_informacion(resultados)

# Supongamos que la información indica que se obtendrá el resultado 1
U_con_info = utilidad_con_informacion(resultados['Resultado 1']['ganancia'])

# Cálculo del valor de la información
valor_informacion = U_con_info - U_sin_info

# Mostrar resultados
system('cls')
print(f"Utilidad Esperada sin Información: {U_sin_info}")
print(f"Utilidad Esperada con Información Perfecta: {U_con_info}")
print(f"Valor de la Información: {valor_informacion}")