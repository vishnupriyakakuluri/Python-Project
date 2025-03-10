# # pytest
# # assert ex
#
# def test_list_contents():
#     my_list = [1, 2, 3, 4]
#     assert 3 in my_list, "Value 3 is missing from the list"
#
#
# def test_dictionary_key():
#     my_dict = {"name": "Alice", "age": 25}
#     assert "name" in my_dict, "Key 'name' is not in the dictionary"
#     assert my_dict["name"] == "Alice", "Expected value for key 'name' is 'Alice'"
# test_list_contents()
# test_dictionary_key()
#
#
# ...........................
#
# import math
#
#
# def test_float_comparison():
#     result = math.sqrt(16)
#     assert math.isclose(result, 4.0, rel_tol=1e-9), "Square root of 16 should be 4.0"
#
#
# .................
#
#
# # boolean
#
# def test_boolean():
#     is_valid = True
#     assert is_valid, "The condition is not valid"
#
#
# ..........................
# # pip install pytest
# # to run in terminal
# # pytest test_example.py
# # to run a particular test case
# pytest
# test_example.py::test_addition
#
# # let he file name has 'test' prefix
# # test_filename.py
# import pytest
#
#
# def test_zero_division():
#     with pytest.raises(ZeroDivisionError, match="division by zero"):
#         result = 1 / 0
#
#
# .........................
# Using
# Pytest
# Fixtures
# with Assertions
# # test_with_fixture.py
# import pytest
# @pytest.fixture
# def sample_data():
#     return [10, 20, 30, 40]
# def test_data_contains_value(sample_data):
#     assert 20 in sample_data, "Expected 20 to be in the sample data"

#
#
# ............................
#
#
# # examples for Parameterized Testing: Running tests with multiple inputs
#
# @pytest.mark.parametrize is a
#
#
# powerful
# feature in Pytest
# that
# allows
# you
# to
# run
# a
# test
# function
# with multiple sets of parameters.This is useful for testing the same functionality with different inputs, thus eliminating the need to write duplicate test functions.
#
# # test_parametrized.py
#
# import pytest
#
#
# # Test function with multiple inputs using @pytest.mark.parametrize
# @pytest.mark.parametrize("a, b, expected", [
#     (3, 2, 5),  # Test case 1
#     (1, 1, 2),  # Test case 2
#     (-1, 1, 0),  # Test case 3
#     (0, 0, 0)  # Test case 4
# ])
# def test_addition(a, b, expected):
#     assert a + b == expected, f"Expected {a} + {b} to be {expected}"
#
#
# .............................
#
# import pytest
#
#
# @pytest.mark.parametrize("value, expected", [
#     (0, "Zero"),  # Edge case 1
#     (1, "Positive"),  # Edge case 2
#     (-1, "Negative"),  # Edge case 3
# ])
# def test_edge_cases(value, expected):
#     if value == 0:
#         assert "Zero" == expected
#     elif value > 0:
#         assert "Positive" == expected
#     else:
#         assert "Negative" == expected
#
#
# ............................
# import pytest
#
#
# @pytest.mark.parametrize("data, expected_type", [
#     (3, int),  # Test case 1
#     (3.14, float),  # Test case 2
#     ("hello", str),  # Test case 3
#     ([1, 2, 3], list),  # Test case 4
#     ({'a': 1}, dict)  # Test case 5
# ])
# def test_data_type(data, expected_type):
#     assert isinstance(data, expected_type), f"Expected type of {data} to be {expected_type}"
#
#
# .......................................
# import pytest
#
#
# @pytest.mark.parametrize("a, b, expected", [
#     (3, 2, 5),
#     (1, 1, 2),
#     (-1, 1, 0),
#     (0, 0, 0)
# ], ids=["test_case_1", "test_case_2", "test_case_3", "test_case_4"])
# def test_addition(a, b, expected):
#     assert a + b == expected, f"Test failed: {a} + {b} should equal {expected}"
#
#
# ....................
#
#
# # Using multiple parametrize decorators
# import pytest
# @pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
# @pytest.mark.parametrize("c, d", [(5, 6), (7, 8)])
# def test_addition(a, b, c, d):
#     assert (a + b) + (c + d) == (a + b + c + d), f"Failed for {a}, {b}, {c}, {d}"

#
