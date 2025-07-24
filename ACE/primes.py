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
primeactive=0
# ----------- MODULES -----------

def numextract(str):
    
    exp=str
    
    for symbol in opcards2:
        exp = exp.replace(symbol, ',')
    
    return exp.split(',')

def exprgen(numlimit):
    answer = 0
    while answer<1 or answer>100:
        op = '0'
        expr = ''

        for i in range(numlimit):
            num = random.choice(numcards)
            expr += num
                
            if i < (numlimit-1):
                if num == '10' or op == '':
                    op = random.choice(opcards2)
                else:
                    op = random.choice(opcards1)    
                expr += op
        answer = int(eval(expr)) 
    return expr

def primes(expr, nums):
    primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primemult = 0
    val = eval(expr)

    if val in primelist:
        primeactive += 1
        for num in nums:
            if num in primelist:
                primemult += 1

    print(val*primemult)

 
expr = (exprgen(4))
nums = numextract(expr)
primes(expr, nums)




