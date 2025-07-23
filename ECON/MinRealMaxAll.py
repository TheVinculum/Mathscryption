from pulp import *

# Defining the problem and variables
prob = LpProblem("MathscryptionBalance", LpMinimize)

E = LpVariable("E", lowBound=1, upBound=3, cat='Integer')   #Easy Question
M = LpVariable("M", lowBound=2, upBound=4, cat='Integer')   #Med Question
H = LpVariable("H", lowBound=3, upBound=5, cat='Integer')   #Hard Question

N = LpVariable("N", lowBound=1, upBound=3, cat='Integer')   #Numbered Cards
O = LpVariable("O", lowBound=1, upBound=4, cat='Integer')   #Operation Notes
S = LpVariable("S", lowBound=1, upBound=5, cat='Integer')   #Special Cards

#Different player levels and extreme maximum value scenarios

Lev1_energy = 5*E + 15*M
Lev1_spend = 15*N + 10*O + 3*S

Lev2_energy = 5*E + 15*M + 5*H
Lev2_spend = 16*N + 11*O + 4*S

Lev3_energy = 15*M + 10*H
Lev3_spend = 18*N + 13*O + 5*S

Max_energy = 25*H
Max_spend = 20*N + 15*O + 6*S

# Introducing variables for accumultion-spending gaps for each level

LEV1GAP = LpVariable("LEV1GAP", lowBound=0, cat='Continuous')
LEV2GAP = LpVariable("LEV2GAP", lowBound=0, cat='Continuous')
LEV3GAP = LpVariable("LEV3GAP", lowBound=0, cat='Continuous')

# Set constraints for absolute value

prob += LEV1GAP >= Lev1_energy - Lev1_spend
prob += LEV1GAP >= Lev1_spend - Lev1_energy

prob += LEV2GAP >= Lev2_energy - Lev2_spend
prob += LEV2GAP >= Lev2_spend - Lev2_energy

prob += LEV3GAP >= Lev3_energy - Lev3_spend
prob += LEV3GAP >= Lev3_spend - Lev3_energy

#Question Energies constraints
prob += M == E+1
prob += H == M+1

#Card Prices contraint
prob += O <= N+1
prob += S == O+2

prob += Max_energy >= Max_spend


prob += LEV1GAP+LEV2GAP+LEV3GAP

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

print(f"LEVEL1 Energy = {value(Lev1_energy)}")
print(f"LEVEL1 Spend = {value(Lev1_spend)}")
print(f"LEVEL2 Energy = {value(Lev2_energy)}")
print(f"LEVEL2 Spend = {value(Lev2_spend)}")
print(f"LEVEL3 Energy = {value(Lev3_energy)}")
print(f"LEVEL3 Spend = {value(Lev3_spend)}")


print(f"LEVEL1 GAP = {value(LEV1GAP)}")
print(f"LEVEL2 GAP = {value(LEV2GAP)}")
print(f"LEVEL3 GAP = {value(LEV3GAP)}")

print(f"Optimized Average GAP = {value(LEV1GAP+LEV2GAP+LEV3GAP)}")
