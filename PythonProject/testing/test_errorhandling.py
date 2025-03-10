# #error handling in pytest
#
# # Test for TypeError
# import pytest
# from priya import divide_numbers
# def test_invalid_input_type():
#     with pytest.raises(TypeError):
#         divide_numbers("10", 2)
# .......................
# # Test that explicitly fails if the result is wrong
# import pytest
# from priya import divide_numbers
# def test_explicit_fail():
#     result = divide_numbers(10, 2)
#     if result != 5:
#         pytest.fail(f"Expected 5, but got {result}")
# ..............................
# # dee.py
#
# def divide_numbers(a, b):
#     """Divide two numbers."""
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
# -----------------
# # test_math_operations.py
# import pytest
# from priya import divide_numbers
#
# # Test that the divide_numbers function raises a ValueError when dividing by zero
# def test_divide_by_zero():
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         divide_numbers(10, 0)
#
# # Test that the divide_numbers function works correctly for valid input
# def test_divide_valid_input():
#     result = divide_numbers(10, 2)
#     assert result == 5
#
# .................................
#
#
