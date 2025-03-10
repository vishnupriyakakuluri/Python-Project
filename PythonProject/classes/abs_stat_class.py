# 1. Abstract Method
# An abstract method is a method that is declared but contains no implementation.
# It is meant to be overridden by subclasses of the class that declares it.
# Abstract methods are defined in abstract classes, which cannot be instantiated directly.
# They force subclasses to provide implementations for those methods.
#
# Definition: A method that is declared in an abstract class and must be implemented by subclasses.

"""from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # No implementation here

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Example usage
dog = Dog()
dog.make_sound()  # Outputs: Woof!"""


#In this example, make_sound is an abstract method that the Dog class must implement.
#===========================================================

# 2. Static Method
# A static method is a method that belongs to the class rather than any instance of the class.
# It doesn't take self as its first argument, meaning it doesn't have access to instance attributes
# or methods. Static methods are often utility functions related to the class but do not need access
# to its instance data.
#
# Definition: A method that does not require access to instance-specific data or methods;
# it belongs to the class itself.

"""class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
result = MathOperations.add(5, 3)
print(result)  # Outputs: 8"""


# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9 / 5) + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9
#
#     @staticmethod
#     def celsius_to_kelvin(celsius):
#         return celsius + 273.15
#
#     @staticmethod
#     def kelvin_to_celsius(kelvin):
#         return kelvin - 273.15
#
#
# # Example usage
# print(TemperatureConverter.celsius_to_fahrenheit(25))  # Outputs: 77.0
# print(TemperatureConverter.fahrenheit_to_celsius(77))  # Outputs: 25.0
# print(TemperatureConverter.celsius_to_kelvin(25))  # Outputs: 298.15
# print(TemperatureConverter.kelvin_to_celsius(298.15))  # Outputs: 25.0

#In this example, add is a static method because it doesn’t require any instance data.
#=============================================

# 3. Class Method
# A class method is a method that is bound to the class rather than its instances.
# It takes the class itself as the first argument (usually named cls), allowing it to access
# class-level attributes and methods, but not instance-level ones.
#
# Definition: A method that is bound to the class and not the instance; it takes the class (cls)
# as its first argument.

# class Employee:
#     raise_amount = 1.05  # Class variable
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#     def apply_raise(self):
#         self.salary *= self.raise_amount
#
# # Example usage
# emp = Employee("John", 50000)
# print(emp.salary)  # Outputs: 50000
#
# # Changing the class variable using class method
# Employee.set_raise_amount(1.10)
# emp.apply_raise()  # Applies the new raise amount
# print(emp.salary)  # Outputs: 55000

# In this example, the set_raise_amount method is a class method that modifies the
# class variable raise_amount.
#
# Summary:
# Abstract Method: A method without implementation in an abstract class,
#     must be implemented by subclasses.
# Static Method: A method that doesn’t require access to instance or class data.
# Class Method: A method that takes the class itself (cls) as the first argument,
# allowing access to class-level attributes.