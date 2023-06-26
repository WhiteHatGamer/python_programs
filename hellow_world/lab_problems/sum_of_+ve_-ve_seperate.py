n=input("Enter The limit")
i=1
ns=0
ps=0
while (i<=n):
    a=input("Enter The Number")
    if (a<0):
        ns=ns+a
    else:
        ps=ps+a
    i=i+1
print ("Sum Of Entered Negative Numbers:",ns)
print ("Sum Of Entered Positive Numbers:",ps)
