#feedback
name=input("Enter your name:")
product_name=input("Enter the product name:")
feedback=input("Write your feedback here and help us to improve the service:")
print("Thank you for your valuable feedback on the product.")
file1=open(product_name+'.txt','a+')
file1.write("{} says: {} \n".format(name,feedback))