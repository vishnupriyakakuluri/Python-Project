# from unittest.mock import Mock
#
# # Mocking a function
# mock_function = Mock(return_value=42)
#
# # Call the mock function
# result = mock_function()
#
# # Assertions
# assert result == 42
# mock_function.assert_called_once()  # Ensure it was called once
# .....................
# from unittest.mock import Mock
#
# class Calculator:
#     def add(self, a, b):
#         return a + b
#
# # Mock the add method
# calculator = Calculator()
# calculator.add = Mock(return_value=10)
#
# # Call the mocked method
# result = calculator.add(2, 3)
#
# # Assertions
# assert result == 10
# calculator.add.assert_called_once_with(2, 3)  # Ensure it was called with specific arguments
# ..............................
#
# #for patch function create a 'json'(data.json) file in the same folder of source/test code
#
# import json
# from unittest.mock import patch
#
#
# # Function to read data from a local JSON file
# def get_data(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
#
# # Mocking the `open` function to simulate reading a local JSON file
# @patch('builtins.open')
# @patch('json.load')
# def test_get_data(mock_json_load, mock_open):
#     # Mock the file content returned by `json.load`
#     mock_json_load.return_value = {"key": "mocked_value"}
#
#     # Call the function with a dummy file path
#     result = get_data('data.json')
#
#     # Assertions
#     assert result == {"key": "mocked_value"}  # Verify the mocked data is returned
#     mock_open.assert_called_once_with('data.json', 'r')  # Ensure the file was opened correctly
#     mock_json_load.assert_called_once()  # Verify `json.load` was called
#
#
# # Run the test function
# if __name__ == "__main__":
#     test_get_data()
#     print("Test passed successfully!")
#
#
# #data.json file
# {
#     "employees": [
#         {
#             "id": 1,
#             "name": "Alice",
#             "role": "Software Engineer",
#             "skills": ["Python", "Flask", "Docker"]
#         },
#         {
#             "id": 2,
#             "name": "Bob",
#             "role": "Data Scientist",
#             "skills": ["Python", "pandas", "NumPy"]
#         }
#     ],
#     "company": {
#         "name": "Tech Corp",
#         "location": "San Francisco",
#         "employeesCount": 200
#     },
#     "isHiring": true
# }
#
# ......................................
#
from unittest.mock import Mock

# Function to process a payment using a payment gateway
def process_payment(payment_gateway, amount):
    response = payment_gateway.charge(amount)
    if response.get("status") == "success":
        return "Payment Successful"
    else:
        return "Payment Failed"

# Test for process_payment function
def test_process_payment():
    # Create a mock object for the payment gateway
    mock_payment_gateway = Mock()

    # Simulate the behavior of the `charge` method
    mock_payment_gateway.charge.return_value = {"status": "success", "transaction_id": "12345"}

    # Test successful payment
    result = process_payment(mock_payment_gateway, 100)
    assert result == "Payment Successful"

    # Verify that the `charge` method was called with the correct amount
    mock_payment_gateway.charge.assert_called_once_with(100)

    # Simulate a failed payment
    mock_payment_gateway.charge.return_value = {"status": "failed", "error": "Insufficient funds"}

    # Test failed payment
    result = process_payment(mock_payment_gateway, 50)
    assert result == "Payment Failed"

    # Verify that the `charge` method was called again with the new amount
    mock_payment_gateway.charge.assert_called_with(50)

# Run the test
if __name__ == "__main__":
    test_process_payment()
    print("All tests passed!")
#
# ..............................................
# Testing Best Practices: Isolating Test Cases
# Isolating test cases means ensuring that each test case is independent and self-contained so that it does not rely on the execution or result of any other test case. This practice is critical for maintaining the reliability and accuracy of your test suite.
#
# Why Isolating Test Cases is Important:
# Avoids Dependencies:
#
# Test cases depending on each other can cause cascading failures, making debugging difficult.
# Improves Reliability:
#
# Independent tests can run in any order without affecting results.
# Facilitates Parallel Execution:
#
# Tests can be executed in parallel for faster testing.
# Simplifies Debugging:
#
# If a test fails, it's easier to pinpoint the issue since there are no dependencies on other tests.
#
# example:
# import unittest
#
# class MyTestCase(unittest.TestCase):
#     def setUp(self):
#         self.resource = "test resource"
#
#     def tearDown(self):
#         self.resource = None
#
#     def test_case_1(self):
#         self.assertEqual(self.resource, "test resource")
#
#     def test_case_2(self):
#         self.assertIsNotNone(self.resource)
#
