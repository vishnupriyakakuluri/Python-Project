class atm:
    def __init__(self,name,password,balance):
        self.name=name
        self.password=password
        self.balance=balance
    def checkbalance(self):
        print(f'your account balance is {self.balance}')
    def deposit(self,money):
        if money>0:
            self.balance += money
            print(f'successfully deposited the amount of {money}')
        else:
            print("invalid amount to deposite.....")
    def forgotpassword(self,username,newpin):
        self.password=newpin
        print("successfully created newpassword")
    def withdraw(self,wmoney):
        if wmoney>0 and wmoney<self.balance:
            self.balance -=wmoney
            print(f'you successfully debited the amount of{wmoney}')
        else:
            print("please enter valid amount to withdraw")
        return self.balance
dict={'1234567890':['vishnu',1234,500.00],'2345678901':['priya',3456,700.00],'345678901':['vinod',5678,1000.00]}
username=input("enter account number:")
if username in dict:
    print("existed user\n")
    balance=dict[username][2]
else:
    print("new user....so please create account :")
    name=input("enter the name:")
    pin=int(input("create the pin:"))
    balance=int(input("enter initial amount:"))
    dict[username]=[name,pin,balance]
    print("successfully created new account")
print("if you want to login into atm press y otherwise N:")
login=input()
if login=='y':
    pass
else:
    print("exiting")
    exit()
for i in range(3):
    pincheck = int(input("enter the pin:"))
    if pincheck==dict[username][1]:
        print("login successfully\ncontinue your process\n----------------------------------")
        break
    else:
        print("your pin is wrong...you have",3-i-1,"more chance")

if pincheck==dict[username][1]:
    user=atm(username,pincheck,balance)
    while(1):
        print("1.deposit\n2.withdraw\n3.balance checking\n4.forgot password\n5.exit\n------------------------")
        choice=int(input("enter the choice:"))
        if choice==2:
            wmoney = int(input("enter the money you want to withdraw"))
            print(user.withdraw(wmoney))
            print("available balance:",user.balance)
        elif choice==1:
            print("your fixed deposite is",balance)
            amount=int(input("enter the amount to deposite:"))
            user.deposit(amount)
        elif choice==3:
            user.checkbalance()
        elif choice==4:
            newpin = int(input("enter new password:"))
            user.forgotpassword(username,newpin)
            pinrecheck=int(input("enter newly created pin to continue:"))
            if newpin==pinrecheck:
                pass
            else:
                print("entered pin is wrong")
                exit()
        elif choice==5:
            print("-----------------\nThank you and exiting")
            exit()
else:
    print("you entered a wrong pin")
    exit()
