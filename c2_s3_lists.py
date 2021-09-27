# Lists
# 1. lists are mutable - add, update and delete
# 2. ordered indexing and slicing
# 3. heterogeneous data types 

l = [11, 22, 33, 44, "HTML", "CSS", "python", ["MYSQL", "GTM", "MONGO"]]
print(l, "\n", type(l), "\n", id(l))

print(l[0])
print(l[-1])
print(l[-1][1])

print(l[1:3])   # [22, 33]
print(l[::-1])  # reversed list 

print(id(l))    # 140493817876352
l = [1,2,3,4,5,6,7,8,9,10]
for elem in l[::2]:
    print(elem)     # will print every 2 elements

# append()
# extend()
# insert()
print(id(l))    # 140493817148160
l.append(600)
print(l)
print(id(l))    # 140493817148160

num1 = 1
print(id(num1)) # 140456111961376
print(id(l[0])) # 140456111961376   # "lists store references of the values"

l.extend([500,600,700,800])
print(l)
l.extend("PYTHON")  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 600, 500, 600, 700, 800, 'P', 'Y', 'T', 'H', 'O', 'N']
print(l)

l.insert(1,2000)    # insert 2000 at location 1 and shift the rest of the values
print(l)

l = [10,20,30]
l2 = l      # will point to the same memory location
l3 = l.copy()
print(l,l2,l3)     # [10, 20, 30] [10, 20, 30] [10, 20, 30]
l.append(40)
print(l,l2,l3)     # [10, 20, 30, 40] [10, 20, 30, 40] [10, 20, 30]
print(id(l))    # 139949531381632
print(id(l2))   # 139949531381632
print(id(l3))   # 140213814592448



# update
# pop
# remove 
# clear 
# del 
l = [10,20,40,40,50,60,60]
l[1] = 10 # update
print(l)

r = l.pop()
print(l,r)  # [10, 10, 40, 40, 50, 60] 60
r = l.pop(2)
print(l,r)  # [10, 10, 40, 50, 60] 40
r = l.remove(10)
print(l,r)  # [10, 40, 50, 60] None
r = l.remove(10)
print(l,r)  # [40, 50, 60] None

#r = l.remove(2000)  # ValueError: list.remove(x): x not in list

l.clear()
print(l)    # []

del l 
#print(l)    # NameError: name 'l' is not defined



# sort()
# reverse()
# sorted()
l = [30,10,5,2,100,70,90,74,43,70,253,215,70,12]
l.sort()
print(l)

print(l[::-1])
l.reverse()
print(l)

del l2
l2 = sorted(l)
print( l, "\n", l2)


# index
# count 
print(l.index(100))
print(l.count(70))


print(l + l2)   # [253, 215, 100, 90, 74, 70, 70, 70, 43, 30, 12, 10, 5, 2, 2, 5, 10, 12, 30, 43, 70, 70, 70, 74, 90, 100, 215, 253]

l4 = [0.1]
print(l4 * 10)  # [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
