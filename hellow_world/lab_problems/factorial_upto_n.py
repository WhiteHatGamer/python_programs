n=int(input("Enter The Limit:"))
i=1
f=1
j=1
if (n==0):
    print ("0!=1")
else:
    while (i<=n):
        while (j<=i):
            f=f*j
            j=j+1
        print (i,"factorial =",f)
        i=i+1
