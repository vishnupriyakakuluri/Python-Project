# Assignment:
# 1. Write a program to raise exception
# a. enter name of the person raise exception where it is below 3 letters
# b. enter salary of the person raise exception when salary below 10000
#
# 2. Define your exception as UsernameLengthFailure
# a. enter username if namelength is below 4 and above 8 raise exception

"""
#1a
try:
    name=input("enter name of the person:")
    if len(name)<3:
        raise ValueError(name)
    else:
        print("entered name is valid i.e.,",name)
finally:
    print("name of the person entered successfully")"""

#1b
"""try:
    salary=int(input("enter salary of the person:"))
    if salary<10000:
        raise ValueError(salary)
    else:
        print(salary)
except TypeError:
    print("error")"""
#2a
"""class UsernameLengthFailure(Exception):
    pass

class TestData:
    def testMe(self,username):
        if len(username)>4 and len(username)<8:print(username)
        else:raise UsernameLengthFailure('Validation Failed')
#once you declare variable for TestData class as follows:
test =TestData()
test.testMe("vis")
"""
