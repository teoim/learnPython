
# help(str)     # string manual
# print(dir(str))     # available functions for string

# format method
num1 = 100
num2 = 200
print("Num1 is {0} and num2 is {1}".format(num1,num2))
print("Num1 is {val1} and num2 is {val2}".format(val1=num1,val2=num2))


s1 = "make me capital one more time"
print(id(s1))
s1 = s1.capitalize()    # Converts the first letter of the string to UPPERCASE
print(s1)
print(id(s1))   # Strings are imutable, so every time you change it a new one will be created in a different memory space

# upper() , isupper() 
# lower() , islower()
# title() , istitle()
# split()
# join()

s2 = s1.replace(" ", ",")
print(s2)
l1 = s1.split(" ")
l2 = s2.split(",")
print(l1,type(l1))
print(l2,type(l2))

s3 = ";".join( l2 )
print(s3)


# maketrans()
# translate()
sampleStr = "Hello python sample string abcd"
abc = "abcd"
ijk = "1234"
table = str.maketrans(abc,ijk)
result = sampleStr.translate(table) # Hello python s1mple string 1234
print(result)


# index()
# find()
# rfind()
sampleStr2 = "HTML,CSS,PYTHON,JAVA,PYTHON"     # yOU WANT TO CHECK IF PYTHON IS PART OF THE STRING 
print( "PYTHON" in sampleStr2)
print( sampleStr2.index("PYTHON"))  # 9 : start of the first "PYTHON"
print( sampleStr2.find("PYTHON"))   # 9
# print( sampleStr2.index("python"))  # ValueError: substring not found
print( sampleStr2.find("python"))   # -1

print( sampleStr2.rfind("PYTHON"))   # 21 : reverse-find - searches in reverse starting from the end of the string
print( sampleStr2.rfind("python"))   # -1


# strip()
# lstrip() strips frpm the left
# rstrip() strip from the right
sampleStr3 = "      ***Some string whatever*******     "
sampleStr4 = sampleStr3.strip(" ")
print(sampleStr3)
print(sampleStr4)
sampleStr5 = sampleStr4.strip("*")
print(sampleStr5)
print(sampleStr4.lstrip("*"))
print(sampleStr4.rstrip("*"))



# center()
# ljust()
# rjust()
str12 = "hello"
print( str12.center(20,"#")) #      #######hello########
print( str12.ljust(20,"#"))  #      hello###############
print( str12.rjust(20,"#"))  #      ###############hello

# replace()
str1 = "html,java,python,html,css"
str2 = str1.replace("html","HTML5")
print(str2)

