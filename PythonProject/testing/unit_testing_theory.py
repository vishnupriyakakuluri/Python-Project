# Unit Testing is the first level of software testing where the smallest testable parts of software are tested.
# Unittest is a built-in testing framework that provides a set of tools for testing our code’s functionality in a more systematic and organized manner.
#
# Arrange: Set up the conditions for the test.
# Act: Perform the operation you want to test.
# Assert: Verify the outcome.
#
# #ex: here Calculator() is not defined, still no error. coz it tests assert.
#
# def test_add():
#     # Arrange
#     calculator = Calculator()
#     a,b = 5,3
#     # Act
#     result = calculator.add(a, b)
#     # Assert
#     assert result == 8
#
#
# OOP Concepts Supported by Unittest Framework:
# The White Box Testing method is used for Unit tests. Below are some of supported oops concept by Unitttest framework:
#
# test fixture: A test fixture is used as a baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable. Examples :
# creating temporary databases.
# starting a server process.
# test case: A test case is a set of conditions which is used to determine whether a system under test works correctly.
# test suite: Test suite is a collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.
# test runner: A test runner is a component which set up the execution of tests and provides the outcome to the user.
# ....................................................
#
# Outcomes Possible in Unit Testing
# There are three types of possible test outcomes :
#
# OK – This means that all the tests are passed.
# FAIL – This means that the test did not pass and an AssertionError exception is raised.
# ERROR – This means that the test raises an exception other than AssertionError.
# ................................
#
# White Box Testing, also known as Clear Box Testing, Glass Box Testing, or Structural Testing, is a software testing technique where the internal structure, design, and implementation of the code are tested. In this method, the tester has full knowledge of the underlying source code, algorithms, and structure.
# ......................................
# Example 1: Function to Find the Maximum of Two Numbers
# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# White Box Test Cases:
# Input: a=5, b=3 → Test the if condition a > b.
# Input: a=2, b=4 → Test the else condition.
# ..........................................
#
# Example 2: For a Login Function
#
# def login(username, password):
#     if username == "admin" and password == "1234":
#         return True
#     else:
#         return False
#
# White Box Test Cases:
#
# Test Case 1: username = "admin", password = "1234" → Both conditions true.
# Test Case 2: username = "user", password = "1234" → First condition false.
# Test Case 3: username = "admin", password = "abcd" → Second condition false.
# Test Case 4: username = "user", password = "abcd" → Both conditions false.
# .........................................
#
# Mocking and Stubbing
# 1. Introduction to Mocking
# Mocking is a testing technique used to replace real objects in your code with simulated versions, called mocks. These mock objects mimic the behavior of real objects and allow you to test code in isolation by focusing on specific interactions.
#
# Why use mocking?
# To test units of code without relying on external systems (e.g., databases, APIs).
#
# Stubbing is a technique where you replace a method or function with a predefined response. Unlike mocking, stubs don't track usage; they are simpler and provide predefined results.
