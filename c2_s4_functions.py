# USER DEFINED FUNCTIONS 
# Uses: 
#	Code reuse
#	Modularity


# Say I have a string and i want the reverse of it :
# s = "python"
# result = value_reverse(s) 

# Function definition:
def value_reverse(value):
    reverse = ""
    if type(value) == list or type(value) == str:
	    reverse = value[::-1]
    else:
        tmp = str(value)
        reverse = tmp[::-1]
    return reverse


# Function call:
s = "Python"
result = value_reverse(s)
print(result)

l = [10,20,30,40,50]
result = value_reverse( l )
print(result)

num1 = 100
result = value_reverse(num1)    # Error --> we must handle this in the new funtion we defined 
print(result)



# PASSING VALUES TO A FUNCTION  -  different techniques:
# 1. Positional argument
# 2. Default argument 
# 3. Keyword argument
# 4. Variable length positional arguments
# 5. Variable length keyword arguments


# --- 1. Positional argument --- #
def linear_search( l, key):
    for value in l:
        if value == key:
            return True
    else:
        return False


l = [100,200,300,400,500]
key = 400
result = linear_search(l,key)   # It's mandatory to pass both parameters expected by the function 
print(result)



# --- 2. Default argument --- #

# Example: I need a password generator.
# The password should comply with the following requirements: 
# 8 chars long (by default, if no length is passed to the function)
# 1 Upper
# 1 lower
# 1 special char 
# 1 digit

# Will use the 2 functions: 
# ord() - returns the ascii code of a char 
# chr() - given an ascii code, returns the corresponding character

print( ord('a'), ord('z'), ord('A'), ord('Z'))    # 97 122 65 90
print( chr(97))     # a 

import random
def gen_password( length=8 ):
    newpass = ''
    #passLength = 8
    #if length is not null: 
    #    passLength = length
    
    while( len(newpass) < length ):
        num1 = chr( random.randint( 97, 122  ))    # lowercase character
        num2 = chr( random.randint( 65, 90   ))     # uppercase character
        num3 = chr( random.randint( 33, 47   ))     # special character
        num4 = chr( random.randint( 48, 57   ))     # digit 
        num5 = chr( random.randint( 58, 64   ))     # special character
        num6 = chr( random.randint( 91, 96   ))     # special character
        num7 = chr( random.randint( 123, 126 ))     # special character
        newpass = newpass + num1 + num2 + num3 + num4 + num5 + num6 + num7 
    l = random.sample( newpass, length) # randomly chooses from newpass the number of characters mentioned by the 'length' 
    newpass = "".join(l)    # convert list to string
    return newpass


result = gen_password(11)
print(result, "\npass length: ", len(result))



# --- 3. Keyword argument --- #


# Example: username and password validation function


def validate( username, password):
    if username == 'ABC' and password == 'Abc@123':
        return 'Access permitted'
    else:
        return 'Access denied'

print( validate( "ABC", "Abc@123")) # Access permitted
print( validate( "Abc@123", "ABC")) # Access denied
print( validate( password="Abc@123", username="ABC")) # Access permitted


# help(print) :
#   print(...)
#       print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
# Default values for separator and end are " ", respectively "\n"
# We can overwrite those values using the keyword arguments: 

print(100,200,300)  # prints all values on a single line, separated by a space and a "newline" char at the end
print(100,200,300,sep="~", end="|") # 100~200~300|
print(1000,2000,3000,sep="\n")  # prints each number on a new line 



# --- 4. Variable length positional arguments --- #


# scenario:
l = [100,200,300,400]
l.append(500)   # adds 500 to the list l 
#l.append(350,500,450)   # will not work with multiple parameters

# => I want a function that gets multiple parameters and adds them all to a list and returns the list:
# add_value(100,200,300,400,500)
# add_value(100,200)
# add_value(100,200,300,400,500,600,700,800,900)


def add_values( *args ):    # accepts any number of parameters 
    # print(args)
    l =[]
    for elem in args:
        l.append(elem)
    return l

result = add_values(100,200,300,400,500)
print(result, type(result))
result = add_values(100,200)
print(result, type(result))
result = add_values(100,200,300,400,500,600,700,800,900)
print(result, type(result))



# --- 5. Variable length keyword arguments --- #


# scenario:
# You have a form with the followintg fields: name, email, contact number, dob 
# The fields are not mandatory, so the user may enter maximum 4 but may enter less 

def get_details( **kwargs ):        # arguments are packed as a dictionary
    print(kwargs, type(kwargs))

# {'name': 'ABC', 'email': 'abc@def123.com', 'contactnum': '1234567890', 'dob': '15-05-1966'} <class 'dict'>
get_details( name = "ABC", email = "abc@def123.com", contactnum = "1234567890", dob = "15-05-1966")

# {'name': 'ABC', 'contactnum': '1234567890', 'dob': '15-05-1966'} <class 'dict'>
get_details( name = "ABC",  contactnum = "1234567890", dob = "15-05-1966") 

# {'name': 'ABC', 'dob': '15-05-1966'} <class 'dict'>
get_details( name = "ABC", dob = "15-05-1966")  



