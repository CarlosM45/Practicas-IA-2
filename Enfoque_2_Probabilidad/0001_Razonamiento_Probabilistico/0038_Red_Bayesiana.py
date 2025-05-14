# Red Bayesiana
from pgmpy.models import DiscreteBayesianNetwork # Clase para crear una red bayesiana discreta
from pgmpy.factors.discrete import TabularCPD # Clase para crear una CPD (Distribución de Probabilidad Condicional)
from pgmpy.inference import VariableElimination # Algoritmo de inferencia para redes bayesianas

# Definir la estructura de la red bayesiana con los tres nodos Cold, Cough y Fever y sus relaciones
model = DiscreteBayesianNetwork([
    ('Cold', 'Cough'),
    ('Cold', 'Fever')
])

cpd_cold = TabularCPD(
    variable='Cold', 
    variable_card=2, # Número de estados
    values=[[0.9], [0.1]]  # Probabilidad de que no haya resfriado (0.9) y de que sí haya resfriado (0.1)
)

cpd_cough_given_cold = TabularCPD(
    variable='Cough', 
    variable_card=2, 
    values=[[0.8, 0.1], [0.2, 0.9]],  # Probabilidad de toser dado que no hay resfriado (0.8) y dado que sí hay resfriado (0.2)
    # y la probabilidad de no toser dado que no hay resfriado (0.1) y dado que sí hay resfriado (0.9)
    evidence=['Cold'], # La variable que condiciona la probabilidad
    evidence_card=[2] # Número de estados de la variable que condiciona
)

cpd_fever_given_cold = TabularCPD(
    variable='Fever', 
    variable_card=2, 
    values=[[0.7, 0.2], [0.3, 0.8]], # Probabilidad de fiebre dado que no hay resfriado (0.7) y dado que sí hay resfriado (0.3)
    # y la probabilidad de no tener fiebre dado que no hay resfriado (0.2) y dado que sí hay resfriado (0.8)
    evidence=['Cold'],
    evidence_card=[2]
)

model.add_cpds(cpd_cold, cpd_cough_given_cold, cpd_fever_given_cold) # Agregar las CPDs al modelo

# Validar el modelo, verificando que la red esté correctamente definida y que las CPDs sean consistentes con la estrucura de la red
assert model.check_model()

print("Bayesian Network structure and CPDs have been defined and validated.")

infer = VariableElimination(model) # Crear un objeto de inferencia para la red bayesiana

query_result_1 = infer.query(variables=['Cold'], evidence={'Cough': 1}) # Preguntar por la probabilidad de tener resfriado dado que se tiene tos
print("P(Cold | Cough) =\n", query_result_1)

query_result_2 = infer.query(variables=['Cold'], evidence={'Cough': 1, 'Fever': 1}) # Preguntar por la probabilidad de tener resfriado dado que se tiene tos y fiebre
print("P(Cold | Cough, Fever) =\n", query_result_2)
