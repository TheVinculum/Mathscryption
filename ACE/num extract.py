import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def numextract(str,op):
    exp=str
    for symbol in op:
        exp = exp.replace(symbol, ',')

    return exp.split(',')

# ----------- SETTINGS -----------
numcards = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
opcards1 = ['+', '-', '/', '*', '']
opcards2 = ['+', '-', '/', '*']

results = []
TurnCount = 1
numlimit = 4

for turns in range(TurnCount):
    op = None
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
    
    expnums = numextract(expr, opcards2)
    print(expnums)
    value = eval(expr)
    print(value)