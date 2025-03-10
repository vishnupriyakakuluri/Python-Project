# a=open("deepthi.txt","w+")
# for i in range(10):
#     a.write("line %d\r\n" % (i+1))
# a.close()
# f=open("deepthi.txt", "a+")
# for i in range(2):
#     f.write("appended %d\r\n" % (i+1))
# f.close()
# f=open("deepthi.txt", "r")
# if f.mode=='r':
#     contents=f.read()
#     print(contents)
#============================================================
# file exists
# from os import path
# print(path.exists("deepthi.txt"))
# print(path.isfile("deepthi.txt"))
# print(path.isdir("deepthi.txt"))

#==========================================================
#pathlib

# import pathlib
# a=pathlib.Path("deepthi.txt")
# print(a)
# if a.exists():
#     print("file exists")
# else:
#     print("file not exist")
#======================================================
#Write line and read line

# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.write("Hello \n")
# file1.writelines(L)
# file1.close()
# #
# file1 = open("myfile.txt", "r+")
# print("Output of Read function is ")
# print()
# print()
# print(file1.read())
#================================================================

# seek(n) takes the file handle to the nth
# bite from the beginning.
# file1 = open("myfile.txt", "r")
# file1.seek(0)
# print("Output of Readline function is ")
# print(file1.readline())
# print()
# .........................
# file1.seek(0)
# # To show difference between read and readline
# print("Output of Read(9) function is ")
# print(file1.read(9))
# # read(starts with 1 and reads till that position-1)
# file1.seek(0)
# ................................
# # readlines function
# print("Output of Readlines function is ")
# print(file1.readlines())
# file1.close()
# ......................
# # readlines function
# print("Output of Readlines function is ")
# print(file1.readlines(2))
# file1.close()
# #