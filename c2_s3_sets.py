
# Sets 
# 1. Mutable
# 2. All elements should be unique
# 3. Imutable elements in the sets - str, int, float, tuple
# 4. Unordered  (no indexing and slicing operations on the sets )

s = {10,20,30,40,10,20,30,40,10,20,30,40}
print(s, type(s))

s1 = {100,200,300,400}
s1.add(500)
print(s1)


# Union
# Intersection
# Difference
# Symmetric difference

s2 = {10,20,30,40,50,60}
s3 = {40,50,60,70,80,90}

s4 = s2.union(s3)   # duplicate elements will only be present once
print(s4)

s5 = s2.intersection(s3)
print(s5)

s6 = s2.difference(s3)  # {10, 20, 30}
print(s6)
s6 = s3.difference(s2)  # {80, 90, 70}
print(s6)

s7 = s2.symmetric_difference(s3)    # {70, 10, 80, 20, 90, 30}
print(s7)

#print(s2)   # {40, 10, 50, 20, 60, 30}
#s2.update(s3)
#print(s2)   # {70, 40, 10, 80, 50, 20, 90, 60, 30}

#s2.intersection_update(s3)  
#print(s2)   # {40, 50, 60}

#s2.difference_update(s3)
#print(s2)   # {10, 20, 30}

s2.symmetric_difference(s3)
print(s2)   # {40, 10, 50, 20, 60, 30}

s8 = {100,200,300,400,500,600}
s9 = {100,200,300,400}
print(s9.issubset(s8))
print(s8.issuperset(s9))


# ---

l = [10,20,30,40,50,60,30,40,50,60,70]
s = set(l)
print(s,type(s))

# ---

l1 = [100,200,300,400,500]
l2 = [40,20,200,350,500,10,25,30,400,600,500]
# print the unique ordered elements

s1 = set(l1)
s2 = set(l2)

s3 = s1.union(s2)
print(s3)

l3 = list(s3)
print(l3)

l3.sort()
print(l3)

# OR 

l4 = sorted(s3)
print(l4)



# pop 
# remove 
# discard 
# clear 
# del 

r = s3.pop()
print(s3, r)

# r = s3.pop(100) # TypeError: pop() takes no arguments (1 given)
s3.remove(100)
print(s3)   # {200, 40, 10, 300, 400, 500, 20, 600, 25, 30}

#s3.remove(10000)    # KeyError: 10000

s3.discard(300)
print(s3)   #       {200, 40, 10, 400, 500, 20, 600, 25, 30}
s3.discard(10000)    # does nothing
print(s3)   # {200, 40, 10, 400, 500, 20, 600, 25, 30}


s3.clear()
print(s3)   # set()

del s3 
#print(s3)   # NameError: name 's3' is not defined

