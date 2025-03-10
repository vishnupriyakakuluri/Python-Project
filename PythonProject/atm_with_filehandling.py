balance = 0


def deposit(amount, name):
    try:
        if amount < 0:
            raise ValueError("\tEnter valid input")
    except ValueError as e:
        print(f"{e}")
    else:
        global balance
        balance += amount
        update_balance(name, balance)
        print("\tyour current balance: ", balance)


def withdraw(amount, name):
    global balance
    try:
        if amount < 0:
            raise ValueError("\n\tEnter a valid amount\n")
        if amount > balance:
            raise ValueError("\n\tInsufficient Balance")
    except ValueError as e:
        print(f"{e}")
    else:
        balance -= amount
        update_balance(name, balance)
        print(f"\twithdrawn amount:{amount}")
        print(f"\n\tActual total amount:{balance}")


def check_balance():
    print(f"\tYour Total balance:{balance}")


def new_user():
    name = input("\tEnter your name: ")
    pin = int(input("\tEnter the Pin: "))
    new_bal = 0
    with open("users.txt", 'a') as file:
        file.write(f"{name},{pin},{new_bal}\n")
    print("\tregistered successfully")


def old_user():
    name = input("\tEnter your name: ")
    pin = int(input("\tEnter the Pin: "))
    with open("users.txt", 'r') as f:
        data = f.readlines()
    for x in data:
        user_data = x.split(',')
        if user_data[0] == name and int(user_data[1]) == pin:
            global balance
            balance = int(user_data[2])
            print(f"\n\twelcome {name} your current balance is : {balance}")
            return name
    print("\tUser not found")


def update_balance(name, new_balance):
    with open('users.txt', 'r') as f:
        data = f.readlines()

    with open("users.txt", 'w') as f:
        for x in data:
            users_data = x.split(',')
            if users_data[0] == name:
                users_data[2] = str(new_balance)
            f.write(",".join(users_data) + "\n")


def menu():
    print("\n\n\t1 New User:\n\t2 Already a user\n\t3 Exit")


def main():
    while True:
        print("\n\tWELCOME TO ATM MACHINE")
        menu()
        Choice = int(input("\n\tEnter your choice: "))
        if Choice == 1:
            new_user()
        elif Choice == 2:
            x = old_user()
            if x:
                while True:
                    print("\n\t1 Deposit\n\t2 Withdraw\n\t3 Check Balance\n\t4 Exit")
                    ch = int(input("\n\tEnter what you whant to do: "))
                    if ch == 1:
                        amount = int(input("\n\tEnter The Amount To Deposit: "))
                        deposit(amount, x)
                    elif ch == 2:
                        amount = int(input("\n\tEnter The Amount To Withdraw: "))
                        withdraw(amount, x)
                    elif ch == 3:
                        check_balance()
                    elif ch == 4:
                        break
                    else:
                        print("Enter the valid input")
        elif Choice == 3:
            exit()
            print("Thank you visit again")
        else:
            print("Enter the valid input")


main()

with open("users.txt", "r") as file:
    lines = file.readlines()  # Reads all lines and returns them as a list
    print(lines)