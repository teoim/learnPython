#
# GENERATORS
# Usages: generate a very long list of prime numbers or fibonaci numbers, etc.
# generator functions (unlike normal functions) are functions that maintain the state of the functions and return one value at a time
# - very helpful for sparing memory usage

# Example of normal function:
def printVals(l):
    for val in l:
        print(val)

l = [1,2,3,4,5,6,7,8,9]
printVals(l)


# EXAMPLES OF GENERATOR functions

# Example 1 : fibonaci
def fibo():
    first_num = 0
    second_num = 1
    while(True):
        last_num = first_num + second_num
        yield last_num      # yield ... means this is a generator function
        first_num,second_num = second_num,last_num

g = fibo()  # Doesn't really execute the function
print(g)    # <generator object fibo at 0x0000008884B1FBA0>

# Each next(g) executes the function up to yield, returns the result and mantains the state of the function for the next execution
print("1",next(g)) # 1  stops at the first yield and returns the first result
print("2",next(g)) # 2  continues from the next line after the first yield (and stops at the next yield if the case)
print("3",next(g)) # 3
print("4",next(g)) # 5

for val in range(5,10):
    print(val, next(g))

for val in range(10):
    print(9+val, next(g))



# Example 2 : generators applied to a normal function
def printVals(l):
    for val in l:
        #print(val)
        yield val

l = [1,2,3,4,5,6]
x = printVals(l)
print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4
print(next(x))  # 5
print(next(x))  # 6
# print(next(x))  # StopIteration exception - must handle this with a try block


# Example 3
l = [1, 2, 3, 4, 5]
l2 = [ val*val for val in l ]
print(l2)   # [1, 4, 9, 16, 25]

l3 = (val*val for val in l)     # Round parenthesis are used to create generators
print(l3)   # <generator object <genexpr> at 0x000000266DDAF890>

print(next(l3)) # 1
print(next(l3)) # 4
print(next(l3)) # 9
print(next(l3)) # 16
print(next(l3)) # 25
