import csv

# Prepare list to store combinations
all_combinations = []

for E in range(1, 3):
    for M in range(E+1, E+3):
        for H in range(M+1, M+3):
            for N in range(1, 3):
                for O in range(N, N+2):
                    for S in range(N+1, N+4):
                        
                        Comb = [E, M, H, N, O, S]
                        
                        MaxSpend= 5*(4*N+4*O+S)
                        MaxAcc= 25*H
                        RealSpend= 5*(3*N+3*O+S)
                        RealAcc= 5*E+15*M+5*H

                        Comb.append(MaxAcc)
                        Comb.append(RealAcc)
                        Comb.append(MaxSpend)
                        Comb.append(RealSpend)
                      
                        MaxDiff = round((MaxAcc-MaxSpend)/((MaxSpend+MaxAcc)/2)*100,1)
                        RealDiff = round((RealAcc-RealSpend)/((RealSpend+MaxAcc)/2)*100,1)
                        if RealAcc-RealSpend<0 or MaxAcc-MaxSpend<0 :
                            Under = "Under"
                        else:
                            Under = "Alright"
        
                        Comb.append(MaxDiff)
                        Comb.append(RealDiff)
                        Comb.append(Under)

                        all_combinations.append(Comb)

# Check how many
print(f"Total combinations: {len(all_combinations)}")

# Write to CSV
with open('mathic_combinations2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Easy", "Medium", "Hard", "Number", "Operation", "Special","MaxAcc","RealAcc","MaxSpend","RealSpend","MaxDiff","RealDiff","Under"])
    writer.writerows(all_combinations)


