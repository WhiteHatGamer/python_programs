u=int(input("Enter the Units Consumed:"))
if(u<=200):
    print ("Rate of Electricity Usage=",u)
elif(u<=300):
    Rate=200+((u-200)*2)
    print ("Rate of Electricity Usage=",Rate)
elif(u<=400):
    Rate=400+((u-300)*5)
    print ("Rate of Electricity Usage=",Rate)
else:
    Rate=u*10
    print ("Rate of Electricity Usage=",Rate)
