#
# INHERITANCE
#
# Simple inheritance
# Multiple inheritance
#

###
# 1 - Simple inheritance
###

import c2_s8_OOP1 as c2s81


# Define a class SavingsAccount which inherits from c2_s3_OOP1.Account class
class SavingsAccount(c2s81.Account):
    def __init__(self, id, name, initial_balance=0):
        super().__init__(id, name, initial_balance)
        self.limit = 50000  # define a new variable

    def withdraw(self, amount):
        if amount < self.limit:
            self.limit -= amount
            return super().withdraw(amount)
        else:
            return "\nError!\nWithdrawal limit exceeded!\nLimit: " + str(self.limit) + "\nAmount: " + str(amount)

sav1 = SavingsAccount( "sav1", "sav1Name", 800)
print(sav1) # <__main__.SavingsAccount object at 0x0000008F55B5E940>

print(sav1.__dict__)

# Reuse methods from parent class:
print(sav1.getName())
print(sav1.getCustomerID())
print(sav1.getBalance())

print(sav1.deposit(45000))
print(sav1.withdraw(3000))

print(sav1.withdraw(300440))




###
# 2 - Multiple inheritance
###

class A:
    pass

class B:
    pass

# Class C inherits from both A and B
class C(A,B):
    pass

help(C)     # a method will be searched first in class C, then in class A and finally in class B if not found this far :
#class C(A, B)
# |  Method resolution order:
# |      C
# |      A
# |      B

# Note: resolution order depends on the order specified when defining the class and inheritance classes 
