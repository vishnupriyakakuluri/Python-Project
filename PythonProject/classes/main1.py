# # For main function
#
# print("Hello")
#
#
# # Defining main function
# def main1():
#     print("hey there")
#
#
# # Using the special variable
# # __name__
# if __name__ == "__main__":
#     main1()
#
# """o/p:
# Hello
# hey there"""
# ...........................................
# Mod1:
#
#
# def main():
#     print("hi")
#
#
# print("where is my print1")
# if __name__ == "__main__":
#     main()
#
# Mod2:
# import mod1
#
# print(__name__)
# print("hay" + __name__)
# ...........................................
# # create a module
# # in file1
# print("File1 __name__ = %s" % __name__)
#
# if __name__ == "__main__":
#     print("File1 is being run directly")
# else:
#     print("File1 is being imported")
#
# """o/p:
# File1 __name__ = __main__
# File1 is being run directly"""
# --------------------------------------------------------------
# # in file2
# import file1
#
# print("File2 __name__ = %s" % __name__)
#
# if __name__ == "__main__":
#     print("File2 is being run directly")
# else:
#     print("File2 is being imported")
#
# """o/p:
# File1 __name__ = mod13
# File1 is being imported
# File2 __name__ = __main__
# File2 is being run directly"""
# ------------------------------------------------------------------------
#
#
#
#
