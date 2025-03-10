products=input("Enter the name of products stored in the cotton box:")
separate_products=products.split(',')
teddy=[]
for i in separate_products:
    if 'teddy' in i:
        teddy.append(i)
print("""Dear Surya,
Total {} teddies are there. And, here they are:""".format(len(teddy)))
print(teddy)