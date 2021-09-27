
# Groups 

# re.findall()  # will return all occurences of the pattern in the string 
# re.match()    # will only return the first occurence of the pattern of the string 
# Both return None if the pattern is not found 

# Notes on patterns:
# [0-9] is equivalent to \d     "only digits"
# [^0-9] is equivalent to \D    "anything BUT digits"
# [a-zA-Z0-9] is equivalent to \w       "only lettes and numbers"
# [^a-zA-Z0-9] is equivalent to \w      "anything BUT letters and numbers"
# for "space" we use \s 
# anything but space: \S 


import re 


s = "AANA01623B"
r = re.compile("^[A-Z]{4}[0-9]{5}[A-Z]")
print( re.findall(r,s))


s = "24-09-2021"
r = "^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
print(re.findall(r,s))      

# Match objects 
m = re.search(r,s)
print( m )  # <re.Match object; span=(0, 10), match='24-09-2021'>
print( m.group() )  # 24-09-2021

s = "24-09-202100"
m = re.search(r,s)
print( m )  # None 
#print( m.group() )  # AttributeError: 'NoneType' object has no attribute 'group'
if m:
    print( m.group() )
else:
    print( "No match found for", r,  )


# --- GROUPS --- # 

s = "24-09-2021"
#r = "^[0-9]{2}-[0-9]{2}-[0-9]{4}$"
r = "^([0-9]{2})-([0-9]{2})-([0-9]{4})$"    # Every piece contained between (...) is a group 
m = re.search(r,s)
if m:
    print( m.group(0))  # 24-09-2021
    print( m.group(1))  # 24 
    print( m.group(2))  # 09 
    print( m.group(3))  # 2021
    # print( m.group(4))  # IndexError: no such group
else:
    print("No pattern found for ", s, r)


# Named groups : 
r = "^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$"    # ?P<groupName>(...) -> /P<..> before every group contains the name of the group 
m = re.search(r,s)
print( "Day:", m.group("day"))
print( "Month:", m.group("month"))
print( "Year:", m.group("year"))


phNum = "+40 724234567"
#phNum = "724234567"
#phNum = "0724234567"
r = re.compile("^(?:\+40\s)?(0?7[0-9]{8})")  # ?: marks a non-captured group - it will be ignored (?)

m = re.search(r,phNum)

if m:
    print(m.group(1))
else:
    print("Nope..not yet.")


