import numpy as np
from os import system

# Estrategias de los jugadores
strategies = ['Cooperar', 'Defraudar']

# Matriz de pagos: (Jugador 1, Jugador 2)
#                  | Jugador 2
#                C  |  D
#          C | (3,3) | (0,5)
# Jugador 1  ------------
#          D | (5,0) | (1,1)

payoffs = np.array([
    [[3, 3], [0, 5]],  # Jugador 1 coopera
    [[5, 0], [1, 1]]   # Jugador 1 defrauda
])

def find_nash_equilibrium(payoffs):
    nash_equilibria = []
    for i in range(len(strategies)):
        for j in range(len(strategies)):
            payoff = payoffs[i][j]
            # Verificar si es un equilibrio de Nash
            if (payoff[0] >= payoffs[1-i][j][0]) and (payoff[1] >= payoffs[i][1-j][1]):
                nash_equilibria.append((strategies[i], strategies[j]))
    return nash_equilibria

system('cls')
nash_equilibria = find_nash_equilibrium(payoffs)
print("Equilibrios de Nash:", nash_equilibria)