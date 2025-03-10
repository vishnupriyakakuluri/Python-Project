from user import User
from order import Order

def test_user_order_integration():
    # Initialize modules
    user_module = User()
    order_module = Order()

    # Step 1: Register a user
    assert user_module.register("john_doe", "password123") == "User registered successfully"

    # Step 2: Log in with the registered user
    assert user_module.login("john_doe", "password123") == "Login successful"

    # Step 3: Place an order as the logged-in user
    assert order_module.place_order("john_doe", "Laptop") == "Order placed: Laptop"

    # Step 4: Verify the order
    orders = order_module.get_orders("john_doe")
    assert len(orders) == 1
    assert orders[0] == "Laptop"

    print("Integration test passed!")


if __name__ == "__main__":
    test_user_order_integration()