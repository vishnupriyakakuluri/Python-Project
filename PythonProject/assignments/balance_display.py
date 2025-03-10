banks_database={100	:['Deepthi',1234,0],
101:	['Eva',2345,100000],
102:	['Raghavendra',3456,110000],
103:	['Sthuthi',4567,85000],
104:	['Sujay',5678,50500]
}
acc_no=int(input("Please enter your Account no.:"))
if acc_no in banks_database.keys():
    pass
else:
    print('Entering wrong account no.Please try again.\nPlease visit our bank and create an account')
    exit()
pin=int(input('Please enter the 4 digit pin:'))
if pin==banks_database[acc_no][1]:
    pass
else:
    print('Sorry Invalid Pin.')
    exit()
print('hi ',banks_database[acc_no][0],'\nYour net balance is:',banks_database[acc_no][2])