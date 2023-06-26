def concatenate(a,b):
    s=a+b
    print (s)
def compare(a,b):
    i=a[0]
    j=b[0]
    if len(a)==len(b):
        if i<j:
            print (b,"Is Greater Than",a)
        elif j<i:
            print (a,"Is Greater Than",b)
        else:
            c=0
            for i in range (0,len(a),1):
                if (a[i]==b[i]):
                    continue
                else:
                    c=c+1
                    break
            if c==0:
                print ("equal")
    else:
        if len(a)<len(b):
            print (b,"is greater than",a)
        else:
            print (a,"is greater than",b)
a=input("Enter First String:")
b=input("Enter Second String:")
print ("1.Concatenate")
print ("2.Compare")
c=int(input("Enter Your Choice:"))
if c==1:
    concatenate(a,b)
elif c==2:
    compare(a,b)
else:
    print ("Invavid Choice")
#if a>b:
        #print a,"is greater than",b
    #elif a>b:
        #print a,"is lower than",b
    #else:
        #print a,"is Equal to",b
