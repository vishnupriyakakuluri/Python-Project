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
# import requests
# from unittest.mock import patch
#
# def get_data(url):
#     response = requests.get(url)
#     return response.json()
#
# # Mocking the `requests.get` method
# @patch('requests.get')
# def test_get_data(mock_get):
#     # Simulate API response
#     mock_get.return_value.json.return_value = {'key': 'value'}
#
#     # Call the function
#     result = get_data('http://example.com/api')
#
#     # Assertions
#     assert result == {'key': 'value'}
#     mock_get.assert_called_once_with('http://example.com/api')
# ......................................
