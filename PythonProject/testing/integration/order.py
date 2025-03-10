class Order:
    def __init__(self):
        self.orders = {}  # Stores orders as `username: [list of orders]`

    def place_order(self, username, item):
        if username not in self.orders:
            self.orders[username] = []
        self.orders[username].append(item)
        return f"Order placed: {item}"

    def get_orders(self, username):
        return self.orders.get(username, [])