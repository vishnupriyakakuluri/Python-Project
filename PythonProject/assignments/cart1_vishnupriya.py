from abc import ABC,abstractmethod
class store1(ABC):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @abstractmethod
    def cart(self,a,b):
        pass
class store(store1):
    def cart(self,a,b):
        print("cart:")
        print("product:quantity:price in rupees:")
        print(a,':',b,':',dict[a]*b)
        print('Thank you')
print("product:price in rs")
dict={'Sugar':50,'Rice':55,'Wheat flour':55,'Toor dal':150,'Rava':70}
for i in dict:
    print(i,':',dict[i])

a=input('Enter the item name to add it to the cart:')
for i in dict:
    if a in dict:
        pass
    else:
        print('Please enter the existing products name in the list')
        exit()
b=int(input("enter the quantity in kgs:"))
if b>0:
    obj1=store(a,b)
    obj1.cart(a,b)
else:
    print('Thank u')
    exit()