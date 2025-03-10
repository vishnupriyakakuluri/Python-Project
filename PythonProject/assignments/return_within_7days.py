from module1 import returned
data={'Narendra':['Toy1',499],
'Sujata': 	['Pink saree',7500],
'Shritan ':['T-shirt',500]
}
print('Please enter the details to return the product.')
name=input("Enter your name:")
pro_name=input("Enter the product name:")
date=input('When did you purchase the product?\nPlease enter the date in mm/dd/yy format:')
returning=returned(date)
if name in data.keys() and pro_name == data[name][0]:
    if returning:
        print('Product:',pro_name,'will be collected from the delivered address and amount:',data[name][1] ,
                  'will be returned to your account.\nThank you.')
    else:
        print('Sorry! the product cannot be returned\nThank you.')
else:
    print('You have not purchased that product recently with us.\nThank you.')
