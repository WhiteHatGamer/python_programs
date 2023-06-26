p=input("Enter The Number Of Passengers")
c=input("Choices Of Travel\n\t1. Sleeper Class\n\t2. AC II Tier\n\t3. AC III Tier\n\t4. AC First Class\nYour Choice:")
if(c==1):
    print("Total ticket Fare",p*150)
elif(c==2):
    print("Total ticket Fare",p*400)
elif(c==3):
    print("Total ticket Fare",p*750)
elif(c==4):
    print("Total ticket Fare",p*1000)
else:
    print("Invalid Choice")
