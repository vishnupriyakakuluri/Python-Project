with open('example.txt', 'w') as file:
    file.write("hello i am vishnupriya and i am from andhra.")
keyword='hi'
with open('example.txt','r') as file:
    data=file.read()
    if keyword in data:
        print("present")
    else:
        print("not present")