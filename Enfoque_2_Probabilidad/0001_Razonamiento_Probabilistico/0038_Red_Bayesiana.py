# Red Bayesiana
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = DiscreteBayesianNetwork([
    ('Cold', 'Cough'),
    ('Cold', 'Fever')
])

cpd_cold = TabularCPD(
    variable='Cold', 
    variable_card=2, 
    values=[[0.9], [0.1]]  
)

cpd_cough_given_cold = TabularCPD(
    variable='Cough', 
    variable_card=2, 
    values=[[0.8, 0.1], [0.2, 0.9]],  
    evidence=['Cold'], 
    evidence_card=[2]
)

cpd_fever_given_cold = TabularCPD(
    variable='Fever', 
    variable_card=2, 
    values=[[0.7, 0.2], [0.3, 0.8]], 
    evidence=['Cold'], 
    evidence_card=[2]
)

model.add_cpds(cpd_cold, cpd_cough_given_cold, cpd_fever_given_cold)

# Validate the model
assert model.check_model()

print("Bayesian Network structure and CPDs have been defined and validated.")

infer = VariableElimination(model)

query_result_1 = infer.query(variables=['Cold'], evidence={'Cough': 1})
print("P(Cold | Cough) =\n", query_result_1)

query_result_2 = infer.query(variables=['Cold'], evidence={'Cough': 1, 'Fever': 1})
print("P(Cold | Cough, Fever) =\n", query_result_2)
