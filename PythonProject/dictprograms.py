#expected output:[1,'h',3,'f',5,'d',7,'b']
#input:
# a=[1,2,3,4,5,6,7,8,9,10]
# b='abcdefghi'
# l=[]
# c=-2
# for i in range(0,len(a),2):
#     l.append(a[i])
#     if b[c] in b:
#         l.append(b[c])
#         c -= 2
#     else:
#         break
# print(l)


# a=[1,2,3,4,5,6,7,8,9,10]
# b='abcdefghi'
# l=[]
# c=a[::2]
# d=b[len(b)-2::-2]
# if len(c)>len(d):
#     for i in range(len(d)):
#         l.append(c[i])
#         l.append(d[i])
# print(l)
#=============================================================
# 1.Convert this to dict. Use only dict comprehension.
# string = "A - 13, B - 14, C - 15"

# string = "A - 13, B - 14, C - 15"
# result = {i.split(' - ')[0]: int(i.split(' - ')[1]) for i in string.split(', ')}
# print(result)
#==============================================================
# 2.Convert this to dict. Use only dict comprehension.
# Note both key and value should be of int type.
# string = "11 - 13, 12 - 14, 13 - 15"

# string="11 - 13, 12 - 14, 13 - 15"
# result={int(i.split(' - ')[0]):int(i.split(' - ')[1]) for i in string.split(', ')}
# print(result)

# 3. #inputs:
# l1=[4,5,6,7]
# l2=[2,3,5,6,7,9,2]
# output-> lo=[6, 8, 1, 4, 8, 9, 2]
#l0=l1+l2 with carry

# l1=[4,5,6,7]
# l2=[2,3,5,6,7,9,2]
# l0=[l1[i]+l2[i] if i<4 else l2[i] for i in range(len(l2))]
# print(l0)

# l1=[4,5,6,7]
# l2=[2,3,5,6,7,9,2]
# l0=[]
# max_len=max(len(l1),len(l2))
# l1=l1+[0]*(max_len-len(l1))
# l2=l2+[0]*(max_len-len(l2))
# carry=0
# for i in range(max_len):
#     total=l1[i]+l2[i]+carry
#     l0.append(total%10)
#     carry=total//10
# if carry:
#     lo.append(carry)
# print(l0)

# def add_lists_with_carry(l1, l2):
#     # Make both lists equal in length by padding the shorter one with zeros
#     max_len = max(len(l1), len(l2))
#     l1 = [0] * (max_len - len(l1)) + l1
#     l2 = [0] * (max_len - len(l2)) + l2
#     # Initialize the result list and carry
#     lo = []
#     carry = 0
#     # Perform the addition with carry
#     for i in range(max_len - 1, -1, -1):
#         total = l1[i] + l2[i] + carry
#         lo.append(total % 10)  # Add the last digit to the result
#         carry = total // 10  # Carry over the tens place
#     # If there's a carry left, append it to the result
#     if carry:
#         lo.append(carry)
#     # Reverse the result list to get it in the correct order
#     lo.reverse()
#     return lo
# l1 = [4, 5, 6, 7]
# l2 = [2, 3, 5, 6, 7, 9, 2]
# result = add_lists_with_carry(l1, l2)
# print("Result:", result)

#=============================================================


# fruits=['apple','banana','cherry']
# dict1={i:len(i) for i in fruits}
# print(dict1)

# original={'a':1,'b':2,'c':3}
# dict1={j:i for i,j in original.items()}
# print(dict1)

# keys=['name','age','gender']
# values=['alice',25,'female']
# d={keys[i]:values[i] for i in range(3)}
# print(d)

# numbers=range(1,11)
# d={i:'even' if i%2==0 else 'odd' for i in numbers}
# print(d)

# string='hello world'
# d={i:string.count(i) for i in string}
# print(d)





# d={chr(i):i for i in range(65,91)}
# print(d)

# nested={'a':{'b':1,'c':2},'d':{'e':3,'f':4}}
# d={k1+'_'+k2:v2 for k1,v1 in nested.items}

