#
# ITERATORS AND ITERTOOLS
#

# ITERATORS
l = [100,200,300,400,500]
i = iter(l)

print(next(i))  # 100
print(next(i))  # 200
print(next(i))  # 300

for val in i:   # more efficient than for val in l
    print(val)


print("-------------------------------------------\n\n")


# ITERTOOLS - functions for working with iterators

import itertools

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]
l3 = [100,200,300,400,500]

# itertools.chain()
# Iterator that iterats through all 3 lists :
i = itertools.chain( l1, l2, l3 )

print(next(i))
print(next(i))
print(next(i))

for val in i:
    print(val)

print("-------------------------------------------\n\n")

# itertools.cycle()
# Create an infinite cycle on the same list

count = 0
for value in itertools.cycle(l2):
    count+=1
    print(count, ' - ', value)
    if count == 23: break

# itertools.repeat()
# Same full list multiple times in a cycle

count = 0
for value in itertools.repeat(l1):
    count+=1
    print(count, ' - ', value)
    if count == 5: break


print("-------------------------------------------\n\n")
l = [1,2,3,4]

i = iter(l)

#for val in i:
#    print(val)
# print(next(i))  # StopIteration - the iterator i has been exhausted and i can't change its position back to the begining of the list

# solution:
t = itertools.tee(i)
print(t)    # (<itertools._tee object at 0x0000005CE11578C0>, <itertools._tee object at 0x0000005CE1161600>)

for val in t[0]:
    print(val)
# then i can iterate the same list again:
for val in t[1]:
    print(val)

print("-------------------------------------------\n\n")

k = iter(l)
t5 = itertools.tee(k,5) # creates 5 copies -  i will be able to iterate 5 times through the same list: t5[0], t5[1], t5[2], t5[3], t5[4]
print(t5)
for j in range(0,5):
    for val1 in t5[j]:
        print(j , ' - ', val1)


print("-------------------------------------------\n\n")


# itertools.islice()
# iterator over part of a list

l5 = [1,213,13,4,123,5214,51245,12,34,4,34,2,3,4,4,23,6,678,9,90,98,656,3,57,54567]

i = iter(l5)
for val in itertools.islice(i,0,6):     # will only iterate over the first 6 elements
    print(val)


print("-------------------------------------------\n\n")


# itertools.count()
# generate fourier series ( infinite numbers )

cnt = 0
for value in itertools.count(10,5):  # starts from 10 and goes on infinitelly in steps of 5. start and step are both optional, default 0 and 1
    cnt +=1
    print(cnt , ' - ', value)
    if cnt == 15: break

print("-------------------------------------------\n\n")

# itertools.permutations
# combinatii de n luate cate m

l = [1,2,3,4,5,6,7,8]
print( itertools.permutations(l,2) )    # <itertools.permutations object at 0x000000CBEAB0E270>

# permutari de 8 luate cate 2 :
perm = itertools.permutations(l,2)
for val in perm:
    print(val)
