from pulp import *

# Define the problem
prob = LpProblem("MathscryptionBalance", LpMinimize)

# Variables
E = LpVariable("E", lowBound=1, upBound=2, cat='Integer')
M = LpVariable("M", lowBound=2, upBound=3, cat='Integer')
H = LpVariable("H", lowBound=3, upBound=5, cat='Integer')

N = LpVariable("N", lowBound=1, upBound=3, cat='Integer')
O = LpVariable("O", lowBound=1, upBound=4, cat='Integer')
S = LpVariable("S", lowBound=2, upBound=5, cat='Integer')

# Realistic and max values
realistic_energy = 5*E + 15*M + 5*H
realistic_spend = 15*N + 10*O + 4*S


max_energy = 25*H
max_spend = 20*N + 15*O + 6*S

# Introduce a variable to model the absolute gap
GAP = LpVariable("GAP", lowBound=0, cat='Continuous')

# Set constraints for absolute value
prob += GAP >= realistic_energy - realistic_spend
prob += GAP >= realistic_spend - realistic_energy

# Additional game logic constraints
prob += O >= N
prob += M == E+1
prob += H == M+1
prob += S == O+2
#prob += realistic_energy >= realistic_spend
#prob += max_energy >= max_spend

# Objective: Minimize the absolute difference
prob += GAP

# Solve
prob.solve()

# Output
print("Status:", LpStatus[prob.status])
print(f"E (Easy energy) = {E.varValue}")
print(f"M (Medium energy) = {M.varValue}")
print(f"H (Hard energy) = {H.varValue}")
print(f"N (Number card cost) = {N.varValue}")
print(f"O (Operation card cost) = {O.varValue}")
print(f"S (Special card cost) = {S.varValue}")
print(f"Realistic Energy = {value(realistic_energy)}")
print(f"Realistic Spend = {value(realistic_spend)}")
print(f"Max Energy = {value(max_energy)}")
print(f"Max Spend = {value(max_spend)}")
print(f"Optimized GAP = {value(GAP)}")
