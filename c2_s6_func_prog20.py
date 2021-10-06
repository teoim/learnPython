#
# MAP, FILTER, LAMBDA FUNCTIONS
# Solve the ame type of problems as comprehension, only much faster, using map, filter and lambda functions
#

# EXAMLPLE 1 - MAP
# YOU HAVE A LIST AND YOU DEFINED A sqr() FUNCTION
# l = [10,20,30,40,50,60]
# map(sqr,l)  maps each element of the list to the sqr() function


def sqr(x):
    return x**2

l = [10,20,30,40,50,60]

result = map(sqr,l)

for elem in result:
    print(elem)


result2 = list( map(sqr,l) )

print(result2)



# EXAMPLE 2

def add(x,y):
    return x+y

l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11,22,33,44,55,66,77,88,99,100]

result = list( map(add,l1,l2) )
print(result)



# When you have to filter elements from a list, you can't use map, you need to use filter
# Example: when you need to find odd or even elements

def check_num(num):
    return num%2==0

l = [1,2,3,4,5,6,7,8,9,10,11]

res = list( filter(check_num,l) )       #  [2, 4, 6, 8, 10]
print(res)

res2 = list( map(check_num,l) )       #  [False, True, False, True, False, True, False, True, False, True, False]
print(res2)



# LAMBDA FUNCTIONS : anonymous functions
# Use these when you have a small piece of code that you don't need to recall in multiple places

# Example 1 : get square of elements in a list
l = [10,20,30,40,50,60]

result2 = list( map( lambda elem:elem**2, l) )  # you can't perform assignment operations or (explicit) return operations with lambda

print(result2)

# Example 2 : get even/odd numbers in a list
l = [1,2,3,4,5,6,7,8,9,10,11]

res = list( map( lambda num1:num1**2 , l ) )       #  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
print(res)

# Example 3 : check wether the numeric elements of the list are odd / even (return False / True )

res = list( map( lambda num1:num1%2==0 , l ) )  # [False, True, False, True, False, True, False, True, False, True, False]
print(res)


# Example 4 : sorting a dictionaries on the base of values

d = { 1:50, 2: 30, 3:70, 4:10, 5: 40 }

#l = sorted(d)   # [1, 2, 3, 4, 5]
#l = sorted(d.items())   # [(1, 50), (2, 30), (3, 70), (4, 10), (5, 40)]    --> soreted based on keys, not values
#l = sorted(d.items(), key = lambda x:x[1])  # [(4, 10), (2, 30), (5, 40), (1, 50), (3, 70)] --> x[0] = keys; x[1] = values
l = dict(sorted(d.items(), key = lambda x:x[1]))    # {4: 10, 2: 30, 5: 40, 1: 50, 3: 70}  --> i can cast it to a dictionary if i need to
print(l)
