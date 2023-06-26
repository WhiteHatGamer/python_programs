l=[]
n=input("enter The Size:")
for i in range (n):
    x=input("Enter A Value:")
    l.append(x)
print l
while(True):
    print "1. Insert\n2. Delete\n3. Replace\n4. Quit"
    ch=input("Enter Your Choice:")
    if ch==1:
        x=input("Enter The Value To be Inserted:")
        i=input("Enter The Place You Want To Insert:")
        l.insert(i,x)
        print l
    elif ch==2:
        x=input("Enter The Value To Be Deleted:")
        if x in l:
            l.remove(x)
            print l
        else:
            print x,"Is Not In",l
    elif ch==3:
        x=input("enter The Value to be replaced:")
        y=input("Enter The Value To be Insterted:")
        if x in l:
            i=l.index(x)
            l.pop(i)
            l.insert(i,y)
            print l
        else:
            print x,"Is Not In",l
    elif ch==4:
        break
    else:
        print "Invalid Choice"
