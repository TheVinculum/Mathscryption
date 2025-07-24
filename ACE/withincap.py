import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ----------- SETTINGS -----------

numcards = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
opcards1 = ['+', '-', '/', '*', '']
opcards2 = ['+', '-', '/', '*']
TurnCount = 1
numlimit = 4
lowcap = 0
highcap = 120
primeactive=0
# ----------- MODULES -----------


def exprgen(numlimit):
    answer = 0
    while answer<1 or answer>100:
        op = '0'
        expr = ''

        for i in range(numlimit):
            num = random.choice(numcards)
            expr += num
                
            if i < (numlimit-1):
                if op is None or num == '10' or op == '':
                    op = random.choice(opcards2)
                else:
                    op = random.choice(opcards1)
                    
                expr += op
        answer = int(eval(expr)) 
    return expr

for j in range (10):
    expr = (exprgen(4))
    answer = int(eval(expr))
    print(answer)

