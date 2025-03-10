# #ITERATORS-only benefit is memory
# #1ST METHOD
# a=[1,2,3,4,5,6,7]
#for i in a:print(i)
# b=iter(a)
# print(next(b))
# print(next(b))
# print(b.__next__())
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
#====================================================
# #2nd method
#
# class Test:
#     def __init__(self,a):self.a=a
#     def __iter__(self):
#         self.x=10
#         return self
#     def __next__(self):
#         x=self.x
#         if x>self.a:
#             print('bye')
#             raise StopIteration
#         self.x=x+1
#         return x
# for i in Test(15):print(i)
#============================================================
# #Third infinite loop
#
# int()
# inf=iter(int,1)
# print(next(inf))
# print(next(inf))
# print(next(inf))

#=============================================================
#GENERATORS-yield key word

# #Method 1
# def gen(n):
#     a=1
#     while a<=n:
#         sq=a**2
#         yield sq
#         a+=1
# value=gen(10)
# print(value)
# for i in value:print(i)

#=============================================================
# #generator method only
#
# def gen():
#     yield 1,2
#     yield 3
#     yield 5
#     av=2   #no use of this line
# a=gen()
# for i in a:print(i)

#===========================================================
#generator-reversing string


# def gen(str):
#     a=len(str)
#     for i in range(a-1,-1,-1):
#         yield str[i]
# for i in gen("vishnupriya"):print(i)

#============================================================
# #infinite even numbers using yield
#
# def all_even():
#     n=0
#     while True:
#         yield n
#         n+=2
# a=all_even()
# for i in a:print(i)
#=========================================================
#pipelining generator-> fibonacci+square+sum
# def fib(n):
#     x,y=0,1
#     for _ in range(n):
#         x,y=y,x+y
#         yield x
# def square(n):
#     for i in n:
#         yield i**2
# print(sum(square(fib(10))))

#========================================================

# #send()
# def ngen(n):#10
#     num=yield#5 #so every time new value can be sent
#     #only 1st time it will work (num=5)
#     print('num1=',num)
#     while num<n:#12
#         print('a=')
#         num=yield num #=5 1st iter
#         print('num2=',num)
#         num+=1 #in 2nd iter
#         print('num3=',num)
#     else:yield
# g=ngen(10)
# next(g) #need in order to send value to generate
# #just like iter and next... yield and next will let send to send the new new values every time
# #print(g.send(None))
# print(g.send(5)) #num values
# print(g.send(2))
# print(g.send(5))
# print(g.send(11))


