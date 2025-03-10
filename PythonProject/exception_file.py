#Exception handling
"""try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")"""
#------------------------
"""try:
    a=5
    b=0 #'0'
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')"""
#-----------------------------
"""try:
    print("try block")
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )"""
#---------------------------------------
"""try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")"""
#--------------------------------------
"""
# User Defined Exception:
# Example:

class MyValidatorError(Exception):
 pass

class TestData:
    def testMe(self, num):
        if num>10:print('validation successful')
        else:raise MyValidatorError('Validation Failed')
#once you declare variable for TestData class as follows:
test =TestData()
test.testMe(12)
# returns output as “validation successful
#test.testMe(4)
#returns error message as “validation Failed”"""
#-------------------------
"""class MyValidatorError(Exception):
 pass

class TestData:
    def testMe(self, num):
        if num>10:print('validation successful')
        else:raise MyValidatorError('Validation Failed')
#once you declare variable for TestData class as follows:
test =TestData()
try:test.testMe(3)
except MyValidatorError:print('Validation Failed1')
# returns output as “validation successful
#test.testMe(4)
#returns error message as “validation Failed”
"""
#..........................................

"""import os
path='C:\\Users\\S KRISHNA\\PycharmProjects\\Deenetwork\\dee2'
try:
    os.mkdir(path)
except OSError as error:
    print('oops already there',error)"""
#---------------------------------
# Assignment:
# 1. Write a program to raise exception
# a. enter name of the person raise exception where it is below 3 letters
# b. enter salary of the person raise exception when salary below 10000
#
# 2. Define your exception as UsernameLengthFailure
# a. enter username if namelength is below 4 and above 8 raise exception