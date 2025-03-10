# #function signature
# #Let’s consider a scenario where you have written a very lengthy code and want to know the function call details. So what you can do is scroll through your code each and every time for different functions to know their details or you can work smartly. You can create a code where you can get the function details without scrolling through the code. This can be achieved in two ways –
# Using signature() function
# Using decorators
#
# We can get function Signature with the help of signature() Function. It takes callable as a parameter and returns the annotation. It raises a value Error if no signature is provided. If the Invalid type object is given then it throws a Type Error.
#
# .........................................................
# from inspect import signature
# def ibrahim(x:str,y:int): print(x,y)
# t=signature(ibrahim)
# print(t)
# print(t.parameters['x'])
# print(t.parameters['y'].annotation)
# -------------------------------------------------
# #decorator
# #To do this the functions in Python certain attributes. One such attribute is __code__ that returns the called function bytecode. The __code__ attributes also have certain attributes that will help us in performing our tasks. We will be using the co_varnames attribute that returns the tuple of names of arguments and local variables and co_argcount that returns the number of arguments (not including keyword-only arguments, * or ** args). Let’s see the below implementation of such decorator using these discussed attributes.
# -----------------------------------------------------
# def make_pretty(func):
#     def inner():
#         print('I got decorated')
#     func()
#     return inner()
# def ordinary():
#     print("I'm ordinary")
# pretty=make_pretty(ordinary)
# print(pretty)
# -----------------------------------------------------
# #decorator
# def inc(x): return x+1
# def dec(x): return x-1
# def operate(func,x):
#     result=func(x)
#     return result
# print(operate(inc,3))
# print(operate(dec,3))
# -------------------------------------------------------
# #decorator
# def smart_division(func):
#     def inner(a,b):
#         print("i'm dividing:",a,'and',b)
#         if b==0:
#             print('Woops! cannot divide')
#             return
#         return func(a,b)
#     return inner
# @smart_division
# def divide(a,b): print(a/b)
# divide(2,0)
# ........................................................
# def function_details(func):
#     argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
#
#     fname = func.__name__
#
#     def inner_func(*args, **kwargs):
#         print(fname, "(", end = "")
#         print(', '.join( '% s = % r' % entry
#                          for entry in zip(argnames, args[:len(argnames)])), end = ", ")
#
#         print("args =", list(args[len(argnames):]), end = ", ")
#         print("kwargs =", kwargs, end = "")
#         print(")")
#
#     return inner_func
#
#
#
# @function_details
# def GFG(a, b = 1, *args, **kwargs):
#     pass
#
# GFG(1, 2, 3, 4, 5, d = 6, g = 12.9)
# GFG(1, 2, 3)
# GFG(1, 2, d = 'Geeks')
# Output:
#
# GFG (a = 1, b = 2, args = [3, 4, 5], kwargs = {‘d’: 6, ‘g’: 12.9})
# GFG (a = 1, b = 2, args = [3], kwargs = {})
# GFG (a = 1, b = 2, args = [], kwargs = {‘d’: ‘Geeks’})
#
#
