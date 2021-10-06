# LIST COMPREHENSION - useful when i want to perform the same operation on each element inside an iterable structure


#EXAMPLE 1
# You have a list
l1 = [10,20,30,40,50]
print(l1)
# And you want a second list containing the square of each value in l1

# Sol 1: (write a loop)
l2 = []
for val in l1:
    l2.append( val*val )

print(l2)

#Sol 2: (comprehension)
l3 = [ val*val for val in l1 ]
print(l3)


# EXAMPLE 2
#You have a list of numbers and you only want the even ones
l = [10,20,25,30,35,40,45,55,66,80]

l4 = [value for value in l if value%2 == 0]
print(l4)



# EXAMPLE 3
# You have a list of strings and you want another list containing the length of each string in the first list
l = ["prune", "pere", "mere", "portocale", "banane"]

l5 = [ len(val) for val in l ]
print(l5)


# Example 4
# Nested for loop in comprehension: create a list of random tuples
l6 = [ (val1,val2) for val1 in range(1,5) for val2 in range(100,103) ]
print(l6)


# EXAMPLE 5
# You have a list of lists and want to output a single list containing all the elements of all the lists mentioned
# In:  [[1,2,3],[4,5,6,7],[8,9]]
# Out: [1,2,3,4,5,6,7,8,9]
l1 = [[1,2,3],[4,5,6,7],[8,9]]

l2 = [ elem for listx in l1 for elem in listx ]
print("In:  ",l1)
print("Out: ", l2)



# EXAMPLE 6
l1 = [100,11,165,210,20,60,645645,64,6,84,684,64,45,6321]
l2 = [ "Ëven" if val%2==0 else "Odd" for val in l1 ]
print(l2)


# EXAMPLE 7
d1 = { val:val**2 for val in range(1,11) }
print(d1)



# EXAMPLE 8
# a:97, b:98, c:99, ... z:122
d2 = { chr(val):val for val in range(97,123) }
print(d2)
