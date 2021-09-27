
s = "Python programming 2021"

print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])
print(s[-3])

# Slicing - print chars from 3 to 14
print(s[3:15])

# Slice from index 7 till the end
print(s[7:])

# 
print(s[:6])

# Stride : print every x characters
print( s[::2])

# Stride : print every x chars in reverse
print( s[::-1])

#

for val in s[::2]:
    print(val)
    
# Help function:

# help(string)	# string manual
# help(str)     # string manual
# print(dir(str))     # available functions for string
