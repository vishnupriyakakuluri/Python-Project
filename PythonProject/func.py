# def dee():
#     print("hi")
#     print("hello")
# dee()
# -----------------------
# #Arguments
#
# def pow(x,y=0):
#     z=x**y
#     print(z)
#     print(x**y)
#     return x**y
# print(pow(3,4))
# ------------------------
# #Multiple Arguments
#
# def a1(*dee):
#     print(dee)
#
# a1(1.1,2,3,4,5,6,5.7)
#
# -------------------------
# #Return
#
# def sq(x):
#     return x*x
#
# print(sq(4))
# -------------------------
# #Multiple Return
#
# def addmul(x,y):
#     a=x+y
#     b=x*y
#     return a,b
#
# add=addmul(5,4)
# mul=addmul(y=4,x=2)
# print(add,mul)
# ----------------------------
# #recursive function
#factorial 5=5*4*3*2*1
# def fact(n):#0
#     if n==0 or n==1: return 1
#     return n*fact(n-1)#5*4*3*2*1*1
# print(fact(5))
#-----------------------------------
#nested functions
#----------------------------------------
# def outside(a):
#     def inside():return a
#     return inside()
# print(outside(1))
#
# #nested functions
# def outside(a):
#     def inside():return a()+1
#     return inside
# def onemore():return 6
# haha=outside(onemore)
# print(haha)
# print(haha())
#
# sum=lambda a,b:a+b
# c=sum(1,2)
# print(c)
# print(sum('a','b'))
#
# #filter
# num=[1,2,3,4,5,6,7,8]
# even1=list(filter(lambda n:n%2==0,num))
# print(even1)
# color=['red','red','pink','brown','black','red','merun red','dark red']
# red=list(filter(lambda n:'red' in n,color))
# print(red)
#
# #map
# even2=list(map(lambda n:n+3,num))
# print(even2)
#
# #reduce
# from functools import reduce
# a=reduce(lambda a,b:a+b,num)
# print(a)

'''

num=[1,2,3,4,5,6,7,8]
print(sum(num))

#factorial
#5=5*4*3*2*1*0

def fact(n):
    if n==0:return 1
    return n*fact(n-1)#=5*4*3**2*1*1
n=int(input())
print(fact(n))#5

import math
print(math.factorial(0))
'''
#=========================================================


