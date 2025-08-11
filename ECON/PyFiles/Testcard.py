Sets = []
for E in range (1,3):
    for M in range(E,E+2):
        for H in range(M+1,M+3):
            for N in range (1,3):
                for O in range(N,N+2):
                    for S in range(O+1,O+4):
                        Comb = [E,M,H,N,O,S]
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
                        Comb.append(MaxDiff)
                        Comb.append(RealDiff)
                        Sets.append(Comb)



print(Sets)
