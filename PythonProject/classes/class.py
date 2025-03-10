# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

#=======================================
# class MyNewClass:
#     '''This is a docstring. I have created a new class'''
#     pass

#========================================
# class Person:
#     "This is a person class"
#     age = 10
#     def greet(self):
#         print('Hello')
# print(Person.age)
# print(Person.greet)
# print(Person.__doc__)
# harry = Person()
# harry.greet()

#===========================================
# #create attribute
# class ComplexNumber:
#     def __init__(self, r=0, i=0):
#         self.real = r
#         self.imag = i
#     def get_data(self):
#         print(f'{self.real}+{self.imag}j')
# num1 = ComplexNumber(2, 3)
# num1.get_data()
# num2 = ComplexNumber(5)
# #create a new attribute
# num2.attr = 10
# # # Output: (5, 0, 10)
# print((num2.real, num2.imag, num2.attr))
# # # but c1 object doesn't have attribute 'attr'
# # # AttributeError: 'ComplexNumber' object has no attribute 'attr'
# #print(num1.attr)

#=========================================================

# class dee1:
#     def fun():print('hi')
# obj=dee1
# obj.name='Vishnu'
# obj.id=1
# obj2=dee1
# obj2.name='Rupesh'
# obj2.id=2
# print(obj.name,obj.id,obj.fun())
# print(obj2.name,obj2.id,obj2.fun())

#=========================================================

# # create addNumbers static method
# class Calculator:
#     def addNumbers(x, y):
#         return x + y
#
#
# Calculator.addNumbers = staticmethod(Calculator.addNumbers)
# # or a=staticmethod(Calculator.addNumbers)
# print('Product:', Calculator.addNumbers(15, 110))
# -------------------------------
#
#
# # create addNumbers static method
# class Calculator:
#     @staticmethod
#     def addNumbers(x, y):
#         return x + y
#
#
# print('Product:', Calculator.addNumbers(15, 110))
# -------------------------------
# # use of class method and static method.
# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, lname, fname, year):
#         name = lname + fname
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', ' xyz', 1996)
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# print(Person.isAdult(12))
# -----------------------------------
#
#
# # object
# class Dog:
#     # attribute
#     attr1 = "mammal"
#     attr2 = "dog"
#
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
#
#
# Rodger = Dog()
# # Labrador Retriever,German Shepherd Dog,Golden Retriever,Bulldog,Beagle
# print(Rodger.attr1)
# Rodger.fun()
# -----------------------------------
#
#
# self
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
#
#
# p1 = Person("John", 36)
# p1.myfunc()
# p1.age = 40
# print(p1.age)
# del p1.age
# del p1
# del Person.myfunc
# del p1
# p2 = Person("dee", 36)
# p2.myfunc()
# # attribute error, once deleted always deleted(myfunc())
# p2
#
#
# class Person:
#     pass
#
#
# ---------------------
#
#
# # Inheritance
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#     # child class Dog inherits the base class Animal
#
#
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
#
#
# d = Dog()
# d.bark()
# d.speak()
# -----------------------------------
#
#
# # Inheritance
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# x = Person("John", "Doe")
# x.printname()
#
#
# class Student(Person):
#     pass
#
#
# x = Student("Mike", "Olsen")
# x.printname()
# -------------------------------
#
#
# continue by improving
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#
#
# # or super().__init__(fname, lname)
# x = Student("Mike", "Olsen")
# x.printname()
# -------------------------
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         # self.address=address
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#
#     # or self.graduationyear = 2019
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
#
# a = Student("Mike", "Olsen", 2019)
# print(a.lastname)
# a.welcome()
# ---------------------------
#
#
# # How inheritance works with static method?
# class Dates:
#     def __init__(self, date):
#         self.date = date
#
#     def getDate(self):
#         return self.date
#
#     @staticmethod
#     def toDashDate(date):
#         return date.replace("/", "-")
#
#
# class DatesWithSlashes(Dates):
#     def getDate(self):
#         return Dates.toDashDate(self.date)
#
#
# date = Dates("15-12-2016")
# dateFromDB = DatesWithSlashes("15/12/2016")
# if (date.getDate() == dateFromDB.getDate()):
#     print("Equal")
# else:
#     print("Unequal")
# -----------------------
#
#
# # Method Overriding in Python
# # notice that __init__() method was defined in both classes, Triangle as well Polygon.
# # When this happens, the method in the derived class overrides that in the base class.
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n): print("Side", i + 1, "is", self.sides[i])
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 3)
#
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         # print(s)
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         print('The area of the triangle is %0.2f' % area)
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()
# # check
# print(isinstance(t, Triangle))
# print(isinstance(t, int))
# print(isinstance(t, object))
# print(issubclass(Polygon, Triangle))
# print(issubclass(Triangle, Polygon))
# print(issubclass(bool, int))
#
# Output: Enter
# side
# 1: 3
# Enter
# side
# 2: 5
# Enter
# side
# 3: 7
# Side
# 1 is 3.0
# Side
# 2 is 5.0
# Side
# 3 is 7.0
# The
# area
# of
# the
# triangle is 6.50
# ------------------------------------------
#
# --------------------------------------
#
#
# # Multi level
# class Base(object):
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#
# class Child(Base):
#     def __init__(self, name, age):
#         Base.__init__(self, name)
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#
# class GrandChild(Child):
#     def __init__(self, name, age, address):
#         Child.__init__(self, name, age)
#         self.address = address
#
#     def getAddress(self):
#         return self.address
#
#
# g = GrandChild("deepthi", 32, "Bangalore")
# print(g.getName(), g.getAge(), g.getAddress())
# ----------------------------------------------
#
#
# # multiple
# class Calculation1:
#     def Summation(self, a, b):
#         return a + b
#
#
# class Calculation2:
#     def Multiplication(self, a, b):
#         return a * b
#
#
# class Derived(Calculation1, Calculation2):
#     def Divide(self, a, b):
#         return a / b
#
#
# d = Derived()
# print(d.Summation(10, 20))
# print(d.Multiplication(10, 20))
# print(d.Divide(10, 20))
# ----------------------------------------------
# # abstract class
# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#     def mileage(self):
#         pass
#
#
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
#
#
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph ")
#
#
# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph ")
#
#
# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph ")
#
#
# t = Tesla()
# t.mileage()
# r = Renault()
# r.mileage()
# s = Suzuki()
# s.mileage()
# d = Duster()
# d.mileage()
# -----------------------
# # abstract class
# from abc import ABC
#
#
# class Polygon(ABC):
#     def sides(self):
#         pass
#
#
# class Triangle(Polygon):
#     def sides(self):
#         print("Triangle has 3 sides")
#
#
# class Pentagon(Polygon):
#     def sides(self):
#         print("Pentagon has 5 sides")
#
#
# class Hexagon(Polygon):
#     def sides(self):
#         print("Hexagon has 6 sides")
#
#
# class square(Polygon):
#     def sides(self):
#         print("I have 4 sides")
#
#
# t = Triangle()
# t.sides()
# s = square()
# s.sides()
# p = Pentagon()
# p.sides()
# k = Hexagon()
# k.sides()
# --------------------------
# # abs class3
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def move(self):
#         pass
# class Human(Animal):
#     def move(self):
#         print("I can walk and run")
# class Snake(Animal):
#     def move(self):
#         print("I can crawl")
# class Dog(Animal):
#     def move(self):
#         print("I can bark")
# class Lion(Animal):
#     def move(self):
#         print("I can roar")
#
#
# R = Human()
# R.move()
# K = Snake()
# K.move()
# R = Dog()
# R.move()
# K = Lion()
# K.move()
# --------------------
#
#
# # abs class4
#
# class parent:
#     def geeks(self):
#         pass
#
#
# class child(parent):
#     def geeks(self):
#         print("child class")
#
#
# # Driver code
# print(issubclass(child, parent))
# print(isinstance(child(), parent))
# ------------------
# # abs class5+ inheritance
# import abc
# from abc import ABC, abstractmethod
# #
# #
# class R(ABC):
#     def rk(self):
#         print("Abstract Base Class")
#
#
# class K(R):
#     def rk(self):
#         super().rk()
#         print("subclass ")
#
#
# # Driver code
# w = R()
# w.rk()
# r = K()
# r.rk()
# ----------------------------
#
#
# # private member
# class C(object):
#     def __init__(self):
#         self.c = 21
#         self.__d = 42
#
#
# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)
#
#
# object1 = D()
# print(object1.d)
# -------------------------------------------
#
#
# # __init__, sublclassing
# class Base1(object):
#     def __init__(self):
#         self.str1 = "hcl"
#         print("Base1")
#
#
# class Base2(object):
#     def __init__(self):
#         self.str2 = "training"
#         print("Base2")
#
#
# class Derived(Base1, Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#
#     def printStrs(self):
#         print(self.str1, self.str2)
#
#
# ob = Derived()
# ob.printStrs()
# -------------------------------------------
#
#
# # How to access parent members in a subclass?
# # (object)is nothing
# class Base(object):
#     def __init__(self, x):
#         self.x = x
#
#
# class Derived(Base):
#     def __init__(self, x, y):
#         Base.x = x
#         # or super(Derived, self).__init__(x)
#         self.y = y
#
#     def printXY(self):
#         print(Base.x, self.y)
#
#
# d = Derived(10, 20)
# d.printXY()
# ---------------------------------
# # Abstract class
# from abc import ABC, abstractmethod
#
#
# class A(ABC):
#     def dee(self): print('this is not correct')
#
#
# class B(A):
#     def dee(self):
#         super().dee()
#         print('but acceptable')
#
#
# z = A()
# z.dee()
# r = B()
# r.dee()
# -----------------------------------------------
#
#
# # overloading
# # Overloading
# class bill:
#     def __init__(self, m, u):
#         self.m = m
#         self.u = u
#
#     def __add__(self, other):
#         m = self.m + other.m
#         u = self.u + other.u
#         bill1 = bill(m, u)
#         return bill1
#     # def __gt__(self, other):
#
#
# a1 = bill(5000, 15000)
# a2 = bill(25000, 5000)
# a = a1 + a2
# print('Your bill=', a.u)
# print('My bill=', a.m)
#
# a, b, c = 2, 3, 'Animesh'
# print(a + b)
# print(str(a) + c)