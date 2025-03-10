# __new__ is a special method responsible for creating and returning a new instance of a class.
# It is called before the __init__ method.
# It is used when you need to control the creation of a new object, for example,
# in singleton patterns or when subclassing immutable types like int or tuple.
# __new__ is a static method, so it takes the class (cls) as the first parameter.
# You typically call the superclass’s __new__ method to ensure proper creation of the instance.
#
# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         print("Creating a new instance")
#         instance = super().__new__(cls)  # Call the base class `__new__`
#         return instance
#
#     def __init__(self, value):
#         print("Initializing the instance")
#         self.value = value
#
# obj = MyClass(10)
# ......................................
#
# __str__ is a special method used to define the string representation of an object
# when str(object) or print(object) is called.
# It is intended to return a "user-friendly" string that represents the object.
#
# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"MyClass(name={self.name}, age={self.age})"
#
# obj = MyClass("Alice", 30)
# print(obj)  # Calls __str__()
# ......................................
#
# #Class Inside a Class
# class OuterClass:
#     def __init__(self, outer_name):
#         self.outer_name = outer_name
# 	#self.i=self.InnerClass()
#     class InnerClass:
#         def __init__(self, inner_name):
#             self.inner_name = inner_name
#
#         def display(self):
#             return f"InnerClass name: {self.inner_name}"
#
#     def display(self):
#         return f"OuterClass name: {self.outer_name}"
#
# # Create an instance of the OuterClass
# outer = OuterClass("Outer_Instance")
#
# # Create an instance of the InnerClass
# inner = outer.InnerClass("Inner_Instance")
# # inner=outer.i
# # inner=OuterClass.InnerClass()
# # Access methods from both classes
# print(outer.display())  # Output: OuterClass name: Outer_Instance
# print(inner.display())  # Output: InnerClass name: Inner_Instance
