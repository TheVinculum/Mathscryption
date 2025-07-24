import random
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import norm

# ----------- SETTINGS -----------

numcards = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
opcards1 = ['+', '-', '/', '*', '']
opcards2 = ['+', '-', '/', '*']
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
SqubeList = [1, 2, 4, 8, 9, 16, 25, 27, 36, 49, 64, 81]
Fibolist = [2, 3, 5, 8, 13, 21, 34, 55, 89]
Triggered = {"Prime": 0, "Fibo":0, "Sqube" : 0}
Scores = {"Prime":[],"Fibo":[],"Sqube":[]}
#TurnCount = 1
prevanswer = 0
numlimit = 4



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

def primes(val, numberlist):
    
    primemult = 0
    if val in primelist:
        Triggered['Prime'] += 1
        primemult = sum(1 for num in numberlist if num in primelist)
        Scores['Prime'].append(val*primemult)

def fibos (preval, val, numberlist):
    fibotriggered = False
    for item in numberlist:
        if item in Fibolist:
            fibotriggered = True
            break
    
    if fibotriggered:
        Triggered ['Fibo'] += 1
        val = val + preval
        Scores['Fibo'].append(val)

def Squbes (val, numlist):
    digsum = 0
    for num in numlist:
      if num in SqubeList:
        digsum += num//10 + num%10 
    
    if digsum > 0:
        Triggered['SqCube']
        

# ----------- MAIN -----------

for i in range (100):
    expr = (exprgen(4))
    answer = int(eval(expr))
    nums = [int(x) for x in numextract(expr)]
    fibos(prevanswer,answer, nums)
    primes(answer, nums)
    prevanswer = answer

print(Scores)
print(Triggered)


