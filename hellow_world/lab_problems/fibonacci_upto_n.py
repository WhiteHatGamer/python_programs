n=int(input("fibonacci: "))
x=0
y=1
c=2
print (x)
print (y)
while (c<n):
    z=x+y
    x=y
    y=z
    print (z)
    c=c+1
