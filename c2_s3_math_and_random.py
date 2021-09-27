
# Math and random

l = [10,20,30,40,50]
print(sum(l))
print(max(l))
print(min(l))

# print(sum(100,200,300))   # TypeError: sum() takes at most 2 arguments (3 given)

num = 25.555
print(round(num))   # 26
print(round(num,2))    # 25.55

#print(dir(__builtins__))
#help(__builtins__)




    # The MATH module

import math 
l = [0.1] * 10
print(l)
print(sum(l))        # expected 1.0, result: 0.9999999999999999
print(math.fsum(l))  # 1.0

num1 = 15.5559  # between 15 and 16
print(math.floor(num1), math.ceil(num1))    # 15 16

print( math.sqrt(25))   # 5.0 
print( math.factorial(5))   # 120 

num1 = 45.5556
print(math.modf(num1))  # (0.5555999999999983, 45.0)
decimalPart, integerPart = math.modf(num1)
print(decimalPart)  # 0.5555999999999983
print(integerPart)  # 45.0 

print(math.pow(10,2))   # 100.0 

print(math.log(10,2))   # base 2: 3.3219280948873626
print(math.log(10))     # base e: 2.302585092994046

print(math.log10(2))    # 0.3010299956639812    log of 2 base 10
print(math.log2(10))    # 3.321928094887362     log of 10 base 2

print(math.sin(math.radians(90)))   # 1 
print(math.cos(math.radians(180)))  # -1
print(math.tan(math.radians(45)))   # 0.9999999999999999

#help(math)  # documentation of the math module 
#print(dir(math))  # list of all functions in the math module 




    # The RANDOM module

import random

print( random.random()) # Generates a random number between 0 and 1 

l = [1,2,3,4,"HAHA",6,7,8,9,10]
print( random.choice(l))    # Chooses a random element from the list l 

print( random.randint(10,100))  # Generates a random number between 10 and 100
print( random.randrange(10,100))    # Generates a random number between 10 and 99

print( random.uniform(10,20))   # random float number in the 10 - 20 range : 19.244837047385936

#help(random) 
print( dir(random))