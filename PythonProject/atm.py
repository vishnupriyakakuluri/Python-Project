class atm:
    def __init__(self,name,password,balance):
        self.name=name
        self.password=password
        self.balance=balance
    def authenticate(self,name,passw):
        if self.name==name and self.password==passw:
            print("login successfully")
            return 1
        else:
            print("wrong password")
            return 0
    def checkbalance(self):
        print(self.balance)
    def deposit(self,money):
        if money>0:
            self.balance += money
        else:
            print("invalid amount to deposite.....")
    def withdraw(self,wmoney):
        self.balance -=wmoney
        return self.balance

user=atm('vishnu',1234,0)
pincheck = int(input("enter the pin:"))
if user.authenticate('vishnu',pincheck):
    while(1):
        print("1.deposit\n2.withdraw\n3.balance checking\n4.exit")
        choice=int(input("enter the choice"))
        if choice==2:
            wmoney = int(input("enter the money you want to withdraw"))
            if user.balance>wmoney:
                print(user.withdraw(wmoney))
                print("available balance:",user.balance)
            else:
                print("no sufficient balance to withdraw")
        elif choice==1:
            amount=int(input("enter the amount to deposite:"))
            user.deposit(amount)
        elif choice==3:
            user.checkbalance()
            exit()
        elif choice==4:
            print("thank you for using")
            exit()
else:
    print("fail to login...try again")
