input_saree=(input("Enter the product details to store it into our data base:"))
input_saree=eval(input_saree)
red=[]
for i in input_saree:
    if 'red'in input_saree[i][0]:
        if 'Silk'in input_saree[i][1]:
            if input_saree[i][2]<10000:
              red.append(i)
    else:
        pass
print(red)
#or

# sarees=list(filter(lambda n:'red' in input_saree[n][0]
#         and input_saree[n][1]=='Silk' and input_saree[n][2]<=10000 ,input_saree))
# print(sarees)