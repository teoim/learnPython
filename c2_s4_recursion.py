
# RECURSIVE FUNCTIONS
# 1. Factorial
# 2. Binary search


# 1. Define a function that returns the factorial of a number 

def factorial( num ):
    if (num == 1 or num == 0): return 1
    else: return num * factorial(num-1)

res = factorial(5)
print(res)
res = factorial(8)
print(res)
res = factorial(0)
print(res)
res = factorial(1)
print(res)
res = factorial(2)
print(res)
res = factorial(3)
print(res)
res = factorial(4)
print(res)




# 2. Binary search
# Define a function that, given an ordered list and a value, will check if the value is present in the list or not 

def bin_src( l, key):
    if len(l) == 0:     # if the key is not present, the alg will reach a point where the list is empty
        return False

    mid = len(l) // 2
    if key == l[ mid ]: return True
    elif key < l[ mid ]: return bin_src( l[:mid], key )
    else: return bin_src( l[ mid+1:], key )
# End bin_search(...)

l = [100,200,300,400,500,600,700,800,900,1000]

r = bin_src( l , 900 )
print( r )
r = bin_src( l , 100 )
print( r )
r = bin_src( l , 90 )
print( r )
r = bin_src( l , 550 )
print( r )
r = bin_src( l , 5550 )
print( r )
