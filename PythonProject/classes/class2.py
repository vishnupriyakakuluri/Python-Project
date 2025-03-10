# # 2 objs both are same:bez not declasring the objects clearly to the class: obj=dee1()
# class dee1:
#     def fun(): print('hi')
#
#
# obj = dee1
# obj.name = 'Vishnu'
# obj.id = 1
# obj2 = dee1
# obj2.name = 'Rupesh'
# obj2.id = 2
# print(obj.name, obj.id, obj.fun())
# print(obj2.name, obj2.id, obj2.fun())

# # o/p:
# hi
# Rupesh
# 2
# None
# hi
# Rupesh
# 2
# None
# ...........................
#
#
# # Corrected one
#
# class dee1:
#     def fun(self): return 'hi'
#
#
# obj = dee1()
# obj.name = 'Vishnu'
# obj.id = 1
# obj2 = dee1()
# obj2.name = 'Rupesh'
# obj2.id = 2
# print(obj.name, obj.id, obj.fun())
# print(obj2.name, obj2.id, obj2.fun())

# # o/p:
# Vishnu
# 1
# hi
# Rupesh
# 2
# hi
# .............................
#
# # instanciation
# # __init__
# class durga:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         a = 3
#         self.a1 = 2
#
#     def fun(self): print(self.name, self.id)
# o = durga('Durga', 1)
# o.fun()
# t = durga('Ajay', 2)
# t.fun()
# def dee(a, b):
#     return a + b
#
#
# dee(2, 3)

# ........................
