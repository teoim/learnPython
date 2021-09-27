# Dictionaries
# 1. Mutable
# 2. Unordered
# 3. Keys should be unique
# 4. Keys should be imutable (int, float, str, tuple)
# Python creates hash tables with key:value pairs ==> dictionarries are faster than lists at retrieving values: complexity O(1)

d = {"id": "ABC100", "name": "giorgio", "email": "giorgio@gmail.com"}
print(d)

# Add:
d["contact_nu"] = 1234567890
print(d)

# Update
d["contact_nu"] = 555555555
print(d)

# get()
# setdefault()
print(d["id"])
print(d.get("id"))

#print(d["age"]) # KeyError: 'age'
print(d.get("age")) # None
print(d.get("age",-100)) # -100
print(d.get("age","What are you taliking about?")) # What are you taliking about?


print( d.setdefault("id"))   # ABC100
print(d)    # {'id': 'ABC100', 'name': 'giorgio', 'email': 'giorgio@gmail.com', 'contact_nu': 555555555}
print( d.setdefault("age")) # None  - Will add the "age" key with default value of "None"
print(d)    # {'id': 'ABC100', 'name': 'giorgio', 'email': 'giorgio@gmail.com', 'contact_nu': 555555555, 'age': None}
print( d.setdefault("city", "London"))  # London
print(d)    # {'id': 'ABC100', 'name': 'giorgio', 'email': 'giorgio@gmail.com', 'contact_nu': 555555555, 'age': None, 'city': 'London'}


# Parse a dictionary

for key in d:
    print(key, d[key])

# Build a dictionary where values are the square of the keys: { 1:1 , 2:4, 3:9, .... 10:100 }
d ={}
print(d)
for i in range(10):
    d.setdefault(i+1, (i+1)**2)
    print(d)


# keys()
# values()
# items()
print(d.keys())
print(d.values())
print(d.items())

for t in d.items():
    print(t)


# --- 



l1 = [1,2,3,4,5,6]
l2 = ["a","b","c","d","e","f"]

# Make a dictionary from 2 lists:
d = dict(zip(l2,l1))
print(d,type(d))

d1 = dict.fromkeys(l1)
print(d1)   # {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}

d2 = dict.fromkeys(l1,"DefaultVal")
print(d2)   # {1: 'DefaultVal', 2: 'DefaultVal', 3: 'DefaultVal', 4: 'DefaultVal', 5: 'DefaultVal', 6: 'DefaultVal'}

d.update(d2)   # Merge the 2 dictionaries
print(d)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 1: 'DefaultVal', 2: 'DefaultVal', 3: 'DefaultVal', 4: 'DefaultVal', 5: 'DefaultVal', 6: 'DefaultVal'}


# pop 
# popitem 
# clear 
# del 

print( d2.pop(2), d2) # DefaultVal {1: 'DefaultVal', 3: 'DefaultVal', 4: 'DefaultVal', 5: 'DefaultVal', 6: 'DefaultVal'}

print( d2.popitem(), d2)    # (6, 'DefaultVal') {1: 'DefaultVal', 3: 'DefaultVal', 4: 'DefaultVal', 5: 'DefaultVal'}

d2.clear()
print( d2)  # {}

del d2
print( d2 ) # NameError: name 'd2' is not defined

