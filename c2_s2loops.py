
# ---
# Write a program that calculates the factorial of a number

# ---

# Write a program that calculates the sum and average of n integers

# ---

# for numbers in the range 0 - 50 prin "Fizz" for multiples of 3, "Buzz" for multiples of 5 and
# FizzBuzz for multiples of both
# Sample:
#   FizzBuzz
#   1
#   2
#   Fizz
#   4 
#   Buzz

for i in range(0,50):
    check = False
    str = ""
    if i%3 == 0:
        str = "Fizz"
        check = True
    if i%5 == 0:
        str = str + "Buzz"
        check = True
    if check:
        print(str)
        continue
    print(f"{i}")

# ---

numbers = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 )
oddNum = evenNum = 0

for i in numbers:
    if i%2:
        oddNum += 1 
    else:
        evenNum += 1
print(f"Found {oddNum} odd numbers and {evenNum} even numbers.")

# ---

start = 1500
end = 2700

for i in range( start, end ):
    if ( i % 5 == 0 and i % 7 == 0 ):
        print(f"{i} is divisible by 5 and 7")

# ---

l = [11,22,33,44,55,66]
key = 44


for value in l:
    if value == key:
        print("Value found.")
        break
    else:
        continue
else:
    print("Value not found.")
print("For loop ended.")

# ---

for index,value in enumerate(l):
    if value == key:
        print(f"Value found at index {index}.")
        break
    else:
        continue
else:
    print("Value not found.")
print("For loop ended.")

# ---

for value in l:
    print(f"Found {value}")
else:
    pass
    # pass is used when no other statement follows it [ "MARKS AN UNDEFINED SCENARIO" ]
    # if we put other statements in the else after pass, those statements will be executed
    #print("INSIDE ELSE AFTER PASS")
print("Outside else with pass")