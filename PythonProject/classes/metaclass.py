# # Metaclass
# # is creating a class dynamically
# '''Metaclass is used for creating Classes.
# A metaclass in Python is a class of a class that defines how a class behaves.
# A class is itself an instance of a metaclass. A class in Python defines how the instance of the
# class will behave.'''
# # Executes with warning
#
# # Ex 1
# num = 23
# print("Type of num is:", type(num))
#
# lst = [1, 2, 4]
# print("Type of lst is:", type(lst))
#
# name = "deepthi"
# print("Type of name is:", type(name))
# ..........................................
# dee = 'metaclasses'
# print(type(dee))
# print(type(str))
# print(dee.__class__.__class__)
#
# # O/p:
# <
#
# class 'str'>
#
# <
#
# class 'type'>
#
# <
#
# class 'type'>
#
#
# ------------------------------
#
#
# # class can be written with just 'pass' due to metaclass.
# class dee: pass


# x = dee()
# print(type(x))
# # <class '__main__.dee'>#object
# print(type(dee))
# # <class 'type'>
#
# '''x is an instance of class dee.
# dee is an instance of the type metaclass.
# type is also an instance of the type metaclass, so it is an instance of itself.'''
#
# ----------------------------------------------------------
#
#
# # Ex for custom meta class
# class meta(type): pass
#
#
# class deepthi(metaclass=meta): pass
# #
# #
# print(type(meta))
# print(type(deepthi))
#
# # o/p:
# <
#
# class 'type'>
#
# <
# class '__main__.meta'>
# ..................................
#
#
# class dee: pass
#
#
# a = dee()
# # put any 3 items inside type() function to make it considered as class
# some = type('deepthi', (), {})
# # there is no difference between these 2 ex.s.
#
# print(type(a))
# print(some)
# s = some()
# s.b = 'An attribute'
# print(s.b)
# .....................................
#
#
# def fun(self):
#     print("This is meta method!")
#
#
# class Base:
#     def userfunction(self):
#         print("This is a class method!")
#
#
# # meta
# meta = type('some', (Base,), dict(a="deepthi", user_method=fun))
# print("The Type of class: ", type(meta))
# # now can create object for meta class
# obj = meta()
# print(" The Type of object: ", type(obj))
# obj.userfunction()
# obj.user_method()
# print(obj.a)
#
# # Output:
# The
# Type
# of
#
#
# class:  <
#     class 'type'>
#
#
# The
# Type
# of
# object: <
#
# class '__main__.some'>
#
#
# This is a
#
#
# class method!
#
#
# This is meta
# method!
# deepthi
# ---------------------------------------------------
# # When you create an object 'new' will be called, and when it is initialized 'init'
# will be called. __new__ allows subclasses of immutable types to customize instance creation.
# It can be overridden in custom metaclasses to customize class creation. __init__ is usually
# called after the object has been created so as to initialize it.
# # __call__ method
# According
# to
# the
# official
# docs, we
# can
# also
# override
# other
#
#
# class methods by defining a custom __call__() method in the metaclass that allows custom behavior
# when the class is called.
#
#
# -------------------------------------------------------
# # Meta class ex
# class deepthi:  # or Meta
#     # def __new__(cls, *args, **kwargs): will get declared before __name__ variable
#     def __new__(self, class_name, bases, attrs):
#         print('bases=',bases)
#         print('class=',class_name)
#         print('attrs=', attrs)
#         a = {}
#         for name, val in attrs.items():
#             if name.startswith('__'):
#                 a[name] = val
#             else:
#                 a[name.upper()] = val
#         print('a=', a)
#         return type(class_name, bases, a)
# class sthuthi(metaclass=deepthi):
#     x = 5
#     y = 8
#     def fun(self):
#         print('hi')
# d = sthuthi()
# #d.fun()
# # Error no o/p
# d.FUN()

