class ecommerce:
    def __init__(self):
        pass
    def cart(self):
        for i in dict:
            for j in dict[i]:
                if a == j:
                    print('these are the', i, 's available')
                    for i in dict[i]:
                        print(i)
                    break
                else:
                    pass
dict={'cloth':['red tshirt','trending tshirt','branded tshirt','cotton tshirt'],
'toy':['Dr. set','kitchen set','teddy','unicorn','fishing'],
'furniture':['chair','table','sofa']}
for i in dict:
    print(i, ':', dict[i])
a = input("enter the product:")
for i in dict:
    for j in dict[i]:
        if a==j:
            obj = ecommerce()
            obj.cart()
            exit()
else:
    print('No matching item found')