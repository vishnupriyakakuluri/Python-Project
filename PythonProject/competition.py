# l=[]
# n=int(input("enter the length of the list:"))
# print("enter the elements:")
# for i in range(n):
#     value=int(input())
#     l.append(value)
# v=[]
# for i in range(n):
#     if l[i]+1 == l[i+1]:
#         v.extend(l[0],l[1])
#     a=len(v)
#
# test1:
# i/p=[100,500,501,503,1,2,101,200,201,202,203]
# o/p={4:[200,201,202,203]}
#
# test2:
# i/p=[1000,2000,80,81,89,82,83,84,85,86]
# o/p={5:[82,83,84,85,86]}

# def longest_contiguous_subsequence(lst):
#     lst = sorted(set(lst))  # Remove duplicates and sort
#     longest_subseq = []
#     current_subseq = [lst[0]]
#
#     for i in range(1, len(lst)):
#         if lst[i] == lst[i - 1] + 1:
#             current_subseq.append(lst[i])
#         else:
#             if len(current_subseq) > len(longest_subseq):
#                 longest_subseq = current_subseq
#             current_subseq = [lst[i]]
#
#     if len(current_subseq) > len(longest_subseq):
#         longest_subseq = current_subseq
#
#     return {len(longest_subseq): longest_subseq} if longest_subseq else {}
#
# # Test cases
# print(longest_contiguous_subsequence([100,500,501,503,1,2,101,200,201,202,203]))
# print(longest_contiguous_subsequence([1000,2000,80,81,89,82,83,84,85,86]))


#sarath question solution

# lst=[100, 200, 201, 202, 9, 201, 202, 203, 204, 205]
#
# dic = {}
# temp_list = []
# for i in range(len(lst)):
#     if not temp_list:
#         temp_list = [lst[i]]
#         j = lst[i]
#     else:
#         if j + 1 == lst[i]:
#             temp_list.append(lst[i])
#             j = lst[i]
#         else:
#             dic[i - len(temp_list)] = temp_list
#             temp_list = [lst[i]]
#             j = lst[i]
# if temp_list:
#     dic[len(lst) - len(temp_list)] = temp_list
# print(dic)
# count = 0
# ans = []
# for value in dic.values():
#     if count < len(value):
#         count = len(value)
#         ans = value
# print({count:ans})


#Anuroop question solution


# main=[]
# list=[0,1,0,3,2,0,2,1]
# lis=list.copy()
# rev_list=list[::-1]
# min_list=[]
# l=len(list)
# for j in range(l):
#     for i in range(j,l):
#         if list[j]<list[i]:
#             list[j]=list[i]
#     for i in range(j,l):
#         if rev_list[j]<rev_list[i]:
#             rev_list[j]=rev_list[i]
# rev_list=rev_list[::-1]
# for i in range(l):
#     if list[i]>rev_list[i]:
#         min_list.append(rev_list[i])
#     else:
#         min_list.append(list[i])
# for i in range(l):
#     main.append(min_list[i]-lis[i])
# print(main)
