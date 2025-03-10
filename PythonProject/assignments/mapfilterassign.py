# map, filter and lambda
#
# Capitalize names starting with the letter 'A' from the list
# ['Alice', 'Bob', 'Anna', 'Tom'].
# Output:['ALICE', 'ANNA']
# a=['Alice', 'Bob', 'Anna', 'Tom']
# # b=list(filter(lambda x:x[0]=='A',a))
# # result=list(map(lambda x:x.upper(),b))
# result=list(map(lambda x:x.upper(),(filter(lambda x:x[0]=='A',a))))
# print(result)

#==================================================
# Find the square root of all positive numbers in
# [-4, 9, 16, -1, 25].
# Output:[3.0, 4.0, 5.0]
# l=[-4, 9, 16, -1, 25]
# result=list(map(lambda x:x**0.5,(filter(lambda x:x>0,l))))
# print(result)
#=====================================================
# Filter words containing the letter 'e' and convert them to uppercase.
# Words: ['apple', 'orange', 'pear', 'banana'].
# Output:['APPLE', 'ORANGE', 'PEAR']
# Words=['apple', 'orange', 'pear', 'banana']
# a=list(map(lambda x:x.upper(),(filter(lambda x:'e' in x,Words))))
# print(a)
#===========================================================
# From the list of tuples [(1, 5), (3, 6), (4, 4), (2, 9)], filter tuples where the second element is greater than the first and compute their product.
# Output:[5, 18, 18]
# l=[(1,5),(3,6),(4,4),(2,9)]
# filter_list=list(filter(lambda x:x[0]<x[1],l))
# result=list(map(lambda x:x[0]*x[1],filter_list))
# print(result)

# l=[(1,5),(3,6),(4,4),(2,9)]
# result=list(map(lambda x:x[0]*x[1],filter(lambda x:x[0]<x[1],l)))
# print(result)

#==========================================================
# Filter palindromes from the list ['madam', 'hello', 'radar', 'world', 'level'].
# Output:['madam', 'radar', 'level']
# list1=['madam', 'hello', 'radar', 'world', 'level']
# result=list(filter(lambda x:x==x[::-1],list1))
# print(result)

# list1=['madam', 'hello', 'radar', 'world', 'level']
# result=list(filter(lambda x:x==''.join(reversed(x)),list1))
# print(result)

#===============================================================
# Find the lengths of words longer than 4 characters in the list
# ['apple', 'is', 'tasty', 'cherry', 'banana'].
#output: [5, 5, 6]
# words = ['apple', 'is', 'tasty', 'cherry', 'banana']
# result=list(map(lambda x:len(x),filter(lambda x:len(x)>4,words)))
# print(result)
#================================================================
# Filter out vowels from the list
# ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z'].
# Output:['a', 'e', 'i', 'o', 'u']

# a=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
# result=list(filter(lambda x:(x=='a'or x=='e'or x=='i'or x=='o'or x=='u'),a))
# print(result)
#===========================================================
# Find all numbers in the range 1-50 that are divisible by both 3 and 5.
# Output: [15, 30, 45]
# numbers=range(1,51)
# result=list(filter(lambda x:x%3==0 and x%5==0,numbers))
# print(result)

#==========================================================
# For odd numbers in 0-9, calculate the sum of their squared digits.
# Output:[1, 9, 25, 49, 81]

# numbers=range(0,10)
# result=list(map(lambda x:x*x,filter(lambda x:x%2==1,numbers)))
# print(result)

#==============================================================
# Filter numbers divisible by 4 in the range 0-20 and divide them by 2.
# Output:[0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
# numbers=range(0,21)
# result=list(map(lambda x:x/2 ,filter(lambda x:x%4==0,numbers)))
# print(result)

#============================================================
# Remove duplicate numbers from [2, 3, 2, 4, 5, 4] and calculate their squares.
# Output: [4, 9, 16, 25]
# a=[2, 3, 2, 4, 5, 4]
# def fun(a):
#     if a not in list1:
#         list1.append(a)
#         return True
#     else:
#         return False
# list1=[]
# result=list(map(lambda x:x**2 ,filter(fun,a)))
# print(result)

#================================================================
# Filter prime numbers in the range 0-49.
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# numbers=range(0,50)
# def fun(n):
#     if n==0 or n==1:
#         return False
#     if n==2:
#         return True
#     l=(n//2)+1
#     for i in range(2,l):
#         if n%i==0:
#             return False
#     else:
#         return True
# result=list(filter(fun,numbers))
# print(result)

#=================================================================
# Calculate the base-10 logarithm of numbers greater than 0 in
# [1, 10, 100, 0, 1000].
# Output:[0.0, 1.0, 2.0, 3.0]

# import math
# a=[1, 10, 100, 0, 1000]
# def fun(a):
#     if a>0:
#         return True
#     else:
#         return False
# result=list(map(lambda x:math.log10(x),filter(fun,a)))
# print(result)
#============================================================