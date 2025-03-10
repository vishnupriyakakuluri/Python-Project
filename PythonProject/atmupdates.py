class atm:
    def __init__(self,name,password,balance):
        self.name=name
        self.password=password
        self.balance=balance
    def checkbalance(self):
        print(self.balance)
    def deposit(self,money):
        if money>0:
            self.balance += money
        else:
            print("invalid amount to deposite.....")
    def withdraw(self,wmoney):
        if wmoney>0 and wmoney<balance:
            self.balance -=wmoney
        else:
            print("please enter valid amount to withdraw")
        return self.balance
dict={'user1':['vishnu',1234,500],'user2':['priya',3456,0],'user3':['vinod',5678,1000]}
username=input("enter the username:")
pincheck =int(input("enter the pin:"))
if username==dict['user1'][0] and pincheck==dict['user1'][1]:
    balance=dict['user1'][2]
    print("valid user\n")
elif username==dict['user2'][0] and pincheck==dict['user2'][1]:
    balance = dict['user2'][2]
    print("valid user\n")
elif username==dict['user3'][0] and pincheck==dict['user3'][1]:
    balance = dict['user2'][2]
    print("valid user")
else:
    print("invalid details.....fail to login")
    exit()
user=atm(username,pincheck,balance)
while(1):
    print("1.deposit\n2.withdraw\n3.balance checking\n4.exit")
    choice=int(input("enter the choice"))
    if choice==2:
        wmoney = int(input("enter the money you want to withdraw"))
        print(user.withdraw(wmoney))
        print("available balance:",user.balance)
    elif choice==1:
        amount=int(input("enter the amount to deposite:"))
        user.deposit(amount)
    elif choice==3:
        user.checkbalance()
    elif choice==4:
        print("thank you and exiting")
        exit()
