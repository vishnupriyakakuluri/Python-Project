# transposed=[]
# matrix=[[1,2,3,4],[5,6,7,8]]
# for i in range(len(matrix[0])):
#     transposed_row=[]
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

#==============================================================================
#itemgetter function

# a=[(1,'vishnu'),(2,'priya'),(3,'vinod')]
# from operator import itemgetter
# li=list(map(itemgetter(1),a))
# print(li)

#======================================================================

# def merge(dict1,dict2):
#     return (dict2.update(dict1))
# dict1={'a':10,'b':8}
# dict2={'d':6,'c':4}
# print(merge(dict1,dict2))
# print(dict2)
#=====================================================================
# r=int(input("enter the no.of rows:"))
# c=int(input("enter the no.of columns:"))
# matrix=[]
# for i in range(r):
#     row=[]
#     for j in range(c):
#         ele=int(input())
#         row.append(ele)
#     matrix.append(row)
# print(matrix)
#====================================================================