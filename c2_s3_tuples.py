
# TUPLES
# immutable data structure 
# ordered indexing and structure
# "very used especially when passing data between functions"

t = (10,20,20,20,30,30,40)
print(t,type(t))
#help(tuple)
#print(t[10])
print(t[:2])
print(t.index(20))
print(t.count(20))


# ---

l = [10,20,30,40,50,60]

for index,value in enumerate(l):
    print(index,value)

for t in enumerate(l):
    print(t)    # (index, value) tuple 

for t in enumerate(l):
    print(t[0])    # all indexes from the tuple 

for t in enumerate(l):
    print(t[1])    # all values from the tuple 


# Convert list to tuple

t = tuple(l)
print(l, type(l))
print(t, type(t))

# Convert tuple to list

l2 = list(t)
print(l2, type(l2))


# How does python pass tuples between functions?