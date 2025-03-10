#write a python program that acccepts an integer (n)and computes the value of n+nn+nnn.
#input:sample value of n is 5
#output:expected result:615
# n=input("enter the value of n:")
# a=n*2
# b=n*3
# result=int(n)+int(a)+int(b)
# print(result)

# from math import pi
# radius=float(input("enter the radius:"))
# if abs(radius)>0:
#      print("the area of the circle with radius %.1f is:%.14f"%(radius,pi*radius**2))

# s="""a string in which you "don't" have to use
# new line
# on tab ........is called as
# dash string --------->example
# """
# print(s)

#print("Twinkle,twinkle,little star,\n\thow i wonder what you are!\n\t\tup above the worlds so high,\n\t\tlike a diamond iin the sky.\nTwinkle,twinkle,little star,\n\thow i wonder what you are!")

#=======================================================
#07/01/2025
# i=1
# while i<=5:
#     print(i)
#     j=i
#     while j<i+1:
#         j+=0.1
#         print(j)
#     i+=1
#==============================================
# outter = 1
# while outter < 5:
#     print(outter)
#     inner = 0
#     while True:
#         inner += 1
#         print(f'{outter}.{inner}')
#         if inner == 9:
#             break
#     outter += 1

#===============================================

string1=input("enter the string:")
for i in range(len(string1)):
    if string1[i]==' ':
        str2=string1[(i+1):]+' '+string1[:i]
        break
print(str2)

