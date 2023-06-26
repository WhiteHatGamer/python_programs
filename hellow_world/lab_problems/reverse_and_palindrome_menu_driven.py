def rev(x):
    r=0
    while x>0:
        d=int(x%10)
        x=int(x/10)
        r=(r*10)+d
    return r
n=input("Enter Starting Range:")
b=input("Enter Ending Range:")
print ("1. Reverse\n2. Palindrome")
c=input("Enter Your Choice:")
if c==1:
    for i in range(n,b+1):
        print (rev(i))
elif c==2:
    for i in range(n,b+1):
        if rev(i)==i:
            print (i,)
else:
    print("Invalid Input")
