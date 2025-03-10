customer={'Sajid':120,'Roopesh':85, 'Koushik':50, 'Lakshmi':64, 'Sathvik':12}
ly_points=0 #global loyalty points
#function for coupon checking
def coupon_checking(coupon_code):
    if coupon_code=="123456": #check the code
        return True

customer_name=input("Please enter the customer name:")
if customer_name not in customer:
    print("New Customer")
else:
    pass

coupon=input("Do the customer has the coupon? Type y or n:")

if coupon=='y':
    coupon_code=input("Please enter the coupon code:")
    a=coupon_checking(coupon_code)
    if a==True:
        ly_points+=15
        pass
    else:
        print('coupon code is invalid')
amount=int(input("Enter the bill amount to be paid:"))
ly_points+=(amount//100)
if customer_name not in customer :
    customer.update({customer_name:ly_points})
else:
    for i in customer:
        if customer[i]==customer[customer_name]:
            customer[i]+=ly_points
            ly_points=customer[i]
            break
print("You have {} loyalty points in your account. Please pay Rs.: {}Thank you.".format(ly_points,amount))
dis_points=ly_points//100
if dis_points in range(1,100):
    print("Congratulations! you won Rs. {} cash back. You have to pay Rs.:  {} And remaining loyalty points in your account is: {}".format(dis_points*100,(amount-(dis_points*100)),((dis_points*100)-ly_points)))