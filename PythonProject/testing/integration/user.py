class User:
    def __init__(self):
        self.users = {}  # Stores users as `username: password`

    def register(self, username, password):
        if username in self.users:
            return "User already exists"
        self.users[username] = password
        return "User registered successfully"

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Login successful"
        return "Invalid username or password"