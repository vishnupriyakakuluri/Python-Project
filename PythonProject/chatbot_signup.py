import re


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None


def is_valid_password(password):
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_pattern, password) is not None

def create_account():
    print("--------MIRAFRA Technologies--------")
    print("Welcome to the Mirafra banking system!")
    def new_user():
        username=input("enter the username:")
        date_of_birth=input("enter your date of birth:")
        email = input("Enter your email: ")
        if not is_valid_email(email):
            print("Invalid email format. Please try again.")
            return

        password = input(
            "Create a password (at least 8 characters,"
            " including one uppercase letter, one number, and one special character): ")
        if not is_valid_password(password):
            print("Password does not meet the requirements. Please try again.")
            return
        with open("users.txt", 'a') as file:
            file.write(f"{username},{date_of_birth},{email},{password}\n")
        print("Account created successfully!")
    new_user()


create_account()
