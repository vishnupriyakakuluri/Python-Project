# creating a empty list
# a=[]
# b=list()


# printing lists
# a=['a',"b",1,2,3,[3,4],[5,6]]
# b=[]
# print(a)
# print(a[5][1])
# print(b)

#list comprehensions

# c=[i for i in range(0,10,2)]
# print(c)
# d=list(range(0,10,2))
# print(d)
# e=list(i for i in range(10))
# print(e)


#string split function

# e="hi,hello,well"
# f=e.split(',')
# print(f)


# g="hello"
# h=list(g)
# print(h)
#
# i=12345
# j=[int(i) for i in str(i)]
# print(j)
#
# dict={'a':1, 'b':2, 'c':3}
# k=list(dict.keys())
# print(k)
# l=list(dict.values())
# print(l)
#
# m=[1,2,3,4]
# n=[5,6,7,8]
# m.append(9)
# print(m)
# m.extend(n)
# print(m)

# m=[1,2,3,4]
# m.insert(10,'add')
# print(m)
# print(m.index(3))
# m.insert(3+2,'duck')
# print(m)
#
# m=[1,2,3,4,5,6,7]
# m.remove(6)
# m.pop()
# m.pop(1)
# print(m)
# m.clear()
# print(m)
#
# --------------------------------------------Assignment--------------------------------------------------
# sort


#m=[1,7,4,6,99,33,76,44]
# m.sort()
# print(m)
# m.sort(reverse=True)
# print(m)
# --------------------
# max & min
#
# o=max(m)
# print(o)
# p=min(m)
# print(p)
# --------------------
# Count
#
# q=['a','b', 'a', 'c', 'a']
# r=q.count('a')
# print(r)
# -----------------------------
# change the values
# a=[1,2,3,4]
# a[1:3]=[5,6]
# ----------------------------------
# repeatation
# a=[1,2,3]
# print(a*3)
# print(a)
# #or
# b=[1,2,3]*2
# print(b)
# print([5,7,8]*5)
# --------------------------------
# reverse
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a.reverse())
# print(a)
# ----------------------------
# copy
# b=a
# b=a.copy()
# c=a[1:3]
# ----------------------------
# delete
# del a[0]
# del a[1:3]
# del a
# --------------------------------
# a,b=2,'vishnu'
# if a>b:print("hi")
# else:print("bye")
