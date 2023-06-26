#nCr=n!\((n-r)!*r!)
def fact(x):
    i=1
    for f in range (1,x+1):
        i=i*f
    return i
print "*****Programme For Finding nCr*****"
n=input("Enter n:")
r=input("Enter r:")
c=fact(n)/(fact((n-r))*fact(r))
print n,"C",r,"=",c
