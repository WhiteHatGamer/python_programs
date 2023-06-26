s=input("Enter A String")
v="aeiouAEIOU"
cv=0
cu=0
cl=0
cd=0
cs=1
for i in s:
    if (i in v):
        cv=cv+1
    if i.isdigit():
        cd=cd+1
    if i.isupper():
        cu=cu+1
    if i.islower():
        cl=cl+1
    if i.isspace():
        cs=cs+1
print ("Vowels in:",s,"is",cv)
print ("UpperCase in:",s,"is",cu)
print ("LowerCase in:",s,"is",cl)
print ("Digits in:",s,"is",cd)
print ("Words in:",s,"is",cs)
