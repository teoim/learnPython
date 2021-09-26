"""
    Docstring: C2, S5, REGEX
    Regular expressions in python
"""

import re

#  . : (dot) any character except new line
#  [a-z] : lowercase characters (char class)
#  [a-zA-Z] : lowercase AND uppercase characters ( char class )
#  [0-9] : matches the digits ( digit class )

#  +  : at least one. Ex: [a-z]+ = "at least one lowercase character"
#  *  : zero or more. Ex: [a-z]* = "zero or more lowercase characters"

#  ^  : start of the string
#  $  : end of string

#  ?  : optional

#  [a-z]{4}  :  exactly 4 lowercase characters;  [a-z] is equivalent of [a-z]{1}
#  [a-z]{2,4}  :  minimum 2 and maximum 4 lowercase characters


# Example: we want to validate the format of a string:

s1 = "ABCDE1234A"
s2 = "ABCDE1234567A"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")

# So i want to check the strings s1 and s2 against the expression r

l = re.findall(r, s1)
print(l)    # ['ABCDE1234A']    => the pathern is valid

l = re.findall(r, s2)
print(l)    # []    (empty list ) => the pathern is invalid


s3 = "AAAAAAABCDE1234A"
l = re.findall(r, s3)
print(l)    # ['ABCDE1234A']  => valid because it found the pattern inside s3 (last 10 positions of the string)
# But i want to restrict this and say the pattern should be at the start of the string:
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r, s3)
print(l)    # []  => not valid. it finds 5 chars but no digit after, still a char -> invalid

s4 = "ABCDE1234AAAA"
l = re.findall(r, s4)
print(l)    # ['ABCDE1234A'] -> FINDS A VALID PATTERN AT THE START OF THE STRING AND IGNORES THE LAST E CHARS
# But I want to restrict that also, so that the string matches the pattern from start to end:
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r, s4)
print(l)    # [] -> now the string must match exactly that format

s5 = "RRRRR1234Q"
l = re.findall(r, s5)
print(l)    # ['RRRRR1234Q']



# I want to check a phone numbr format
# Must be a 10 digit number
# The first digit has to be from 6 to 9
num = "8123456789"  # valid

r = re.compile("^[6-9][0-9]{9}$")
l = re.findall(r,num)
print(l)    # ['8123456789']

num1 = "88888123456789"
l = re.findall(r,num1)
print(l)    # []

num2 = "812345678999"
l = re.findall(r,num2)
print(l)    # []

num2 = "3123456789"
l = re.findall(r,num2)
print(l)    # []    - first digit is less then 6


# Check the date format
# must be dd-mm-yyyy

s = "12-04-2021"
r = re.compile("^[0-3][0-9]-[0-1][0-9]-[0-9]{4}$")
print( re.findall(r,s) )    # ['12-04-2021']

s = "40-40-2020"
print( re.findall(r,s) )    # []

s = "39-19-9999"
print( re.findall(r,s) )    # ['39-19-9999']  .... can get better 
