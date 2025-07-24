SqubeList = [1, 2, 4, 8, 9, 16, 25, 27, 36, 49, 64, 81]
numbers = [25,33,4]
answer = 25

def Squbes (val, numlist):
    digsum = 0
    for num in numlist:
      if num in SqubeList:
        digsum += num//10 + num%10 
    
    if digsum > 0:
        print(val)
   
Squbes(answer, numbers)
