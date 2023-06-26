n=input("Enter A Number")
c=0
for i in range (1,(n+1),1):
    if n%i==0:
        c=c+1
    else:
        continue
if c==2:
    print ("Prime Number")
else:
    print ("Not A Prime")
