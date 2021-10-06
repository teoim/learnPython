#
# OOP in python
#
#  methods that start and end by "__" are implicitly called
#  private variables start with __
# class variables
# class methods
# static methods
#



# define an empty class and instantiate an object
class Person:
    pass

pers1 = Person()
if(__name__ == "__main__"):     # don't execute the following lines when importing this module (c2_s8_OOP3.py)
    print(pers1)  # <__main__.Account object at 0x000000EEDB48E460>



# Define a class:
# Bank account with customer id, __name, __balance; actions: deposit and withdraw

class Account:
    count = 0   # Class variable - ? equivalent to static var. ?

    # Define a class method ( used to work with class variables ) by the keyword @classmethod :
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def getCount(cls):
        return cls.count

    # Static methods don't need the first parameter (self, cls, etc)
    @staticmethod
    def doSomethingStaticly():
        print("This method (Account.doSomethingStaticly()) is static.")

    def __init__(self,cust_id, name, initBal=0):     #  methods that start and end by "__" are implicitly called
        self.__customerID = str(cust_id) + "_" + str(Account.getCount()+1)                    #  private variables start with __
        self.__name = name
        self.__balance = initBal
        #Account.count += 1      # access class variables by "ClassName.classVariable"
        Account.increment_count()   # replaced access to class var by class method

    def getBalance(self):
        return self.__balance

    def getName(self):
        return self.__name

    def getCustomerID(self):
        return self.__customerID

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            return self.__balance

## END OF CLASS Account

if(__name__ == "__main__"):

    cust1 = Account( 8880001, "Bruce", 10000000)
    print(cust1.getName())

    cust2 = Account( 8880002, "Teo", 9900000000)
    print(cust2.getCustomerID())

    cust3 = Account( 8880003, "Johan", 8000)
    print(cust3.getBalance())


    cust3.deposit(90000000)
    print(cust3.getBalance())

    print( cust2.withdraw(5500888888888888888880))
    print(cust2.getBalance())


    # print( cust1.__name )   # AttributeError: 'Account' object has no attribute '__name'
    print( cust1._Account__name )   # Bruce         # standard convention not to do this (accesss private variables this way)
    # This is possible because we are accessing the private var through the object's namespace
    # You can see an object's namespace as follows:
    print( cust1.__dict__ )     # {'_Account__customerID': 8880001, '_Account__name': 'Bruce', '_Account__balance': 10000000}



    #
    # Class variables
    # print the number of accounts created (class variable Account.count) :
    print( "Total number of customers: ", Account.count)

    print("Cust 1: ", cust1.count) # 3
    print("Cust 2: ", cust2.count) # 3
    print("Cust 3: ", cust3.count) # 3
    print("Account.count: ", Account.count) # 3

    Account.count += 5
    print("Cust 1: ", cust1.count) # 8
    print("Cust 2: ", cust2.count) # 8
    print("Cust 3: ", cust3.count) # 8
    print("Account.count: ", Account.count) # 8

    cust1.count = 100   # This will create a new variable in the namespace of the cust1 object
    cust3.count += 5    # This will create a new variable in the namespace of the cust2 object

    print("Cust 1: ", cust1.count) # 100
    print("Cust 2: ", cust2.count) # 8
    print("Cust 3: ", cust3.count) # 13
    print("Account.count: ", Account.count) # 8


    print( cust1.__dict__) # {'_Account__customerID': '8880001_1', '_Account__name': 'Bruce', '_Account__balance': 10000000, 'count': 100}
    print( cust2.__dict__) # {'_Account__customerID': '8880002_2', '_Account__name': 'Teo', '_Account__balance': 9900000000}
    print( cust3.__dict__) # {'_Account__customerID': '8880003_3', '_Account__name': 'Johan', '_Account__balance': 90008000, 'count': 13}


    # Static methods
    Account.doSomethingStaticly()
