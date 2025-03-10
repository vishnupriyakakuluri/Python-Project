# squares = {x: x**2 for x in range(1, 11)}
# print(squares)
# # Output: {1: 1, 2: 4, 3: 9, ..., 10: 100}
# .........................................
# numbers = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print(numbers)
# # Output: {2: 4, 4: 16, 6: 36, ..., 10: 100}
# .........................................
# fruits = ['apple', 'banana', 'cherry']
# fruit_dict = {fruit: len(fruit) for fruit in fruits}
# print(fruit_dict)
# # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
# ..........................................
# original = {'a': 1, 'b': 2, 'c': 3}
# reversed_dict = {value: key for key, value in original.items()}
# print(reversed_dict)
# # Output: {1: 'a', 2: 'b', 3: 'c'}
# ............................
# keys = ['name', 'age', 'gender']
# default_dict = {key: None for key in keys}
# print(default_dict)
# # Output: {'name': None, 'age': None, 'gender': None}
# ............................................
# numbers = range(1, 11)
# even_odd = {x: ('even' if x % 2 == 0 else 'odd') for x in numbers}
# print(even_odd)
# # Output: {1: 'odd', 2: 'even', 3: 'odd', ..., 10: 'even'}
# ..........................................
# keys = ['name', 'age', 'gender']
# values = ['Alice', 25, 'Female']
# merged = {keys[i]: values[i] for i in range(len(keys))}
# print(merged)
# # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female'}
# .........................................
# ascii_dict = {chr(i): i for i in range(65, 91)}
# print(ascii_dict)
# # Output: {'A': 65, 'B': 66, ..., 'Z': 90}
# ....................................
# nested = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
# flattened = {k1 + '_' + k2: v2 for k1, v1 in nested.items() for k2, v2 in v1.items()}
# print(flattened)
# # Output: {'a_b': 1, 'a_c': 2, 'd_e': 3, 'd_f': 4}
# ..........................................
# string = "hello world"
# freq = {char: string.count(char) for char in set(string)}
# print(freq)
# # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
