# 1
# for i in range(10):
#     print(i)
# ......................
# 2
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# ........................
# 3
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")
# ............................
# 4
# person = {"name": "John", "age": 30, "city": "New York"}
# for key, value in person.items():
#     print(f"{key}: {value}")
# ..................................
# 5
# for i in range(3):
#     for j in range(3):
#         print(f"i: {i}, j: {j}")
# ............................................
# 6
# squares = [x**2 for x in range(10)]
# print(squares)
# ...................................
# 7
# names = ["Alice", "Bob", "Charlie",1]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# ................................
# 8
# for i in range(5):
#     print(i)
# else:
#     print("Loop finished without interruption.")
# ...........................
# 9
# for i in reversed(range(5)):
#     print(i)
# ........................
# 10
# from itertools import count
#
# for i in count(10):  # Starts at 10 and goes infinitely
#     print(i)
#     if i > 15:
#         break
# ................................
# 11
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()
# ..................................
# 12
# for i in range(0, 20, 5):
#     print(i)
# ..................
# 13
# class MyIterable:
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         self.current = 0
#         return self
#
#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current - 1
#         else:
#             raise StopIteration
#
# for num in MyIterable(5):
#     print(num)
# ......................
# 14
# numbers = [1, 2, 3, 4]
# doubled = map(lambda x: x * 2, numbers)
#
# for num in doubled:
#     print(num)
