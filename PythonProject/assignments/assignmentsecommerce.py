# from datetime import datetime, timedelta
# today_date = datetime.strptime("12/01/22", "%m/%d/%y")
# products = {
#     1: {"name": "Soap", "expiry_date": today_date + timedelta(days=30)},
#     2: {"name": "Shampoo", "expiry_date": today_date - timedelta(days=5)},
#     3: {"name": "Tooth paste", "expiry_date": today_date - timedelta(days=10)},
#     4: {"name": "Ready juice", "expiry_date": today_date + timedelta(days=20)},
#     5: {"name": "Chips", "expiry_date": today_date + timedelta(days=15)},
# }
# def check_expiry(product_code):
#     if product_code in products:
#         product = products[product_code]
#         product_name = product["name"]
#         expiry_date = product["expiry_date"]
#         if expiry_date < today_date:
#             return f"Product name: {product_name}\nExpired"
#         else:
#             return f"Product name: {product_name}\nGood to sale"
#     else:
#         return "Enter the existing product code."
#
# # Main program loop
# print("Welcome to ABC super market's inspection portal")
# print(f"Today's Date is:{today_date.strftime('%m/%d/%y')}")
# while True:
#     try:
#         product_code = int(input("Enter the product code: "))
#         result = check_expiry(product_code)
#         print(result)
#         if result == "Enter the existing product code.":
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid product code.")
#         break

#======================================================================

# """Discount coupon
# Ravi has an online sweets store called ‘XYZ’.
# He wants to announce discount on the occasions of Christmas and new year.
# He has already distributed coupon codes amongst his customers.
# Please help him by writing piece of code which will be reducing
# the payable amount by the customer only if the coupon code is correct.
# Please note the coupon codes are case sensitive.
#  Descriptions of coupon codes:
# 1.	Please consider the payable amount by the customer  is Rs. 1500/-.
# 2.	If the coupon code is 'CDEC01' then reduce Rs. 500/- from payable amount.
# 3.	If the coupon code is 'ONEJAN02' then reduce half of the price from payable amount.
# 4.	If the coupon code is '2234150' then display the message that the customer has earned 1000 loyalty points and don’t reduce any amount  from payable.
# """
# def discount(s,a):
#     if s=="CDEC01":
#         a-=500
#         print("successfully applied the coupon code. Please pay {}/-".format(a))
#     elif s=="ONEJAN02":
#         a//=2
#         print("successfully applied the coupon code. Please pay {}/-".format(a))
#     elif s=="2234150":
#         print("Congratulations! You got 1000 loyalty points for shopping with us. Please pay {}/-".format(a))
#     else:
#         print("Invalid Coupon Code")
#         print("Please pay Rs.{}".format(a))
#
# i=1
# while(i<100000000000000):
#     print("Sample Case {}:".format(i))
#     print("WELCOME TO ONLINE SHOPPING")
#     print("Your cart is not empty.")
#     a=1500
#     print("You have to pay Rs. 1500/-")
#     print("Do you have a coupon?")
#     coupon=input()
#     if coupon=='y':
#         s=input("Enter the Coupon Code:")
#         discount(s,a)
#         print()
#     elif coupon=='n':
#         print("Please pay Rs.{}".format(a))
#     i+=1
#

#=====================================================================

"""Customer sign in
As you know everyone has to sign in by giving valid details to any online shopping site to shop.
So that these data will be stored in shopping site permanently
which will help sellers to know their customers better and customers need not to enter their details.
Being a programmer write a program which will act as:
1.	A sign in form which will take the basic details of a customer
2.	Validate the data entered
3.	If the data entered is wrong ask the customer to re-enter  n no. of times until they enter a valid data.
4.	Finally accept only the valid data.
Conditions for valid fields:
1.	Full name.
2.	Address: in 3 lines
3.	Email: A email ID  should have ‘@’ symbol and a domain name to be valid.
4.	Card:16 digits
5.	GST no.:8 digit and 7 alphabets
"""
# import re
# def validate_Fullname(Full_name):
#    if len(Full_name)>0:
#       return True
#    else:
#       return False
# def validate_address(address):
#    if len(address)==3:
#       return True
#    else:
#       return False
#
# def validate_email(email):
#    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#    if re.match(email_regex, email):
#       return True
#    else:
#       return False
#
# def validate_cardnumber(card_no):
#    if len(card_no)==16 and card_no.isdigit():
#       return True
#    else:
#       return False
# def validate_gst_no(gst_no):
#    gst_regex = r'^[0-9]{2}[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}[0-9]{1}[A-Za-z]{1}[0-9]{1}$'
#    if re.match(gst_regex, gst_no):
#       return True
#    else:
#       return False
#
# i=1
# while (i<1000):
#    print("""Sample case {}:
# Please fill the details to sign in.""".format(i))
#    while True:
#       Full_name=str(input("Full Name:"))
#       if validate_Fullname(Full_name):
#          break
#       else:
#          print("Invalid name.Please Enter again")
#    while True:
#       print("Delivery Address:")
#       address=[]
#       for x in range(1,4):
#          line=input("Line {}:".format(x))
#          address.append(line)
#       if validate_address(address):
#          break
#       else:
#          print("Please Enter Address:")
#    while True:
#       email=input("Email Id:")
#       if validate_email(email):
#          break
#       else:
#          print("Please Enter the valid Email:")
#    while True:
#       card_no=input("Card no.:")
#       if validate_cardnumber(card_no):
#          break
#       else:
#          print("Please Enter Valid Card No:")
#    while True:
#       gst_no=input("GST No:")
#       if validate_gst_no(gst_no):
#          break
#       else:
#          print("Please Enter the valid GST No:")
#    print("Thank You")
#    i+=1

#=======================================================================

# import time as t
# items={'sugar':50,'rice':55,'wheat flour':55,
#        'toor dal':150,'rava':70,'Sugar':50,'Rice':55,'Wheat flour':55,'Toor dal':150,'Rava':70}
# print("WELCOME TO THE XYZ SHOP")
# print("50% Off on Wheat Flour and 50% off on the sugar if you buy 2 Kg")
# print("""items list:
#       sugar:50
#       rice:55
#       wheat flour:55
#       Toor dal:150
#       rava:70""")
# print("***********************")
# def discount_wheat(price,kg):
#     price=(price/2)*kg
#     print("You got 50% discount")
#     return price
# def discount_sugar(price,kg):
#     a=kg%2
#     price=(a*price)+(kg-a)*(price/2)
#     return price
#
# def price(price,kg):
#     price=price*kg
#     return price
# def shop(item,kg):
#     if item in (items.keys() or l2):
#         if item=='sugar'or item=='Sugar':
#             a=discount_sugar(items[item],kg)
#             print("You have to pay {} ruppes.".format(a))
#             t.sleep(2)
#         elif item=='wheat flour' or item=='Wheet flour':
#             a=discount_wheat(items[item],kg)
#             print("You have to pay {} ruppes.".format(a))
#             t.sleep(2)
#         elif item=='rice'or item=='Rice' or item=='Toor dal'or item=='toor dal'or item=='rava'or item=='Rava':
#             p=price(items[item],kg)
#             print("You have to pay {} ruppes.".format(p))
#             t.sleep(2)
#         else:
#             print("Invalid Menu Option")
#     else:
#         print("Please Enter item from above list Only.")
# l1=items.keys()
# l2=[]
# for i in l1:
#     l2.append(i.capitalize())
#
# while True:
#      item=input("Enter item:")
#      if item in items.keys() or l2:
#          kg=int(input("How many kgs do you want?"))
#          shop(item,kg)
#      else:
#          print("Please Enter item from above list")
#      t.sleep(1)

#======================================================================
# city_names={'Bangalore':560000,'Hyderabad':500000,'Chennai':600000,'Mumbai':400000}
# def loc_check(location):
#     for i in city_names:
#         if i in location :
#            print(city_names[i])
#            print("Your delivery package reach in 1 or 2 days.")
#            break
#     else:
#         print("Sorry Can't reach")
#
# while True:
#     location = input("Enter Your location:")
#     loc_check(location)

#====================================================================

# def main():
#     products = {
#         "pdcR012": {"type": "Shelf", "price": 0, "quantity": 0, "location": None},
#         "pdcc01": {"type": "Chair", "price": 1500, "quantity": 10, "location": "B1R1C2"},
#         "pdcs11": {"type": "Sofa", "price": 50000, "quantity": 5, "location": None},
#         "pdct01": {"type": "Table", "price": 20000, "quantity": 3, "location": None}
#     }
#
#     product_code = input("Please enter the product code: ").strip()
#     if product_code not in products:
#         print("Please enter a valid product code.")
#         return
#
#     product = products[product_code]
#     if product["quantity"] == 0:
#         print(f"Product Type: {product['type']}")
#         print("Sorry! Out of stock")
#         return
#     print(f"Product Type: {product['type']}")
#
#     if product["type"] == "Sofa" or product["type"] == "Table":
#         total_price = product["price"] + 600
#         print(f"Product Price: {product['price']} + 600/- Rs. Delivery charge.")
#         print(f"Please pay Rs. {total_price}")
#         print("The product will be delivered to your home.")
#     else:
#         print(f"Price: {product['price']}")
#         print(
#             f"You can collect the product in the ground floor, Bay: {product['location'][1]} Row: {product['location'][3]} Column: {product['location'][5]}")
# main()

#==========================================================================

# def product_info(code):
#     if code=="pdcc01":
#         print("Product Type:",product_code[1]['Name'])
#         print("Price:",product_code[1]['Price'])
#         print("You can collect the product in the ground floor, Bay: 1 Row: 1 Column: 2 \n")
#         product_code[1]['Quantity']-=1
#
#     elif code=="pdcs11":
#         print("Product Type: Sofa")
#         print("Product Price: {} + {}/- Rs. Delivery charge.".format(product_code[2]['Price'],600))
#         print("Please pay Rs. {}".format(product_code[2]['Price']+600))
#         print("The product will be delivered to your home.\n")
#
#     elif code=="pdct25":
#         print("Product Type: Table")
#         print("Product Price: {} + {}/- Rs. Delivery charge.".format(product_code[3]['Price'],600))
#         print("Please pay Rs. {}".format(product_code[3]['Price']+600))
#         print("The product will be delivered to your home.\n")
#
#     elif code=="pdcd011":
#         print("Product Type:",product_code[4]['Name'])
#         print("Price:", product_code[4]['Price'])
#         print("You can collect the product in the ground floor, Bay: 4 Row: 2 Column: 3\n")
#         product_code[4]['Quantity']-=1
#
#     elif code=="pdcR012":
#         print("Product Type:",product_code[5]['Name'])
#         print("Price:", product_code[5]['Price'])
#         print("You can collect the product in the ground floor, Bay: 5 Row: 1 Column: 4\n")
#         if product_code[5]['Quantity']==0:
#             print("Sorry! Out of stock\n")
#         else:
#             pass
#         product_code[5]['Quantity']-=1
#
#     else:
#         print("Please Enter the Valid Product Code\n")
#
#
# product_code={1:{'code':"pdcc01",'Name':'Chair','Price':1500,'Location':'B1R1C2','Quantity':2},
#               2:{'code':"pdcs11",'Name':'Sofa','Price':50000,'Location':'B2R4C1','Quantity':'Home'},
#               3:{'code':"pdct25",'Name':'Table','Price':1500,'Location':'B3R3C2','Quantity':'Home'},
#               4:{'code':"pdcd011",'Name':'Desk','Price':900,'Location':'B4R2C3','Quantity':13},
#               5:{'code':"pdcR012",'Name':'Shelf','Price':2500,'Location':'B5R1C4','Quantity':0}
#               }
# i=1
# while(i<1000):
#     print("Sample Case {}".format(i))
#     code=input("Please enter the product code:")
#     i+=1
#     if code=="pdcc01" or "pdcs11" or "pdct25" or "pdcd011" or "pdcR012":
#         product_info(code)
#
#     else:
#         print("Please Enter the Valid Product Code")
#         break
#====================================================================

