n=input("Enter A Number")
s=0
for i in range (1,n):
    if (n%i==0):
        s=s+i
    i=i+1
if (s==n):
    print n,"is a Perfect Number"
else:
    print n,"is not a Perfect Number"
